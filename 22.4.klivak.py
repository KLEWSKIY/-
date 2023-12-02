import os
import tarfile
from datetime import datetime, timedelta
def archive_logs(log_directory, days_ago, output_directory):
    current_date = datetime.now()
    target_date = current_date - timedelta(days=days_ago)
    log_file_pattern = current_date.strftime("%Y-%m-%d") + "-"
    archive_filename = f"{output_directory}/logs_archive_{current_date.strftime('%Y%m%d%H%M%S')}.tar.gz"
    with tarfile.open(archive_filename, "w:gz") as archive:
        for filename in os.listdir(log_directory):
            if filename.startswith(log_file_pattern):
                file_path = os.path.join(log_directory, filename)

                if os.path.getctime(file_path) < target_date.timestamp():
                    archive.add(file_path, arcname=filename)

    print(f"Архівування завершено: {archive_filename}")

log_directory = r"C:\need\kchay\Archive"
days_ago = 7
output_directory = r"C:\need\kchay\Log"

archive_logs(log_directory, days_ago, output_directory)
