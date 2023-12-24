import sys
import os
import send
from pdf2image import convert_from_path
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QVBoxLayout, QHBoxLayout,
                             QListWidget, QFileDialog)



EXTENSIONS = ["pdf", "png", "jpeg", "jpg"]
wrkdr = ""
flnm = ""

app = QApplication(sys.argv)
#processor = ImageProcess()

# Widgets
window = QWidget()
window.setWindowTitle("Anonimizer")
window.resize(1000, 600)

btn_choose_dir = QPushButton("Папка")
btn_save_pdf = QPushButton("Process")



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

btn_layout.addWidget(btn_save_pdf)
right_layout.addLayout(label_layout)
right_layout.addLayout(btn_layout, 80)

window.setLayout(main_layout)


# Functional
def show_files_list():
    global wrkdr
    workdir = QFileDialog.getExistingDirectory()
    wrkdr = workdir
    if not workdir:
        return
    os.chdir(workdir)
    files_names = os.listdir(workdir)
    files_list.clear()
    files_images = filter(is_in_extens, files_names)
    files_list.addItems(files_images)


def is_in_extens(filename):
    file_path = os.path.join(os.getcwd(), filename)
    if not os.path.isfile(file_path):
        return False
    return filename.split(".")[-1] in EXTENSIONS


def show_image(wrkdr, flnm):
    if flnm.split(".")[-1] == "pdf":
        convert_from_path(os.path.join(wrkdr, flnm), first_page=0, last_page=1)[0].save("trash.png")
        pixmap_image = QPixmap("trash.png")
        os.remove("trash.png")
    else:
        fpath = os.path.join(wrkdr, flnm)
        pixmap_image = QPixmap(fpath)
    width, height = image.width(), image.height()
    pixmap_image = pixmap_image.scaled(width, height, Qt.KeepAspectRatio)
    image.setPixmap(pixmap_image)


def show_chosen_image():
    global flnm
    filename = files_list.currentItem().text()
    flnm = filename
    show_image(os.getcwd(), filename)

def save_pdf():
    send.file_send(os.path.join(wrkdr, flnm), flnm.split(".")[-1])

btn_choose_dir.clicked.connect(show_files_list)
files_list.currentRowChanged.connect(show_chosen_image)
btn_save_pdf.clicked.connect(save_pdf)
window.show()
app.exec()