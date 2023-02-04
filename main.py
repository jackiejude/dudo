#!/usr/bin/env python

import sys
from enum import Enum

# state machines are technically a form of AI ok??
class state_machine(Enum):
    GOOD = 0
    BAD = 1

if len(sys.argv) < 2:
    print("command expected")
    exit()

good_commands = ("whoami")

def ai_execute(command):
    if command in good_commands:
        return command
        state = state_machine['GOOD']
    state = state_machine['BAD']

cached_commands = [
    ("whoami", "root")
]

def ai_cache(command):
    for i in cached_commands:
        if i[0] == command:
            print(i[1])


ai_cache(ai_execute(sys.argv[1]))
