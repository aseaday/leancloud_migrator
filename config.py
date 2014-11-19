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
        if not os.path.isfile('config.yaml'):
            raise('Error Configure File')
        self._config = 'config.yaml'
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
