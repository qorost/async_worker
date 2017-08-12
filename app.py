import argparse
import logging
import os
import re
import sqlite3
import sys
import threading
from datetime import datetime
from distutils.version import StrictVersion
from lazyme.string import color_print

import asyncio

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def cprint(line):
    print('\x1b[6;30;42m' + line + '\x1b[0m')

def redprint(line):
    print('\x1b[6;30;41m' + line + '\x1b[0m')


async def worker_demo(work):
    pass

def async_run(works, worker):
    """
    Running worker asynchrously, with data works.
    Input:
        works: the data array
        worker: the function that perform on data, should be declared with `async def`
    """
    if type(works) == dict:
        tmp = works
        works = []
        for item in tmp:
            works.append(tmp[item])
    if type(works) != list:
        print("Input is an Invalid type")
        return

    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(worker(work)) for work in works]
    loop.run_until_complete(asyncio.wait(tasks))


"""
Functions used to test
"""


"""
api related to user input
"""

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via input() and return their answer.
    refer from http://stackoverflow.com/questions/3041986/apt-command-line-interface-like-yes-no-input
    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        redprint(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Experiments Carrier.")
    #FIXME, improve the clarity
    subparsers = parser.add_subparsers(title="subcommands", \
                                        description="valid subcommands", \
                                        help="sub-command help")
    parser_helper = subparsers.add_parser("help", help="print help information ")
    args = parser.parse_args()








