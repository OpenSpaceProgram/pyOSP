# -*- coding: utf-8 -*-

import sys
from library.components.SensorFactory import SensorFactory as SensorFactory
from library.components.JobModule import JobModule as Job
from collections import defaultdict
import requests

#add the project folder to pythpath
sys.path.append('../../')



class SyncData(Job):

    def __init__(self, specification):
        super(SyncData, self).__init__(specification)

    def run(self):
        senseFact = SensorFactory()
        data = defaultdict(list)

        for sensorName in self.specification:
            sensor = senseFact.getSensor(sensorName)

            if (sensor is not False):
                metaData = sensor.getMetaData()
                data[self.specification[sensorName]] = metaData[self.specification[sensorName]].getValue()

        r = requests.post("http://192.168.1.3/post", data=data)

        print(r.status_code)