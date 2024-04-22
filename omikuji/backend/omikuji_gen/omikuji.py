from reportlab.pdfgen import canvas
from reportlab.lib.colors import lightgrey
from reportlab.lib.units import inch
from PyPDF2 import PdfWriter, PdfReader

# Open the files you want to import
files_to_import = ["file1.pdf", "file2.pdf", "file3.pdf"]
for file_name in files_to_import:
    input_stream = open(file_name, "rb")
    input_pdf = PdfReader(input_stream)

    # Add the pages from the input file to the output file
    for i in range(len(input_pdf.pages)):
        output.add_page(input_pdf.pages[i])

output = PdfWriter()

# Write the output file
output_stream = open("merged.pdf", "wb")
output.write(output_stream)

page_width = 8.27 * inch
page_height = 11.69 * inch
section_height = page_height / 6

c = canvas.Canvas("new_example.pdf")
c.setStrokeColor(lightgrey)

for i in range(1, 6):
    c.line(0, i * section_height, page_width, i * section_height)

c.save()
