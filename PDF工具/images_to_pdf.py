import os
from jpg2pdf import create


def jpgs_to_pdf(jpgs_path: str) -> None:
    with create(os.path.join(jpgs_path, "test.pdf")) as pdf:
        abs_path = os.path.abspath(jpgs_path)
        for i in os.listdir(abs_path):
            filepath = os.path.join(abs_path, i)
            if os.path.isfile(filepath) and filepath.endswith("jpg"):
                pdf.add(filepath)


if __name__ == "__main__":
    jpgs_to_pdf(r"C:\Users\Administrator\Desktop\111\倪海厦天纪系列之天机道\output")
