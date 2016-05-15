# -*- coding: utf-8 -*-

import sys
from sense_hat import SenseHat
#add the project folder to pythpath
sys.path.append('../../')

from library.components.SensorModule import SensorModule as Sensor
from library.components.MetaData import MetaData as MetaData


class SensePressure(Sensor):

    def __init__(self):
        super(SensePressure, self).__init__()
        tempMetaData = MetaData('millibars')
        tempMetaData.setValueCallback(self.getPressureValue)
        tempMetaData.setUnitCallback(self.getPressureUnit)
        self.addMetaData(tempMetaData)

    def getPressureValue(self):
        sense = SenseHat()
        return str(sense.pressure)

    def getPressureUnit(self):
        return " Millibars"

    def getMetaData(self):
        return super(SensePressure, self).getMetaData()