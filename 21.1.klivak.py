import re

def normalize_dates(text):
    date_pattern = re.compile(r'(\d{1,2})[./](\d{1,2})[./](\d{2,4})')

    def replace_date(match):
        day, month, year = match.groups()
        day = day.zfill(2)
        month = month.zfill(2)
        if len(year) == 2:
            year = '20' + year
        return f'{day}.{month}.{year}'

    result = date_pattern.sub(replace_date, text)

    return result

#приклад роботи
text_with_dates = "Сьогодні 15/07/2023, а тиждень тому 8.7.22."
normalized_text = normalize_dates(text_with_dates)
print(normalized_text)
