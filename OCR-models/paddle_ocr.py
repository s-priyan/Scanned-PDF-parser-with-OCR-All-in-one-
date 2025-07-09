# Initialize PaddleOCR instance
from paddleocr import PaddleOCR
ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False)

# Run OCR inference on a sample image 
result = ocr.predict(
    input="source/20259004609379.png")

# Visualize the results and save the JSON results
for res in result:
    # print(type(res))
    res.print()
    res.save_to_img("output")
    res.save_to_json("output")