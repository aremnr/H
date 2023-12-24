import os
from PIL import Image
import shutil



def start():
    if not(os.path.isdir("./temp_imges_for_pdf/")):
        os.mkdir("./temp_imges_for_pdf/")
    shutil.rmtree("./temp_imgs/")

def convert_to_pdf(ImagesList: list):
    start()
    images = [
        Image.open("./temp_imges_for_pdf/" + f)
        for f in ImagesList
    ]

    pdf_path = "Output/output.pdf"

    images[0].save( 
        pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
    )
    shutil.rmtree("temp_imges_for_pdf")
    os.system("mv Output/output.pdf ../../Output")
    shutil.rmtree("Output")
