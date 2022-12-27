from PIL import Image
import pytesseract


def ocr(filename: str) -> None:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Tools\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(filename), lang="chi_tra")
    return text


if __name__ == "__main__":
    t=ocr(r"C:\Users\Administrator\Desktop\111\倪海厦天纪系列之天机道.pdf_dir\1_倪海厦天纪系列之天机道.pdf.jpg")
    print(t)