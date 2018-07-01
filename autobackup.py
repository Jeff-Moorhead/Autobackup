#! python3

import os
import backup
import argparse
import win32api
import logging

logging.basicConfig(level=logging.NOTSET, format='%(message)s')
# logging.disable(logging.CRITICAL)

documents = "C:\\Users\\Jmoor\\OneDrive\\Documents"
desktop = "C:\\Users\\Jmoor\\OneDrive\\Desktop"
drives = win32api.GetLogicalDriveStrings().split('\\\000')[:-1]
drives.remove('C:')

parser = argparse.ArgumentParser()
parser.add_argument('drives', nargs='*', type=str, choices=drives, help='A backup drive.')
parser.add_argument('-r', '--remove', nargs='?', const=7, type=int, help='Remove old backups. If an integer value is specified, backups at least n days'
	+ ' old will be removed. If no integer is given, the default value of seven days will'
	+ ' be used.')
parser.add_argument('-s', '--shutdown', action='store_true', help='Shutdown when backups finish')
args = parser.parse_args()

for drive in args.drives:
	if not os.path.exists(drive):
		print(f'{drive} not found. Backup failed.')
	else:
		backup.check_for_backups(drive)
		print(f'Backing up to drive {drive}...')
		print('Backing up documents...')
		backup.backup(documents, drive)
		print(f'----------Backup to {drive} complete!-----------')
		if args.remove:
			logging.info(f'Removing backups older than {args.remove} days.')
			backup.remove_old_backups(args.remove, drive)
			
if args.shutdown:
	logging.info('Shutting down...')
	os.system('shutdown /s /t 5')
