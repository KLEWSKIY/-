import re
from datetime import datetime

def replace_underscores_with_current_date(text):
    # Знайти всі дати у тексті
    dates = re.findall(r'\d{2}\.\d{2}\.\d{4}|__\.____', text)

    # Замінити підкреслення на поточну дату
    current_date = datetime.now().strftime('%d.%m.%Y')
    updated_text = re.sub(r'__\.____', current_date, text)

    return updated_text

# Шлях до вхідного та вихідного файлів
input_file_path = 'C:/need/kchay/Дати.txt'
output_file_path = 'C:/need/kchay/Нові дати.txt'

with open(input_file_path, 'r', encoding='utf-8') as file:
    content = file.read()

updated_content = replace_underscores_with_current_date(content)

with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(updated_content)

print(f'Оновлений текст збережено у файлі: {output_file_path}')


