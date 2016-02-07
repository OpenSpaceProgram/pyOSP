# -*- coding: utf-8 -*-

import sys
from sense_hat import SenseHat
#add the project folder to pythpath
sys.path.append('../../')

from library.components.SensorModule import SensorModule as Sensor
from library.components.MetaData import MetaData as MetaData


class SenseTemp(Sensor):

    def __init__(self):
        super(SenseTemp, self).__init__()
        tempMetaData = MetaData('Centigrade')
        tempMetaData.setValueCallback(self.getTempValue)
        tempMetaData.setUnitCallback(self.getTempUnit)
        self.addMetaData(tempMetaData)

    def getTempValue(self):
        sense = SenseHat()
        temp = sense.get_temperature()
        return str(temp)

    def getTempUnit(self):
        return " Centigrade"

    def getMetaData(self):
        return super(SenseTemp, self).getMetaData()