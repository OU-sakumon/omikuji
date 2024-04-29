import os
from reportlab.pdfgen import canvas
from reportlab.lib.colors import lightgrey
from reportlab.lib.units import inch
from reportlab.platypus import Image
from pdf2image import convert_from_path
from datetime import datetime

# import pdf
## specify the directory-name
## import from `pdf`
# convert pdf into png
# add png to pdf
# draw lines on pdf

def add_pdf():
    # Specify the directory
    omikuji_gen_path = os.getcwd()
    backend_path = os.path.dirname(omikuji_gen_path)
    pdf_path = os.path.join(backend_path, "pdf")    
    imported_pdf = os.listdir(pdf_path)
    png_path = os.path.join(backend_path, "png")
    
    os.makedirs(png_path, exist_ok=True)
    
    png_images = []

    for pdf in imported_pdf:
        # Convert the PDF to images
        images = convert_from_path(os.path.join(pdf_path, pdf))

        # Save each image
        for i, image in enumerate(images):
            image_path = os.path.join(png_path, f'{os.path.splitext(pdf)[0]}_{i}.png')
            image.save(image_path, 'PNG')
            png_images.append(image_path)
            
    now = datetime.now()
    timestamp = now.strftime("%Y_%m_%d_%H_%M")
    c = canvas.Canvas(f"{timestamp}.pdf")
    
    pages_needed = len(png_images) // 6 + (len(png_images) % 6 > 0)
    
    page_width = 8.27 * inch
    page_height = 11.69 * inch
    section_height = page_height / 6

    for page in range(pages_needed):
        for i in range(6):
            image_index = page * 6 + i
            if image_index < len(png_images):
                # Add the image to the PDF. Adjust the position as needed.
                c.drawImage(png_images[image_index], 0, i * section_height, width=page_width, height=section_height)

        c.setStrokeColor(lightgrey)
    
        for i in range(1, 6):
            c.line(0, i * section_height, page_width, i * section_height)
        
        c.showPage()  # End the current page and start a new one
    
    c.save()

add_pdf()