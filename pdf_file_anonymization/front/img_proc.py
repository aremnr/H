import os
from PIL import Image, ImageFilter
from docx2png import docx_to_img


class ImageProcess:
    def __init__(self):
        self.image = None
        self.basedir = None
        self.filename = None
        self.save_dir_name = "modified"

    def load_image(self, dir: str, filename):
        image_path = os.path.join(dir, filename)
        if os.path.exists(image_path):
            self.basedir = dir
            self.filename = filename
            if image_path.split(".")[-1] == "docx":
                self.image = docx_to_img(dir, filename)
            else:
                self.image = Image.open(image_path)

    def save_image(self):
        if self.image:
            path_to_dir = os.path.join(self.basedir, self.save_dir_name)
            if not os.path.isdir(path_to_dir):
                os.mkdir(path_to_dir)
            image_path = os.path.join(path_to_dir, self.filename)
            self.image.save(image_path)
            return image_path

    def do_gray(self):
        if self.image is None:
            return
        self.image = self.image.convert("L")
        image_path = self.save_image()
        return image_path

    def rotate_left(self):
        if self.image is None:
            return
        self.image = self.image.transpose(Image.ROTATE_90)
        image_path = self.save_image()
        return image_path

    def rotate_right(self):
        if self.image is None:
            return
        self.image = self.image.transpose(Image.ROTATE_270)
        image_path = self.save_image()
        return image_path

    def rotate_mirror(self):
        if self.image is None:
            return
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        image_path = self.save_image()
        return image_path

    def make_sharpness(self):
        if self.image is None:
            return
        self.image = self.image.filter(ImageFilter.SHARPEN)
        image_path = self.save_image()
        return image_path
