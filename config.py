#!/usr/bin/env python
# encoding: utf-8

'''
@author: aseaday
@updated: 2014-11-16
'''

from __future__ import print_function, with_statement, division, absolute_import
import yaml
import os
import sys

option = None

class Config(object):
    def __init__(self, *args, **kwargs):
        global option
        if not os.path.isfile(option.configure):
            raise('Error Configure File')
        self._config = option.configure
        super(Config, self).__init__(*args, **kwargs)

    def load(self):
        if not self.checkcode(self._config):
            exit(0)
        stream = open(self._config)
        result = yaml.load(stream)
        print(result)

    def checkcode(cls, file):
        '''
        who can realize a quick code check not a stupid package charset
        '''
        return True


if __name__ == '__main__':
    try:
        from optparse import OptionParser
    except ImportError as e:
        raise e
    parser = OptionParser()
    parser.add_option("-c", "--config", action="store", dest="configure", metavar="FILE")
    (option, arg) = parser.parse_args()
    Config().load()
