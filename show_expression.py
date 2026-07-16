from PIL import Image
import os

IMAGE_DIR = "images"

def show(expression):
    path = os.path.join(IMAGE_DIR, f"{expression}.png")

    if not os.path.exists(path):
        print(f"이미지를 찾을 수 없습니다: {path}")
        return

    img = Image.open(path)
    img.show()


if __name__ == "__main__":
    show("slight_smile01")