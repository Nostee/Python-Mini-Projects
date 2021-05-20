import PyPDF2
import sys

filesToBeWatermarked = sys.argv[1:]
watermark = PyPDF2.PdfFileReader(open("wtr.pdf","rb"))

for f in filesToBeWatermarked:
    pdf_file = PyPDF2.PdfFileReader(open(f"{f}","rb"))
    num_of_pages = pdf_file.numPages

    writer = PyPDF2.PdfFileWriter()

    for p in range(num_of_pages):
        page_of_current_pdf = pdf_file.getPage(p)
        page_of_current_pdf.mergePage(watermark.getPage(0))
        writer.addPage(page_of_current_pdf)

    writer.write(open(f"./Watermarked/{f}","wb"))