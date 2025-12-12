import re

def clean_text(text):
    text = text.replace("\r", "\n")
    text = re.sub(r"\n{2,}", "\n\n", text)
    text = re.sub(r"\n\s*\d+\s*\n", "\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def chunk_text(text, max_chars=1000):
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunk, length = [], 0

    for p in paras:
        if length + len(p) <= max_chars:
            chunk.append(p)
            length += len(p)
        else:
            yield "\n\n".join(chunk)
            chunk, length = [p], len(p)

    if chunk:
        yield "\n\n".join(chunk)
