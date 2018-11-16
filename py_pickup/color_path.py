# coding=utf-8

import os


def get_path(color):
    home = os.environ['HOME']
    dir_path = home + '/worktree/'
    # color = {
    #     'red': dir_path + 'red.xml',
    #     'blue': dir_path + 'blue.xml',
    #     'yellow': dir_path + 'yellow.xml',
    #     'redball': dir_path + 'redball.xml'
    # }
    return dir_path + color + '.xml'
