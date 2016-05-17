# -*- coding: utf-8 -*-
from collections import defaultdict


class SensorModule(object):

    metaDataList = defaultdict(list)
    exclusiveFlag = False
    valueRange = defaultdict(list)

    def __init__(self):
        super(SensorModule, self).__init__()

    def addMetaData(self, MetaData):
        self.metaDataList[MetaData.getName()] = MetaData

    def getMetaData(self):
        return self.metaDataList

    def isExclusive(self):
        return self.exclusiveFlag
