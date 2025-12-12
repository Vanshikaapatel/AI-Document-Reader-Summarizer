from summarizer.text_preprocess import chunk_text    # ✔ correct import

import streamlit as st

@st.cache_data(show_spinner=False)
def summarize_text(text, mode="abstractive", max_length=200):
    from summarizer.document_classifier import detect_document_type, adjust_summary_prompt

    # Auto-switch to FAST extractive mode for large files
    if len(text) > 8000:
        mode = "extractive"

    # Detect document type
    doc_type = detect_document_type(text)
    prompt_text = adjust_summary_prompt(doc_type, text)

    # Abstractive Summarization
    if mode == "abstractive":
        try:
            return _abstractive(prompt_text, max_length)
        except:
            return _extractive(prompt_text, max_length)

    # Extractive Summarization
    return _extractive(prompt_text, max_length)



def adjust_summary_prompt(doc_type, text):
    if doc_type == "Research Paper":
        return "Summarize this research paper focusing on abstract, methods, results, and conclusion:\n" + text

    if doc_type == "Notes":
        return "Summarize these study notes in simple language with bullet points:\n" + text

    if doc_type == "Assignment":
        return "Summarize this assignment clearly and concisely with key points:\n" + text

    if doc_type == "Legal Document":
        return "Summarize this legal document by explaining clauses in easy language:\n" + text

    if doc_type == "Invoice":
        return "Summarize this invoice by listing amounts, items, and total payable:\n" + text

    if doc_type == "Medical Report":
        return "Summarize this medical report focusing on diagnosis, tests, and treatment:\n" + text

    return "Summarize this document:\n" + text


def _abstractive(text, max_length):
    from transformers import pipeline
    summarizer = pipeline("summarization", model="philschmid/bart-large-cnn-samsum")

    chunks = list(chunk_text(prompt_text))
    out = []

    for c in chunks:
        s = summarizer(c, max_length=max_length, min_length=30, do_sample=False)[0]["summary_text"]
        out.append(s)

    return "\n\n".join(out)


def _extractive(text, max_length):
    try:
        from gensim.summarization import summarize
        return summarize(text, word_count=max_length)
    except:
        return " ".join(text.split()[:max_length])


from summarizer.document_classifier import detect_document_type, adjust_summary_prompt

def summarize_text(text, mode="abstractive", max_length=200):
    doc_type = detect_document_type(text)
    prompt_text = adjust_summary_prompt(doc_type, text)

    if mode == "abstractive":
        try:
            return _abstractive(text, max_length)
        except:
            return _extractive(text, max_length)

    return _extractive(text, max_length)
