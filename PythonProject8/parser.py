import pdfplumber


def extract_text_from_pdf(file_path):
    """
    Extracts all text from a PDF file.

    Parameters:
    - file_path: Path to the PDF file (string or file-like object)

    Returns:
    - Extracted text (string)
    """
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

    return text


def clean_text(text):
    """
    Cleans extracted text by removing excessive spaces and newlines.

    Parameters:
    - text: Raw text (string)

    Returns:
    - Cleaned text (string)
    """
    import re
    # Replace multiple spaces with a single space and remove leading/trailing whitespace
    cleaned = re.sub(r'\s+', ' ', text).strip()
    return cleaned