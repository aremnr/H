# from pdf2image import convert_from_path
# import shutil
# import os
# shutil.rmtree("/home/ar/Documents/Hachaton/temp_imgs/")
# os.mkdir("/home/ar/Documents/Hachaton/temp_imgs/")
# def PdfToImg(pdf_path):
#     pages = convert_from_path("/home/ar/Documents/Hachaton/PDF/Example.pdf", dpi=800, size=3000)
#     for count, page in enumerate(pages):
#         page.save(f'/home/ar/Documents/Hachaton/temp_imgs/out{count}.png', 'PNG')


import pypdfium2 as pdfium
pdf = pdfium.PdfDocument("/home/ar/Documents/Hachaton/r.pdf")
n_pages = len(pdf)
for page_number in range(n_pages):
    page = pdf.get_page(page_number)
    pil_image = page.render(
    scale=10,
    rotation=0,
    crop=(0, 0, 0, 0),

    
    ).to_pil()
    pil_image.save(f"/home/ar/Documents/Hachaton/temp_imgs/out{page_number+1}.png")
