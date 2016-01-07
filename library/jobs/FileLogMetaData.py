# -*- coding: utf-8 -*-

import sys
from library.components.SensorFactory import SensorFactory as SensorFactory
from library.components.JobModule import JobModule as Job
from collections import defaultdict
import time
import json
#add the project folder to pythpath
sys.path.append('../../')



class FileLogMetaData(Job):

    def __init__(self, specification):
        super(FileLogMetaData, self).__init__(specification)

    def run(self):
        senseFact = SensorFactory()
        for sensorName in self.specification:
            sensor = senseFact.getSensor(sensorName)
            metaData = sensor.getMetaData()

            #print(sensorName + "::" + metaData[self.specification[sensorName]].getName() + " reading: ")
            #print(metaData[self.specification[sensorName]].getValue() + " "+ metaData[self.specification[sensorName]].getUnit())
            data = defaultdict(list)
            log = defaultdict(list)
            timestamp = str(time.time())
            data['unit'] = metaData[self.specification[sensorName]].getUnit()
            data['value'] = metaData[self.specification[sensorName]].getValue()
            log[timestamp] = data
            print(json.dumps(log))
            #append to file the log data