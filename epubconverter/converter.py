import zipfile
from bs4 import BeautifulSoup
import pdfkit

def extract_epub_content(epub_path, extract_to):
    """
    Extract the content of an EPUB file to a directory.

    Args:
    - epub_path: Path to the EPUB file.
    - extract_to: Directory to extract contents to.

    Returns:
    - List of paths of extracted content.
    """
    with zipfile.ZipFile(epub_path, 'r') as z:
        z.extractall(extract_to)
        return z.namelist()

def convert_html_to_pdf(html_path):
    """
    Convert an HTML file to PDF.

    Args:
    - html_path: Path to the HTML file.

    Returns:
    - Binary content of the PDF.
    """
    return pdfkit.from_file(html_path, False)