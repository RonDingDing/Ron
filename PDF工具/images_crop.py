from __future__ import annotations
from PIL import Image
import os


def crop_left_right(filename: str) -> None:
    # 左右一分为二
    abs_path = os.path.abspath(filename)
    img = Image.open(abs_path)
    width, height = img.size
    boxes = [(width / 2, 0, width, height), (0, 0, width / 2, height)]
    output_path = os.path.join(abs_path.split(".")[0], "output")
    return crop(img, output_path, boxes)


def crop(img: Image, output_path: str, boxes: list[tuple[float]]) -> None:
    os.makedirs(output_path, exist_ok=True)
    for i, box in enumerate(boxes):
        new_img = img.crop(box)
        while os.path.isfile(f"{output_path}/{i}.jpg"):
            i += 1
        new_img.save(f"{output_path}/{i}.jpg")


def rename(ori_names: list[str]) -> None:
    digits = len(str(len(ori_names)))
    for filename in ori_names:
        base_with_dir, ext = os.path.splitext(filename)
        first, *last = os.path.basename(base_with_dir).split("_", 1)
        if len(first) < digits:
            dir_name = os.path.dirname(filename)
            new_fname = f"{first.zfill(digits)}{''.join(last)}{ext}"
            new_name = os.path.join(dir_name, new_fname)
            os.rename(filename, new_name)


def find_all(abs_base_path: str, suffix: str) -> None:
    ori_names = []
    for a in os.listdir(abs_base_path):
        filename = os.path.join(abs_base_path, a)
        if os.path.isfile(filename) and filename.endswith(suffix):
            ori_names.append(filename)
    return ori_names


def crop_pics_in_folder(basepath: str, suffix=".jpg") -> None:
    abs_base_path = os.path.abspath(basepath)
    ori_names = find_all(abs_base_path, suffix)
    rename(ori_names)
    new_names = find_all(abs_base_path, suffix)

    for name in new_names:
        crop_left_right(name)
    output_path = os.path.join(abs_base_path.split(".")[0], "output")
    files = find_all(output_path, suffix)
    rename(files)


if __name__ == "__main__":
    crop_pics_in_folder(r"C:\Users\Administrator\Desktop\111\倪海厦天纪系列之天机道.pdf_dir")
