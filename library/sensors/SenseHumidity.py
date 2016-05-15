# -*- coding: utf-8 -*-

import sys
from sense_hat import SenseHat
#add the project folder to pythpath
sys.path.append('../../')

from library.components.SensorModule import SensorModule as Sensor
from library.components.MetaData import MetaData as MetaData


class SenseHumidity(Sensor):

    def __init__(self):
        super(SenseHumidity, self).__init__()
        tempMetaData = MetaData('Humidity')
        tempMetaData.setValueCallback(self.getHumidityValue)
        tempMetaData.setUnitCallback(self.getHumidtyUnit)
        self.addMetaData(tempMetaData)

    def getHumidityValue(self):
        sense = SenseHat()
        return str(sense.humidity)

    def getHumidtyUnit(self):
        return " %"

    def getMetaData(self):
        return super(SenseHumidity, self).getMetaData()