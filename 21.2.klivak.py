import re

def split_into_sentences(text):
    regex = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s')
    sentences = regex.split(text)

    for i, sentence in enumerate(sentences):
        print(f'Речення {i + 1}: {sentence}')

#приклад як працює
text = "Перше речення. Друге речення. Четверте речення. П'яте речення"
split_into_sentences(text)