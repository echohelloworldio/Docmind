from pathlib import Path
from pypdf import PdfReader


def load_pdfs(folder: str) -> list[dict]:
    """Read every PDF in a folder and return one record per page."""
    pages = []
    for pdf_path in Path(folder).glob("*.pdf"):
        reader = PdfReader(pdf_path)
        for page_num, page in enumerate(reader.pages, start=1):
            text = (page.extract_text() or "").strip()
            if not text:
                continue  # skip blank or image-only pages
            pages.append({
                "text": text,
                "source": pdf_path.name,
                "page": page_num,
            })
    return pages


if __name__ == "__main__":
    docs = load_pdfs("data")
    print(f"Loaded {len(docs)} pages")
    print(docs[0]["source"], docs[0]["page"])
    print(docs[0]["text"][:300])