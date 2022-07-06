# Week1:Using Python to Interact with the Operating System
print("Week1: Example 1")

#!C:\Users\levil\AppData\Local\Programs\Python\Python310 python
##!/usr/bin/env python3
from network import *
import shutil
import psutil
def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75
# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity():
    print("Everything ok")
else:
    print("Network checks failed")

print("Week1: Example 2")
#!C:\Users\levil\AppData\Local\Programs\Python\Python310 python
##!/usr/bin/env python3
import requests
import socket

def check_localhost():
  localhost = socket.gethostbyname('localhost')
  if localhost == "127.0.0.1":
    return True
  else:
    return False

def check_connectivity():
  request = requests.get("http://www.google.com")
  if request.status_code == 200:
    return True
  else:
    return False
#Week2:Using Python to Interact with the Operating System
print("Week2: Example 1")
with open("The Black Cat.txt") as file:
    for line in file:
        print(line.strip().upper())

print("Week2: Example 2")
file = open("The Black Cat.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)

print("Week2: Example 3")
with open("The Black Cat(1).txt", "w") as file:
    file.write("It was a dark and stormy night")

print("Week2: Example 4: C2M2L1_Reading_And_Writing_Files")
guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")
guests.close()

with open("guests.txt") as guests:
    for line in guests:
        print(line)
        
new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

with open("guests.txt") as guests:
    for line in guests:
        print(line)
        
checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

guests.close()

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")
        
with open("guests.txt") as guests:
    for line in guests:
        print(line)

guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))

print("Week2: Example 5")
import os
  os.remove("novel.txt")
  os.rename("first_draft.txt", "finished_masterpiece.txt")
  os.path.exists("finished_masterpiece.txt")
  os.path.exists("userlist.txt")
  