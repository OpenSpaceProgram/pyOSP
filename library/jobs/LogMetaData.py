# -*- coding: utf-8 -*-

import sys
from library.components.SensorFactory import SensorFactory as SensorFactory
from library.components.JobModule import JobModule as Job
#add the project folder to pythpath
sys.path.append('../../')



class LogMetaData(Job):

    def __init__(self, specification):
        super(LogMetaData, self).__init__(specification)

    def run(self):
        print('::Logging MetaData')
        senseFact = SensorFactory()
        for sensorName in self.specification:
            print("Get sensor: " + sensorName)
            sensor = senseFact.getSensor(sensorName)
            metaData = sensor.getMetaData()
            print(sensorName + "::" + metaData[self.specification[sensorName]].getName() + " reading: ")
            print(metaData[self.specification[sensorName]].getValue() + " "+ metaData[self.specification[sensorName]].getUnit())
