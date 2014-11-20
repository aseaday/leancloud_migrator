#!/usr/bin/env python3
# encoding: utf-8

'''
@author: aseaday
@updated: 2014-11-15
TODO: write a non-blocked version
'''

from __future__ import division, with_statement, print_function
from config import Config

class Base(object):
    def __init__(self, *args, **kwargs):
        try:
            self._config = Config().load()
            print(self._config)
            self.with_connect(*args, **kwargs)
        except Exception:
            raise

    def with_connect(self, *args, **kwargs):
        try:
            self._connect = self.connect(*args, **kwargs)
        except Exception:
            raise('Connect Error')

    def connect(self, *args, **kwargs):
        '''
        @Override
        you should return a datebase cursor here
        '''
        raise NotImplementedError()

    def get_collection(self, collection):
        '''
        return _connect.cursor.collection
        '''
        raise NotImplementedError()

    def get_objects(self, cursor):
        '''
        return a iterator of objects
        '''
        raise NotImplementedError()

    def _transfer(self, target):
        '''
        return a json object from the cursor's object
        '''
        raise NotImplementedError()

    def objects(self, collection):
        cursor = self.get_collection(collection)
        return self.get_objects(cursor)

    def transfer(self):
        self.llist = {}
        collections = self._config.get('collections')
        for collection in collections:
            name = collection.get('name')
            self.llist[name] = []
            for aobject in self.objects(name):
                self.llist[name].append(self._transfer(aobject))
        return self.llist
