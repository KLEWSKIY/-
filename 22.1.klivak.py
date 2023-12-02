import os

def compare_directories(dir1, dir2, output_file):
    files_set1 = set(os.listdir(dir1))
    files_set2 = set(os.listdir(dir2))

    unique_to_dir1 = files_set1 - files_set2
    unique_to_dir2 = files_set2 - files_set1

    with open(output_file, 'w') as f:
        f.write(f'Файли присутні в {dir1} але не в {dir2}:\n')
        for file in unique_to_dir1:
            f.write(f'{file}\n')

        f.write(f'\nФайли присутні в {dir2} але не в {dir1}:\n')
        for file in unique_to_dir2:
            f.write(f'{file}\n')

if __name__ == "__main__":
    directory1 = r'C:\need\kchay\КаталогOne'
    directory2 = r'C:\need\kchay\КаталогTwo'

    output_file_path = r'C:\need\kchay\Різниця.txt'

    compare_directories(directory1, directory2, output_file_path)
    print(f'Різницю збережено в файлі: {output_file_path}')
