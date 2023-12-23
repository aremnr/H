from pdf2image import convert_from_path
import shutil
import os
shutil.rmtree("/home/ar/Documents/Hachaton/temp_imgs/")
os.mkdir("/home/ar/Documents/Hachaton/temp_imgs/")
def PdfToImg(pdf_path):
    pages = convert_from_path("/home/ar/Documents/Hachaton/PDF/Example.pdf", dpi=800, size=3000)
    for count, page in enumerate(pages):
        page.save(f'/home/ar/Documents/Hachaton/temp_imgs/out{count}.png', 'PNG')