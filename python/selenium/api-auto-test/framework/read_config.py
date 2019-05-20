#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import configparser

# sys.path.append(os.path.dirname(__file__))
# print(sys.path)
# print(os.path.dirname(os.path.abspath('.')))

class ConfigRead(object):

    def get_value(self, section, key):
        config = configparser.ConfigParser()
        root_path = os.path.split(os.path.dirname(__file__))[0]
        file_path = root_path + '/config/config.ini'
        try:
            config.read(file_path)
            return config.get(section, key)
        except Exception as e:
            print('config read fail.', format(e))

config = ConfigRead()
print(config.get_value('host', 'url'))

    