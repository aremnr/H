import pypdfium2 as pdfium
import img_work, os

def start():
    if not(os.path.isdir("./temp_imgs/")):
        os.mkdir("./temp_imgs/")

def pdf_processing(path: str):
    start()
    pdf = pdfium.PdfDocument(path)
    n_pages = len(pdf)
    for page_number in range(n_pages):
        page = pdf.get_page(page_number)
        pil_image = page.render(
        scale=10,
        rotation=0,
        crop=(0, 0, 0, 0)).to_pil()
        pil_image.save(f"./temp_imgs/out{page_number+1}.png")
    img_work.pdf()