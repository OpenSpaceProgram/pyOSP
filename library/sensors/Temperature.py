# -*- coding: utf-8 -*-

import sys
from random import randint
#add the project folder to pythpath
sys.path.append('../../')

from library.components.SensorModule import SensorModule as Sensor
from library.components.MetaData import MetaData as MetaData


class Temperature(Sensor):

    def __init__(self):
        super(Temperature, self).__init__()
        tempMetaData = MetaData('Centigrade')
        tempMetaData.setValueCallback(self.getTempValue)
        tempMetaData.setUnitCallback(self.getTempUnit)
        self.addMetaData(tempMetaData)

    def getTempValue(self):
        return str(randint(-7, 40))

    def getTempUnit(self):
        return " Centigrade"

    def getMetaData(self):
        return super(Temperature, self).getMetaData()