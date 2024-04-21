from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import lightgrey
from reportlab.lib.units import inch

margin = 72
page_width = 8.27 * inch
page_height = 11.69 * inch
section_height = page_height / 6

c = canvas.Canvas("new_example.pdf")
c.setStrokeColor(lightgrey)

for i in range(1, 6):
    c.line(0, i * section_height, page_width, i * section_height)

c.save()
