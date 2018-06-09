"""
Backup my files.
"""

import os
import zipfile
import datetime


def backup(src, dest):
    """Backup files from src to dest."""
    base = os.path.basename(src)
    now = datetime.datetime.now()
    newFile = f'{base}_{now.month}-{now.day}-{now.year}.zip'

    # Set the current working directory.
    os.chdir(dest)

    if os.path.exists(newFile):
        os.unlink(newFile)
        newFile = f'{base}_{now.month}-{now.day}-{now.year}_OVERWRITE.zip'

    # Write the zipfile and walk the source directory tree.
    with zipfile.ZipFile(newFile, 'w') as zip:
        for folder, _ , files in os.walk(src):
            print(f'Working in folder {os.path.basename(folder)}')

            for file in files:
                zip.write(os.path.join(folder, file),
                          arcname=os.path.join(
                              folder[len(src):], file),
                          compress_type=zipfile.ZIP_DEFLATED)
        print(
            f'\n---------- Backup of {base} to {dest} successful! ----------\n')


if __name__ == '__main__':
    # The destination folder.
    destination = input('Backup to which drive? ')

    # The source folder.
    source = input('Backup which folder? ')

    shutdown = input('Shutdown after backup (y/n)? ')
    if shutdown == shutdown.lower() == 'y':
        print('The computer will shut down 10 seconds after backup.')

    print('Starting backup...')

    backup(source, destination)

    if shutdown.lower == 'y':
        os.system('shutdown /s /t 10')
