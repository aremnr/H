import sys
import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QVBoxLayout, QHBoxLayout,
                             QListWidget, QFileDialog, QTextEdit)

from img_proc import ImageProcess

EXTENSIONS = ["png", "jpeg", "pdf", "docx", "xlsx"]

app = QApplication(sys.argv)
processor = ImageProcess()

# Widgets
window = QWidget()
window.setWindowTitle("Anonimizer")
window.resize(1000, 600)

btn_choose_dir = QPushButton("Папка")
btn_rotate_left = QPushButton("PDF")
btn_rotate_right = QPushButton("PNG")
btn_do_mirror = QPushButton("JPEG")
btn_sharpness = QPushButton("DOCX")
btn_bw = QPushButton("XLSX")

files_list = QListWidget()

image = QLabel("Картинка")
image.setAlignment(Qt.AlignCenter)

# Layouts
main_layout = QHBoxLayout()
left_layout = QVBoxLayout()
right_layout = QVBoxLayout()
label_layout = QHBoxLayout()
btn_layout = QHBoxLayout()

# Connect widgets to layout
main_layout.addLayout(left_layout)
left_layout.addWidget(btn_choose_dir)
left_layout.addWidget(files_list)
label_layout.addWidget(image, 95)
main_layout.addLayout(right_layout, 20)

btn_layout.addWidget(btn_rotate_left)
btn_layout.addWidget(btn_rotate_right)
btn_layout.addWidget(btn_do_mirror)
btn_layout.addWidget(btn_sharpness)
btn_layout.addWidget(btn_bw)
right_layout.addLayout(label_layout)
right_layout.addLayout(btn_layout, 80)

window.setLayout(main_layout)


# Functional
def show_files_list():
    workdir = QFileDialog.getExistingDirectory()
    if not workdir:
        return
    os.chdir(workdir)
    files_names = os.listdir(workdir)
    files_list.clear()
    files_images = filter(is_image, files_names)
    files_list.addItems(files_images)


def is_image(filename):
    file_path = os.path.join(os.getcwd(), filename)
    if not os.path.isfile(file_path):
        return False
    return filename.split(".")[-1] in EXTENSIONS


def show_image(workdir, filename):
    if filename.split(".")[-1] == "docx":
        pixmap_image = QPixmap.fromImage(processor.image)
    else:
        fpath = os.path.join(workdir, filename)
        pixmap_image = QPixmap(fpath)
    width, height = image.width(), image.height()
    pixmap_image = pixmap_image.scaled(width, height, Qt.KeepAspectRatio)
    image.setPixmap(pixmap_image)


def show_chosen_image():
    if files_list.currentRow():
        filename = files_list.currentItem().text()
        processor.load_image(os.getcwd(), filename)
        show_image(os.getcwd(), filename)


def do_gray():
    if not processor.image:
        return
    image_path = processor.do_gray()
    show_image(image_path)


def rotate_left():
    if not processor.image:
        return
    image_path = processor.rotate_left()
    show_image(image_path)


def rotate_right():
    if not processor.image:
        return
    image_path = processor.rotate_right()
    show_image(image_path)


def rotate_mirror():
    if not processor.image:
        return
    image_path = processor.rotate_mirror()
    show_image(image_path)


def make_sharpness():
    if not processor.image:
        return
    image_path = processor.make_sharpness()
    show_image(image_path)


btn_choose_dir.clicked.connect(show_files_list)
files_list.currentRowChanged.connect(show_chosen_image)
btn_bw.clicked.connect(do_gray)
btn_rotate_left.clicked.connect(rotate_left)
btn_rotate_right.clicked.connect(rotate_right)
btn_do_mirror.clicked.connect(rotate_mirror)
btn_sharpness.clicked.connect(make_sharpness)
window.show()
app.exec()