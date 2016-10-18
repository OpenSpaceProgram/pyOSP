# -*- coding: utf-8 -*-

import sys
import time
from subprocess import call
#add the project folder to pythpath
sys.path.append('../../')

from library.components.SensorModule import SensorModule as Sensor
from library.components.MetaData import MetaData as MetaData


class Raspistill(Sensor):

    def __init__(self):
        super(Raspistill, self).__init__()
        # ISO100
        iso200MetaData = MetaData('ISO100')
        iso200MetaData.setValueCallback(self.getIso100)
        iso200MetaData.setUnitCallback(self.getUnit)
        self.addMetaData(iso200MetaData)

        # ISO200
        iso200MetaData = MetaData('ISO200')
        iso200MetaData.setValueCallback(self.getIso200)
        iso200MetaData.setUnitCallback(self.getUnit)
        self.addMetaData(iso200MetaData)

        # ISO400'
        iso200MetaData = MetaData('ISO400')
        iso200MetaData.setValueCallback(self.getIso400)
        iso200MetaData.setUnitCallback(self.getUnit)
        self.addMetaData(iso200MetaData)

        # ISO800'
        iso200MetaData = MetaData('ISO800')
        iso200MetaData.setValueCallback(self.getIso800)
        iso200MetaData.setUnitCallback(self.getUnit)
        self.addMetaData(iso200MetaData)

    def getIso100(self):
        filename = "photos/" + str(time.time()) + "-iso100.jpg"
        call(["raspistill", "--ISO", "100", "-o", filename])
        return str(filename)

    def getIso200(self):
        filename = "photos/" + str(time.time()) + "-iso200.jpg"
        call(["raspistill", "--ISO", "200", "-o", filename])
        return str(filename)

    def getIso400(self):
        filename = "photos/" + str(time.time()) + "-iso400.jpg"
        call(["raspistill", "--ISO", "400", "-o", filename])
        return str(filename)

    def getIso800(self):
        filename = "photos/" + str(time.time()) + "-iso800.jpg"
        call(["raspistill", "--ISO", "800", "-o", filename])
        return str(filename)

    def getUnit(self):
        return " Photo"

    def getMetaData(self):
        return super(Raspistill, self).getMetaData()