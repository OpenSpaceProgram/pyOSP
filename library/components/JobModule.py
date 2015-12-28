# -*- coding: utf-8 -*-
from collections import defaultdict


class JobModule(object):

    specification = defaultdict(list)
    #binaryDataList = list

    def __init__(self, specification):
        super(JobModule, self).__init__()
        self.specification = specification

    def run(self):
        return