"""
Automatically backup any folder to a zip file using backup.py.
Differs from autobackup.pyw in that this version is designed to run
with Windows Task Scheduler so that it doesn't have to be constantly
running in the background.
"""

import os
import sys
from time import sleep
from backup import backup

documents = "C:\\Users\\Jmoor\\OneDrive\\Documents"
desktop = "C:\\Users\\Jmoor\\OneDrive\\Desktop"
drive1 = sys.argv[1]
drive2 = sys.argv[2]
# Check if computer should shut down after backups.
shutdown = input('Shut down after backups (y/n)? ')

# If neither backup drive exists, shutdown the computer.
if not (os.path.exists(drive1 + '\\') or os.path.exists(drive2 + '\\')):
	print("---------- Backup failed: Drives not available! ----------")
	sleep(3)
	sys.exit(1)
else:
	# Perform backups.
	if os.path.exists(f'{drive1}\\'):
		backup(desktop, f'{drive1}\\')
		backup(documents, f'{drive1}\\')
		#backup("C:\\Users\\Jeff Moorhead\\Pictures", "E:\\")
		
	if os.path.exists(f'{drive2}\\'):
		backup(desktop, f'{drive2}\\')
		backup(documents, f'{drive2}\\')
		#backup("C:\\Users\\Jeff Moorhead\\Pictures", "F:\\")

if shutdown == 'y':
        os.system('shutdown /s /t 3')
else:
        sleep(3)
        sys.exit(0)
