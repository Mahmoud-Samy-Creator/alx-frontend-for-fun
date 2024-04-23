#!/usr/bin/python3
""" 0. Start a script """


from sys import argv, stderr
from os.path import exists

if (len(argv) < 3):
    print("Usage: ./markdown2html.py README.md README.html", file = stderr)
    exit(1)

elif (not exists(f"{argv[1]}")):
    print(f"Missing {argv[1]}", file = stderr)

else:
    exit(0)
