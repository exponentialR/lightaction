# from handdata import *
import argparse

import os
import json
from pathlib import Path


def check_if_postive_int(value):
    """Wherever this function is called it checks if the input value is a positive number"""
    _value = int(value)
    if _value <= 0:
        raise argparse.ArgumentTypeError('%s This is an not an int value' % value)
    return _value


parser = argparse.ArgumentParser()
parser.add_argument('-lst', '--actions', nargs='+', help="list of actions, Example --> pick node, wave", required=True)
parser.add_argument("-sbf", "--subfolder_numbers", help="number of subfolders, must be int", required=True,
                    type=check_if_postive_int)
parser.add_argument("-dir", "--pat", help="Parent directory for data, must be in string", required=True, type=str)
parser.add_argument("-len", "--video_length", help='The length of the video in frames', required=True,
                    type=check_if_postive_int)
args = parser.parse_args()


def create_dir(actions, subfolder_numbers, data_dir):
    """This function creates the data folder and corresponding subfolders,
    as defined by you on the command line. You can have as many data instances and subfolders as possible
    The file write logic on the last few lines overwrites the .iams file everytime you run this code
    which is correspondingly used in collect_data_iams.py. This function also """

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
        for folder in range(subfolder_numbers):  # Comment this code not to create subfolders
            try:
                os.makedirs(os.path.join(data_dir, action, str(folder)))
            except:
                pass
            finally:
                iams_dict = {'actions': args.actions, 'subfolder_length': args.subfolder_numbers,
                             'video_length': args.video_length, 'Data_Directory': data_dir,
                             'Data_Subfolder': str(Path("{}/data".format(args.pat)))}
                w = 'iamsMediapipe.iams'
                if not os.path.exists(w):
                    w = os.path.join(w)
                    f = open(w, 'w')
                    json.dump(iams_dict, f)
                    f.close()
                os.path.exists(w)
                f = open(w, 'r+')
                f.seek(0)
                json.dump(iams_dict, f)
                f.truncate()
                f.close()

    absolute_iams_path = os.path.abspath(data_dir)

    print('Your data directory is {}'.format(absolute_iams_path))
    print('Your data is saved in {}'.format(data_dir))
    print('Defined list of actions are: {}'.format(args.actions))
    print('Your video will run for {} seconds at every collection'.format(args.video_length))


if __name__ == '__main__':
    create_dir(args.actions, args.subfolder_numbers, args.pat)
