# -*- coding: utf-8 -*-
from collections import defaultdict


class TriggerModule(object):

    metaDataList = defaultdict(list)
    #binaryDataList = list
    exclusiveFlag = False
    valueRange = defaultdict(list)

    def __init__(self):
        super(TriggerModule, self).__init__()

    def addMetaData(self, MetaData):
        self.metaDataList[MetaData.getName()] = MetaData

    def getMetaData(self):
        return self.metaDataList

    def isExclusive(self):
        return self.exclusiveFlag
