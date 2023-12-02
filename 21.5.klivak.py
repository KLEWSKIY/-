import re
from datetime import datetime


def normalize_date(match):
    groups = match.groupdict()

    if groups['day']:
        return f"{groups['year']}-{groups['month']}-{groups['day']}"
    else:
        return f"{groups['year']}-{groups['month']}"


def normalize_dates_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    date_patterns = [
        r'(?P<day>\d{2})\.(?P<month>\d{2})\.(?P<year>\d{4})',
        r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',
        r'(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})'
    ]

    for pattern in date_patterns:
        content = re.sub(pattern, normalize_date, content)

    with open(file_path, 'w') as file:
        file.write(content)

    print(f"Дати у файлі {file_path} були нормалізовані.")

file_path = 'C:/need\kchay\Ще нові дати\Дати 2.0.txt'
normalize_dates_in_file(file_path)



