"""
Automatically backup any folder to a zip file using backup.py.
Differs from autobackup.pyw in that this version is designed to run
with Windows Task Scheduler so that it doesn't have to be constantly
running in the background.
"""

import os
from sys import exit
from time import sleep
from backup import backup

# Check if computer should shut down after backups.
shutdown = input('Shut down after backups (y/n)? ')

# If neither backup drive exists, shutdown the computer.
if not (os.path.exists("F:\\") or os.path.exists("E:\\")):
	print("---------- Backup failed: Drives not available! ----------")
	sleep(10)
else:
	# Perform backups.
	if os.path.exists("E:\\"):
		backup("C:\\Users\\Jmoor\\Desktop", "E:\\")
		backup("C:\\Users\\Jmoor\\OneDrive\\Documents", "E:\\")
		#backup("C:\\Users\\Jeff Moorhead\\Pictures", "E:\\")
		
	if os.path.exists("F:\\"):
		backup("C:\\Users\\Jmoor\\Desktop", "F:\\")
		backup("C:\\Users\\Jmoor\\OneDrive\\Documents", "F:\\")
		#backup("C:\\Users\\Jeff Moorhead\\Pictures", "F:\\")

if shutdown == 'y':
        os.system('shutdown /s /t 10')
else:
        sleep(10)
        exit()
