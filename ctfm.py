#!/usr/bin/env python3

from datetime import datetime
import os
import sys
from argparse import ArgumentParser

CATEGORIES = ["Reverse_Engineering", "Binary_Exploitation",
              "Web_Exploitation", "Cryptography", "General_Skills"
              "Forensics", "Misc"]

def initialize(ctf_name):
    try:
        os.mkdir(ctf_name)
        os.chdir(ctf_name)
        for category in CATEGORIES:
            os.mkdir(category)
        
        date = datetime.now()
        with open("README.md", "w") as readme:
            readme.write(f"# {ctf_name}\n## date : {date}\n")
            readme.close()
    except Exception as err:
        print(f"[!]- Err: {err}")


def save_the_flag(flag):
    with open("flag.txt", "w") as flagf:
        flagf.write(f"{flag}\n")
        flagf.close()
    print("[+] saved in flag.txt")


def start_challenge():
    start_date = datetime.now()
    challenge_name = os.getcwd().split("/")[-1]
    with open("ctf_manager.txt", "w") as status:
        status.write(f"# {challenge_name}\n")
        status.write(f"started : {start_date}\n")
        status.close()
    print(f"[+] challenge started {start_date}")


def finish_challenge():
    finish_date = datetime.now()
    with open("ctf_manager.txt", "a") as status:
        status.write(f"finshed : {finish_date}\n")
        status.close()
    print(f"[+] challenge finished {finish_date}")


ap = ArgumentParser(prog="ctfm")
ap.add_argument("-i", "--initialize", metavar="CTF_NAME",
                help="initialize the requirements")
ap.add_argument("-f", "--flag", 
                help="save the flag in flag.txt")
ap.add_argument("-s", "--start", action="store_true",
                help="start the challenge, build the ctf_manager.txt")
ap.add_argument("-d", "--done", action="store_true", 
                help="finish the challenge")

args = ap.parse_args()

if len(sys.argv) > 1:
    if ctf_name:=args.initialize:
        initialize(ctf_name)
    elif flag:=args.flag:
        save_the_flag(flag)
    elif args.start:
        start_challenge()
    elif args.done:
        finish_challenge()
    else:
        ap.print_help()
else:
    ap.print_help()
