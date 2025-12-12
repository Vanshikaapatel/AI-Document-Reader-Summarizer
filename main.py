import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "summarizer"))

import argparse
from summarizer.pdf_reader import extract_text_from_pdf
from summarizer.text_preprocess import clean_text
from summarizer.summarize_model import summarize_text


def parse_args():
    parser = argparse.ArgumentParser(description="AI Document Reader & Summarizer")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("--mode", choices=["abstractive", "extractive"], default="abstractive")
    parser.add_argument("--output", default=None, help="Output file for summary")
    parser.add_argument("--max_len", type=int, default=200)
    parser.add_argument("--ocr", action="store_true", help="Use OCR for scanned PDFs")
    return parser.parse_args()


def main():
    args = parse_args()
    raw = extract_text_from_pdf(args.pdf_path, use_ocr=args.ocr)

    if not raw.strip():
        print("No text found. Try --ocr")
        return

    cleaned = clean_text(raw)
    summary = summarize_text(cleaned, mode=args.mode, max_length=args.max_len)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(summary)
        print(f"Saved to {args.output}")
    else:
        print(summary)


if __name__ == "__main__":
    main()
