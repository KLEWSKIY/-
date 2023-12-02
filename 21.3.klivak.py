import re


def roman_to_int(roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    prev_value = 0

    for num in reversed(roman):
        val = roman_numerals[num]
        if val < prev_value:
            res -= val
        else:
            res += val

        prev_value = val
    return res


def validate_roman_numeral(roman):
    pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    return re.match(pattern, roman) is not None


def find_and_validate_roman_numerals(text):
    roman_numerals = re.findall(r'\b[IVXLCDM]+\b', text)

    valid_numerals = [numeral for numeral in roman_numerals if validate_roman_numeral(numeral)]

    return valid_numerals

text = "Текст із римськими числами: MCMLXXXIV, XVII, ABC, XI, IVX"
valid_numerals = find_and_validate_roman_numerals(text)

print("Знайдені та валідні римські числа:", valid_numerals)

for numeral in valid_numerals:
    arabic_equivalent = roman_to_int(numeral)
    print(f"Римське число {numeral} має арабський еквівалент: {arabic_equivalent}")
