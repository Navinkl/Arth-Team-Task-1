import os
import pyttsx3
import getpass
import subprocess as sp

PW = "navin"

while True:
        os.system("tput setaf 7")
        pyttsx3.speak("PLease enter your password to continue.")
        pw = getpass.getpass("\n\t If you want to continue, please enter your password: ")
        if pw == PW:
                os.system("tput setaf 6")
                pyttsx3.speak("Correct Password Stark")
                print("\n\Correct password")
                pyttsx3.speak("Terminal sleeping for 2 seconds")
                os.system("sleep 2")
                break
        else:
                os.system("tput setaf 5")
                pyttsx3.speak("Incorrect password Stark")
                print("\tIncorrect password!\n")

while True:
        def configure_lvm():
        pyttsx3.speak("Welcome to the Linux LVM automation Script")
        print("\t\t\tWelcome to the Linux LVM automation Script")
        print("\t\t\t------------------------------------------")


        print("""
1.Press 1 to get the list of all the disks attached to the system
2.Press 2 to create Physical Volume
3.Press 3 to create Volume Group
4.Press 4 to create Logical Volume
5.Press 5 to increase or decrease the Logical Volume
6.Press 6 to remove the Logical Volume
7.Press 7 to remove the Volume Group
8.Press 8 to remove the Physical Volume
9.Press 9 to format the partition
10.Press 10 to mount the partition
11.Press 11 to get a list of mount targets
12.Press 12 to unmount the partition\n""")


