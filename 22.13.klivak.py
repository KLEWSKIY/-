import os
import glob
def merge_files(input_dir, output_file):
    files = glob.glob(os.path.join(input_dir, '*.txt'))
    files.sort(key=os.path.getctime)

    with open(output_file, 'w', encoding='utf-8') as output:
        for file in files:
            with open(file, 'r', encoding='utf-8') as input_file:
                output.write(input_file.read())
                output.write('\n')

    print(f"Файли успішно об'єднані у {output_file}")

input_directory = r'C:\need\kchay\ПапкаX'
output_file = r'C:\need\kchay\Файл.txt'
merge_files(input_directory, output_file)
