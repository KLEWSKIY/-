import os


def compare_directories(dir1, dir2, output_file):
    with open(output_file, 'w') as output:
        output.write("Список різниці у розмірах файлів:\n\n")

        files1 = set(os.listdir(dir1))
        files2 = set(os.listdir(dir2))

        common_files = files1.intersection(files2)

        for filename in common_files:
            path1 = os.path.join(dir1, filename)
            path2 = os.path.join(dir2, filename)

            size1 = os.path.getsize(path1)
            size2 = os.path.getsize(path2)

            if size1 != size2:
                output.write(f"{filename}:\n")
                output.write(f"  {dir1}: {size1} байт\n")
                output.write(f"  {dir2}: {size2} байт\n\n")


if __name__ == "__main__":
    dir1 = r"C:\need\kchay\Папка1"
    dir2 = r"C:\need\kchay\Папка2"
    output_file = r"C:\need\kchay\Результати.txt"

    compare_directories(dir1, dir2, output_file)
    print(f"Результати порівняння збережено у файлі: {output_file}")
