#! python3

import os
import zipfile
import datetime
import re


def check_for_backups(folder):
    today = datetime.datetime.today()
    file_regex = re.compile(rf'(\w+)_{today.month}-{today.day}-{today.year}.zip')
    files = filter(lambda file: file_regex.match(file), os.listdir(folder))
    for file in files:
        os.remove(f'{folder}\\{file}')


def backup(src, dest):
    if not os.path.exists(src):
        raise FileNotFoundError(f'{src} is not a valid path.')

    base = os.path.basename(src)
    now = datetime.datetime.now()
    newFile = f'{base}_{now.month}-{now.day}-{now.year}.zip'

    # Set the current working directory.
    os.chdir(dest)

    # Write the zipfile and walk the source directory tree.
    with zipfile.ZipFile(newFile, 'w') as zip:
        for folder, _ , files in os.walk(src):
            for file in files:
                zip.write(os.path.join(folder, file),
                        arcname=os.path.join(
                            folder[len(src):], file),
                        compress_type=zipfile.ZIP_DEFLATED)
                

def remove_old_backups(time, folder):
    file_regex = re.compile(r'(\w+)_(\d+)-(\d+)-(\d+).zip')
    files = list(filter(lambda file: file_regex.match(file), os.listdir(folder)))
    counter = 0
    for file in files:
        date_created = os.path.getctime(f'{folder}\\{file}')
        time_elapsed = datetime.datetime.today() - datetime.datetime.fromtimestamp(date_created)
        if time_elapsed.days >= time:
            try:
                os.remove(f'{folder}\\{file}')
                counter += 1
            except PermissionError:
                print(f'Access denied to {file}!')
