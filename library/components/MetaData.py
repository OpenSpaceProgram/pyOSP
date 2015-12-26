# -*- coding: utf-8 -*-


class MetaData(object):

    name = None

    def __init__(self, name):
        super(MetaData, self).__init__()
        self.name = name

    def setValueCallback(self, valueCallback):
        self.valueCallback = valueCallback

    def getValue(self):
        return self.valueCallback()

    def getName(self):
        return self.name

    def setUnitCallback(self, unitCallback):
        self.unitCallback = unitCallback

    def getUnit(self):
        return self.unitCallback()