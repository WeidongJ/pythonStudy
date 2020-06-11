#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
import time
import os


class Logger(object):

    def __init__(self, logger):

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 创建handle写入日志
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        b_path = os.getcwd().split(os.path.sep+'apitest')
        log_path = b_path[0] + '/apitest/logs/'
        log_name = log_path + rq + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger





