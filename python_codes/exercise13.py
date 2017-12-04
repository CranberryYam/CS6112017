import re

file_path = 'emails.txt'
p = re.compile(r"[^\s@\"]+@[^\s@]+\.[a-zA-Z]+", re.IGNORECASE)

with open(file_path, 'r') as myfile:
    data=myfile.read()
    for email in re.findall(p, data):
        print(email)

