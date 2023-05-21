import PyPDF2

original_path = 'pdf_combinated.pdf'
output_path = 'watermark_pdf.pdf'
watermark = 'wtr.pdf'

original = PyPDF2.PdfReader(open(original_path, 'rb'))
pdf_writer = PyPDF2.PdfWriter()

pdf_watermark = PyPDF2.PdfReader(open(watermark, 'rb')).pages[0]

for page in original.pages:
    page.merge_page(pdf_watermark)
    pdf_writer.add_page(page)

with open(output_path, 'wb') as output_pdf:
    pdf_writer.write(output_pdf)

