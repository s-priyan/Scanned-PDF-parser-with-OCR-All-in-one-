import fitz
from PIL import Image
from surya.recognition import RecognitionPredictor
from surya.detection import DetectionPredictor

# To get better resolution
zoom_x = 2.0  # horizontal zoom
zoom_y = 2.0  # vertical zoom
mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension


# doc = fitz.open("source/20259004608180_toc.pdf")  # open document
doc = fitz.open("source/20259004609379.pdf")  # open document
for page in doc:  # iterate through the pages
    pix = page.get_pixmap(matrix=mat)
    pix.save("source/20259004609379.png")  # save as PNG
    break

image = Image.open("source/20259004609379.png")           
recognition_predictor = RecognitionPredictor()
detection_predictor = DetectionPredictor()

predictions = recognition_predictor([image], det_predictor=detection_predictor)

for prediction in predictions:
    for texline in prediction.text_lines:
        print(texline.text)
