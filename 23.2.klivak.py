import re
from datetime import datetime
def convert_date_format(string_time):
    if re.match(r'\d{1,2}\.\d{1,2}\.\d{4}', string_time):
        time = datetime.strptime(string_time, '%d.%m.%Y')
    elif re.match(r'\d{4}/\d{1,2}/\d{1,2}', string_time):
        time = datetime.strptime(string_time, '%Y/%m/%d')
    else:
        raise ValueError('Непідтримуваний формат дати')

        return time.strftime('%d.%m.%Y')

time_for_string = "2023/5/15"
new_format = convert_date_format(time_for_string)
print(f"Початкова дата: {time_for_string}")
print(f"Новий формат: {new_format}")
