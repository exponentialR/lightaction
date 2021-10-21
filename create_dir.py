# from handdata import *
import argparse
import re
import logging
import traceback
import os
import sys


def check_if_postive_int(value):
    _value = int(value)
    if _value <= 0:
        raise argparse.ArgumentTypeError('%s This is an not an int value' % value)
    return _value


parser = argparse.ArgumentParser()
parser.add_argument('-lst', '--actions', nargs='+', help="list of actions, Example --> pick node, wave", required=True)
parser.add_argument("-sbf", "--subfolder_numbers", help="number of subfolders, must be int", required=True,
                    type=check_if_postive_int)
parser.add_argument("-dir", "--pat", help="Parent directory for data, must be in string", required=True, type=str)
args = parser.parse_args()


# global datadir


def create_dir(actions, subfolder_numbers, data_dir):
    # data_dir = 'handdata'
    i = 1
    # w = '_'
    if not os.path.exists(data_dir):
        data_dir = os.path.join(data_dir)

    while os.path.exists(data_dir):
        data_dir = ('{}_%s'.format(args.pat) % i)
        i += 1
        data_dir = os.path.join(data_dir)

    for action in actions:
        for folder in range(subfolder_numbers):
            try:
                os.makedirs(os.path.join(data_dir, action, str(folder)))
            except:
                pass


if __name__ == '__main__':
    create_dir(args.actions, args.subfolder_numbers, args.pat)
