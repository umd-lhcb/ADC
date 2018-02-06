#!/usr/bin/env python
#
# Last Change: Mon Feb 05, 2018 at 09:11 PM -0500

try:
    from base import DataSource
except ImportError:
    from bUrn.ADC.base import DataSource

from random import uniform


class DataSourceRNG(DataSource):
    def __init__(self, num_of_ch):
        self.num_of_ch = num_of_ch

        # Call the parent's constructor
        super(DataSourceRNG, self).__init__()

    def get(self):
        data = list()
        for i in range(0, self.num_of_ch):
            num = uniform(0, 10)
            data.append((self.time_now_formatted(), 'ch%s' % i, num))
            self.logger.debug('Current number: %s', num)
        return data
