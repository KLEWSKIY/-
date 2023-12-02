import os
from datetime import datetime


def compare_files(dir1, dir2, output_file):
    with open(output_file, 'w') as result_file:
        result_file.write("Порівняння файлів в {} і {}\n\n".format(dir1, dir2))

        for root, dirs, files in os.walk(dir1):
            for file in files:
                file_path1 = os.path.join(root, file)
                file_path2 = os.path.join(dir2, os.path.relpath(file_path1, dir1))

                if os.path.exists(file_path2):
                    time1 = os.path.getctime(file_path1)
                    time2 = os.path.getctime(file_path2)

                    if time1 != time2:
                        datetime1 = datetime.fromtimestamp(time1)
                        datetime2 = datetime.fromtimestamp(time2)

                        result_file.write("File: {}\n".format(file))
                        result_file.write("  {} - {}\n".format(dir1, datetime1))
                        result_file.write("  {} - {}\n\n".format(dir2, datetime2))


if __name__ == "__main__":
    dir1 = r"C:\need\kchay\ПапкаOne"
    dir2 = r"C:\need\kchay\ПапкаTwo"
    output_file = r"C:\need\kchay\Файл.txt"

    compare_files(dir1, dir2, output_file)
    print("Порівняння завершено. Результати збережено в {}".format(output_file))
