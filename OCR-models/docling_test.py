# from docling.document_converter import DocumentConverter


# source = "source/20259004609379.pdf"  # document per local path or URL
# converter = DocumentConverter()
# result = converter.convert(source)
# markdown_text = result.document.export_to_markdown()

# # Write to a text file
# with open("results/docling.md", "w", encoding="utf-8") as f:
#     f.write(markdown_text)

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    PdfPipelineOptions,
    TesseractOcrOptions,
    TesseractCliOcrOptions,
    EasyOcrOptions,
)
from docling.document_converter import DocumentConverter, PdfFormatOption

file_name = '03-415920_Chapter 04_Footnote not linked'

input_doc_path = f"edge-case-sources/{file_name}.pdf" 

pipeline_options = PdfPipelineOptions()
pipeline_options.do_ocr = True
pipeline_options.do_table_structure = True
pipeline_options.table_structure_options.do_cell_matching = True

# Any of the OCR options can be used:EasyOcrOptions, TesseractOcrOptions, TesseractCliOcrOptions, OcrMacOptions(Mac only), RapidOcrOptions
ocr_options = EasyOcrOptions(force_full_page_ocr=True)
# ocr_options = TesseractOcrOptions(force_full_page_ocr=True)
# ocr_options = OcrMacOptions(force_full_page_ocr=True)
# ocr_options = RapidOcrOptions(force_full_page_ocr=True)
# ocr_options = TesseractCliOcrOptions(force_full_page_ocr=True)
# ocr_options = EasyOcrOptions(force_full_page_ocr=True)
pipeline_options.ocr_options = ocr_options

converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(
            pipeline_options=pipeline_options,
        )
    }
)

doc = converter.convert(input_doc_path).document


md = doc.export_to_markdown()


# return the bounding box objects
# items = doc.texts
# for item in items[:5]:
#     print(item.text)
#     print(item.prov)

# Write to a text file
with open(f"edge-case-results-docling/{file_name}.md", "w", encoding="utf-8") as f:
    f.write(md)
        