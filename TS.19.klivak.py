import os
import time
def create_temp_files(base_directory, num_files):
    for i in range(num_files):
        filename = f"{base_directory}/temp_file{i + 1}.tmp"
        with open(filename, 'w') as file:
            file.write(f"Це тимчасовий файл {i + 1}")

def delete_old_temp_files(base_directory, t2):
    current_time = time.time()
    for filename in os.listdir(base_directory):
        if filename.endswith(".tmp"):
            file_path = os.path.join(base_directory, filename)
            file_mtime = os.path.getmtime(file_path)
            if current_time - file_mtime > t2:
                os.remove(file_path)

if __name__ == "__main__":
    base_directory = r"C:\need\kchay\Tmp"
    t1 = 30
    t2 = 300

    while True:
        create_temp_files(base_directory, 5)
        time.sleep(t1)
        delete_old_temp_files(base_directory, t2)
