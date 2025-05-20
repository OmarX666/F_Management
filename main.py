import os
import re
import platform
import datetime

print('Get current working directory : ', os.getcwd())

source = input("Enter Your Source Path: ").strip()
target = input("Enter Your Target Path: ").strip()

EXTS = ["jpg", "png", "jpeg", "mov", "mp4"] # Video & Photo Extensions
DATE_PATTERN = r'.*(20\d\d)-?([01]\d)-?([0123]\d).*'

files = os.listdir(source) 

def creation_date(path_to_file):
    # Try to get the date that a file was created, falling back to when it was
    # last modified if that isn't possible.
    if platform.system() == 'Windows':
        timestamp = os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            timestamp = stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            timestamp = stat.st_mtime
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def get_date(folder, file):
    matchObj = re.match(DATE_PATTERN, file)
    if matchObj:
        year = matchObj.group(1)
        month = matchObj.group(2)
        print(year, month)
    else:
        dateCreated = creation_date(folder + f"/{file}")
        matchObj = re.match(DATE_PATTERN, dateCreated)
        year = matchObj.group(1)
        month = matchObj.group(2)
        print(year, month)


for i in files:
    if i.lower().endswith(tuple(EXTS)):
        get_date(source, i)
        print(i)
