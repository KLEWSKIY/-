from docx import Document
from docx.shared import RGBColor
def replace_red_with_blue(input_file, output_file):

    doc = Document(input_file)

    red_color = RGBColor(255, 0, 0)
    blue_color = RGBColor(0, 0, 255)

    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            # Перевірте, чи має поточний елемент червоний колір
            if run.font.color and run.font.color.rgb == red_color:
                # Замініть колір на синій
                run.font.color.rgb = blue_color

        doc.save(output_file)

if __name__ == "__main__":
    input_file = r"C:\need\kchay\Colors Word\MS Word.docx"
    output_file = r"C:\need\kchay\Colors Word\MS WordChange.docx"

    replace_red_with_blue(input_file, output_file)

