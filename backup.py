"""
Backup my files.
"""

import os
import zipfile


def backup(src, dest):
    """Backup files from src to dest."""
    base = os.path.basename(src)

    # Set the current working directory.
    os.chdir(dest)

    # If the zip file already exists, delete the old one.
    if os.path.exists(f'{base}.zip'):
        os.unlink(f'{base}.zip')

    # Write the zipfile and walk the source directory tree.
    with zipfile.ZipFile(f'{base}.zip', 'w') as zip:
        for folder, subfolders, files in os.walk(src):
            print(f'Working in folder {os.path.basename(folder)}')
            for file in files:
                zip.write(os.path.join(folder, file),
                          compress_type=zipfile.ZIP_DEFLATED)
        print(f'\n---------- Backup of {base} to {dest} successful! ----------\n')


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
