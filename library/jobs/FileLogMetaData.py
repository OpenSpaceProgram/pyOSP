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

            if (sensor is not False):
                metaData = sensor.getMetaData()

                data = defaultdict(list)
                log = defaultdict(list)
                timestamp = int(time.time())
                data['unit'] = metaData[self.specification[sensorName]].getUnit()
                data['value'] = metaData[self.specification[sensorName]].getValue()
                data['sensor'] = sensorName
                data['metaData'] = self.specification[sensorName]
                log[timestamp] = data

                # Open a file
                fo = open("log.txt", "a")

                #append to file the log data
                fo.write(json.dumps(log) + "\n")

                # Close opend file
                fo.close()