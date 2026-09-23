"""Load documents from disk and extract their text."""

from pathlib import Path

from pypdf import PdfReader


def load_pdf(path: Path) -> str:
    """Return the text content of a PDF file.

    Args:
        path: Location of the PDF file.

    Returns:
        The extracted text, with pages joined by newlines.
    """
    reader = PdfReader(path)
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages)


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent.parent
    docs_dir = project_root / "data" / "docs"

    for pdf_path in sorted(docs_dir.glob("*.pdf")):
        text = load_pdf(pdf_path)
        print(f"{pdf_path.name}: {len(text)} characters")
        print(text[:400])
        print("---")