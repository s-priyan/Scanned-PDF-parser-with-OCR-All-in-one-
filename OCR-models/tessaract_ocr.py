from PIL import Image
import fitz
from pdf2image import convert_from_path
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# # Simple image to string
# print(pytesseract.image_to_string(Image.open("source/20259004608180_toc.png")))
# To get better resolution
file_name = '05-413733_Chapter 07_Font Space Issue'
input_file = f"edge-case-sources/{file_name}.pdf"

pages = convert_from_path(input_file, 500)

# doc = fitz.open("source/20259004608180_toc.pdf")  # open document

    # Extract text from each page using Tesseract OCR
text_data = ''
for page in pages:
    text = pytesseract.image_to_string(page)
    text_data += text + '\n'

mkd_file_path = f'edge-case-results-tesseract/{file_name}.md'

with open(mkd_file_path, "w", encoding="utf-8") as f:
    f.write(text_data)
# # In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# # NOTE: In this case you should provide tesseract supported images or tesseract will return error
# print(pytesseract.image_to_string("source/20259004609379.png"))

# # List of available languages
# print(pytesseract.get_languages(config=''))

# # # French text image to string
# # print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))

# # # Batch processing with a single file containing the list of multiple image file paths
# # print(pytesseract.image_to_string('images.txt'))

# # Timeout/terminate the tesseract job after a period of time
# try:
#     print(pytesseract.image_to_string('test.jpg', timeout=2)) # Timeout after 2 seconds
#     print(pytesseract.image_to_string('test.jpg', timeout=0.5)) # Timeout after half a second
# except RuntimeError as timeout_error:
#     # Tesseract processing is terminated
#     pass

# # Get bounding box estimates
# print(pytesseract.image_to_boxes(Image.open("source/20259004608180_toc.png")))

# # Get verbose data including boxes, confidences, line and page numbers
# print(pytesseract.image_to_data(Image.open("source/20259004608180_toc.png")))

# # Get information about orientation and script detection
# print(pytesseract.image_to_osd(Image.open("source/20259004608180_toc.png")))

# # Get a searchable PDF
# pdf = pytesseract.image_to_pdf_or_hocr("source/20259004608180_toc.png", extension='pdf')
# with open("results/ressaract.pdf", 'w+b') as f:
#     f.write(pdf) # pdf type is bytes by default

# # Get HOCR output
# hocr = pytesseract.image_to_pdf_or_hocr("source/20259004608180_toc.png", extension='hocr')

# # Get ALTO XML output
# xml = pytesseract.image_to_alto_xml("source/20259004608180_toc.png")

# # getting multiple types of output with one call to save compute time
# # currently supports mix and match of the following: txt, pdf, hocr, box, tsv
# text, boxes = pytesseract.run_and_get_multiple_output("source/20259004608180_toc.png", extensions=['txt', 'box'])