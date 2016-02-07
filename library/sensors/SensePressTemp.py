# -*- coding: utf-8 -*-

import sys
from sense_hat import SenseHat
#add the project folder to pythpath
sys.path.append('../../')

from library.components.SensorModule import SensorModule as Sensor
from library.components.MetaData import MetaData as MetaData


class SensePressTemp(Sensor):

    def __init__(self):
        super(SensePressTemp, self).__init__()
        tempMetaData = MetaData('Centigrade')
        tempMetaData.setValueCallback(self.getTempValue)
        tempMetaData.setUnitCallback(self.getTempUnit)
        self.addMetaData(tempMetaData)

    def getTempValue(self):
        sense = SenseHat()
        temp = sense.get_temperature_from_pressure()
        return str(temp)

    def getTempUnit(self):
        return " Centigrade"

    def getMetaData(self):
        return super(SensePressTemp, self).getMetaData()