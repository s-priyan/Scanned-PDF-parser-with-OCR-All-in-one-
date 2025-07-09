import fitz  # PyMuPDF

# PDF path and output
input_pdf = "source/20259004608180_toc.pdf"
output_pdf = "source/output_20259004608180_toc.pdf"

# Bounding box 
bbox = {
    "left": 24.333333333333332,
    "top": 768.3333333333334,
    "right": 174.66666666666666,
    "bottom": 743.6666666666666
}

# Open PDF
doc = fitz.open(input_pdf)
page = doc[0]  # Page number is 0-indexed

# Convert coordinates: PyMuPDF uses (0, 0) at top-left
page_height = page.rect.height
rect = fitz.Rect(
    bbox["left"],
    page_height - bbox["top"],
    bbox["right"],
    page_height - bbox["bottom"]
)

# Draw rectangle (you can also fill with color if needed)
shape = page.new_shape()
shape.draw_rect(rect)
shape.finish(color=(1, 0, 0), width=1.5)  # Red border, 1.5 pt
shape.commit()

# Save result
doc.save(output_pdf)
doc.close()
