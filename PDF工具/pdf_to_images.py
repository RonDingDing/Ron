import os
from pdf2jpg import pdf2jpg


def pdf_to_jpgs(pdf_path: str) -> None:
    pdf2jpg.convert_pdf2jpg(pdf_path, os.path.dirname(pdf_path), dpi=300, pages="ALL")


if __name__ == "__main__":
    pdf_to_jpgs(r"C:\Users\Administrator\Desktop\111\倪海厦天纪系列之天机道.pdf")
