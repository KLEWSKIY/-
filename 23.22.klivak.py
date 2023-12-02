import openpyxl
class ExcelIterator:
    def __init__(self, file_path, sheet_name):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.headers = None
        self.current_row = 2
        self.load_data()

    def load_data(self):
        wb = openpyxl.load_workbook(self.file_path)
        sheet = wb[self.sheet_name]
        self.headers = [cell.value for cell in sheet[1]]
        self.data_rows = list(sheet.iter_rows(min_row=2, values_only=True))

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_row == len(self.data_rows) + 2:
            raise StopIteration

        row_data = self.data_rows[self.current_row - 2]
        self.current_row += 1

        row_dict = dict(zip(self.headers, row_data))
        return row_dict

    def get_headers(self):
        return self.headers

file_path = r"C:\need\kchay\Papka\ExcelP.xlsx"
sheet_name = "Табличка"

excel_iterator = ExcelIterator(file_path, sheet_name)

headers = excel_iterator.get_headers()
print("Заголовки стовпчиків:", headers)

for row_data in excel_iterator:
    print(row_data)

