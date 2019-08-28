# Autobackup
I have always found commercial backup systems to be overly cumbersome. In my experience, if my computer crashes, all I really need to recover are my files. I find that software recovered from a disk image seldom works the way it did before the crash. However, I have never come across a system that allows you to back up only _select_ folders. Sure, it is a straightforward exercise to simply copy whatever files you want backed up onto an external harddrive, but there is no automation in that procedure. My solution: use my knowledge of software development and Python to automate the backup process. This simple project allows the user to specify which drive to backup, and then automatically takes all folders from that drive and stores it on the backup drive specified by the user. Further, it is possible to run this application off of the Windows task scheduler so that it will back up your files even when you're away from your computer.  
</br></br>
This system currently only supports Windows file system, but I would like to expand it to include Unix-based systems as well. I feel that the simplicity of the interface and the customization options make this tool very useful to the average computer user who just doesn't need to restore their full operating system in the event of a crash.
