from docx2pdf import convert
import os
from PIL import Image
from pdf2image import convert_from_path

def docx_to_img(workdir, filename):
    convert(os.path.join(workdir, filename), os.path.join(workdir, "temp.pdf"))
    img = convert_from_path(os.path.join(workdir, "temp.pdf"), poppler_path="C:/Program Files/poppler-23.11.0/Library/bin")
    os.remove(os.path.join(workdir, "temp.pdf"))
    img[0].save(os.path.join(workdir, "temp.png"))

#image = docx_to_img("C:/Users/Кирилл/Desktop", "10.docx")
