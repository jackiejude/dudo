#!/usr/bin/env python

import sys

if len(sys.argv) < 2:
    print("command expected")
    exit()

good_commands = ("whoami")

def ai_execute(command):
    if command in good_commands:
        return command

cached_commands = [
    ("whoami", "root")
]

def ai_cache(command):
    for i in cached_commands:
        if i[0] == command:
            print(i[1])


ai_cache(ai_execute(sys.argv[1]))
