import os
import img_work
def start():
    if os.path.isdir("./temp_imgs/"):
        os.mkdir("./temp_imgs/")

def img_processing(path):
    start()
    img_work.img(path)