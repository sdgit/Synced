#!/usr/bin/env python

# Synced - A personal media oranizer, storage and backup suite

import sys
import argparse

import synced
import util.logger as logger

def parse_args(args):
    parser = argparse.ArgumentParser(description="Synced")
    parser.add_argument('-v','--version', action='version', version='Synced v'+str(synced.version()))
    parser.add_argument('Program', help='This Program')
    args = parser.parse_args(args)

def main(args):
    parse_args(args)
    if sys.version_info < (2, 7):
        sys.exit("Sorry, requires Python 2.7.")
    synced.initialize(True)


    logger.log("End of main", logger.DEBUG)

if __name__ == '__main__':
    main(sys.argv)

