import easyocr


reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
result = reader.readtext("source/20259004609379.png")

for text in result:
    print(text[1])  # text[1] contains the recognized text