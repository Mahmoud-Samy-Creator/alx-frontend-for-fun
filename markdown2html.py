#!/usr/bin/python3
""" 0. Start a script """


from sys import argv, stderr, exit
from os.path import exists
from markdown import markdown

errMessage = "Usage: ./markdown2html.py README.md README.html"

if __name__ == "__main__":
    if (len(argv) < 3):
        print(f"{errMessage}", file=stderr)
        exit(1)

    elif (not exists(f"{argv[1]}")):
        print(f"Missing {argv[1]}", file=stderr)
        exit(1)

    else:
        with open(f"{argv[1]}", "r") as file:
            content = file.read()
            html_rep = markdown(content)

        with open(f"{argv[2]}", "w") as file:
            file.write(html_rep)
        exit(0)
