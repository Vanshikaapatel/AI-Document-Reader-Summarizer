import re

def detect_document_type(text):
    text_lower = text.lower()

    # Research Paper Keywords
    research_keywords = ["abstract", "methodology", "results", "discussion", "conclusion", "references"]
    
    # Notes Keywords
    notes_keywords = ["chapter", "topic", "unit", "definition", "example", "note:", "summary"]

    # Assignment Keywords
    assignment_keywords = ["question", "assignment", "solve", "explain", "write short note"]

    # Legal Document
    legal_keywords = ["hereby", "whereas", "plaintiff", "defendant", "contract", "agreement", "section"]

    # Invoice Keywords
    invoice_keywords = ["invoice", "amount", "price", "billing", "gst", "total payable"]

    # Medical Report
    medical_keywords = ["diagnosis", "prescription", "bp", "blood test", "treatment", "symptoms"]

    # Matching Logic
    if any(k in text_lower for k in research_keywords):
        return "Research Paper"

    if any(k in text_lower for k in notes_keywords):
        return "Notes"

    if any(k in text_lower for k in assignment_keywords):
        return "Assignment"

    if any(k in text_lower for k in legal_keywords):
        return "Legal Document"

    if any(k in text_lower for k in invoice_keywords):
        return "Invoice"

    if any(k in text_lower for k in medical_keywords):
        return "Medical Report"

    return "General Document"



def adjust_summary_prompt(doc_type, text):
    """Modifies the summarization text based on detected document type."""

    if doc_type == "Research Paper":
        return (
            "Summarize this RESEARCH PAPER focusing on Abstract → Methods → Results → Conclusion.\n\n"
            + text
        )

    if doc_type == "Notes":
        return (
            "Summarize these NOTES in simple bullet points for studying.\n\n"
            + text
        )

    if doc_type == "Assignment":
        return (
            "Summarize this ASSIGNMENT with clear explanations and key answers.\n\n"
            + text
        )

    if doc_type == "Legal Document":
        return (
            "Summarize this LEGAL DOCUMENT in simple language, explaining key clauses.\n\n"
            + text
        )

    if doc_type == "Invoice":
        return (
            "Summarize this INVOICE by listing important items, amounts, GST, and final payable.\n\n"
            + text
        )

    if doc_type == "Medical Report":
        return (
            "Summarize this MEDICAL REPORT focusing on diagnosis, tests, and treatment.\n\n"
            + text
        )

    return "Summarize this document:\n\n" + text
