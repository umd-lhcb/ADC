#!/usr/bin/env python
#
# Last Change: Mon Feb 05, 2018 at 09:10 PM -0500

from logging import getLogger
from datetime import datetime

standard_time_format = "%Y-%m-%d %H:%M:%S.%f"


class DataSource(object):
    def __init__(self, logger_name='queue'):
        self.logger = getLogger(logger_name)

    @staticmethod
    def time_now_formatted():
        return datetime.now().strftime(standard_time_format)

    def get(self):
        # The returned list should contain entries of tuples;
        # each tuple should 3 elements:
        #   (<time>, <channel name>, <measured value>)
        data = [('0', '0', 0)]
        return data
