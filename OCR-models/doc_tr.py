from doctr.models import ocr_predictor
from doctr.io import DocumentFile
import matplotlib.pyplot as plt
# import pdfkit
from lxml import etree

model = ocr_predictor(det_arch='db_resnet50', reco_arch='crnn_vgg16_bn', pretrained=True)

# PDF
# pdf_doc = DocumentFile.from_pdf("source/20259004608180_toc.pdf")
pdf_doc = DocumentFile.from_pdf("source/20259004609379.pdf")

# Analyze
result = model(pdf_doc)

synthetic_pages = result.render()

print(synthetic_pages)

# # Save to a file
# with open("results/doc-tr.xml", "w", encoding="utf-8") as file:
#     file.write(synthetic_pages.decode("utf-8"))



# # Load and transform XML using XSLT
# xml = etree.parse('input.xml')
# xslt = etree.parse('template.xsl')
# transform = etree.XSLT(xslt)
# html = transform(xml)

# # Save to HTML
# with open("output.html", "w") as f:
#     f.write(str(html))

# # Convert to PDF
# pdfkit.from_file("output.html", "output.pdf")


# print(synthetic_pages)

# lines = result.pages[0].blocks[0].lines

# # print(lines)
# text = ""
# for line in lines:
#     words = line.words
#     senetence = " ".join([word.value for word in words]) + '\n'
#     text += senetence
# # print(text)


# # Write the text to the file
# with open("results/doc-tr.md", "w", encoding="utf-8") as file:
#     file.write(text)


# result.show()


# synthetic_pages = result.synthesize()
# plt.imshow(synthetic_pages[0]); plt.axis('off'); plt.show()

# json_output = result.export()

# print(json_output)

# # Write to a JSON file
# with open("results/doc-tr.json", "w", encoding="utf-8") as f:
#     f.write(json_output)