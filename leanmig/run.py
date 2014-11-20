#!/usr/bin/env python3
# encoding: utf-8

from pymongo import MongoClient
from json import dumps
from base import Base

class MongoBase(Base):


    def connect(self):
        return getattr(MongoClient(), 'qudian')

    def get_collection(self, collection):
        return getattr(self._connect, collection)

    def get_objects(self, cursor):
        return cursor.find()

    def _transfer(self, target):
        return dumps(str(target))

if __name__ == '__main__':
    new = MongoBase()
    print(new.transfer())
