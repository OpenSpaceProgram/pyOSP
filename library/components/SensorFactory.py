# -*- coding: utf-8 -*-

from collections import defaultdict
import glob
import sys
#add the project folder to pythpath
sys.path.append('../../')


class SensorFactory(object):

    sensorList = defaultdict(list)
    sensorPath = 'library/sensors/'
    sensorNameSpace = 'library.sensors.'

    def __init__(self):
        super(SensorFactory, self).__init__()
        self.getSensorList()

    def getSensorList(self):
        if (len(self.sensorList) == 0):
            for fileName in glob.glob(self.sensorPath + "*.py"):
                if (fileName != self.sensorPath + '__init__.py'):
                    shortName = fileName.replace(self.sensorPath, '').replace('.py', '')
                    module = __import__(self.sensorNameSpace + shortName, globals(), locals(), [shortName])
                    self.sensorList[shortName] = {
                        'fileName': fileName,
                        'module': module
                    }
                    print(shortName)

        return self.sensorList

    def getSensor(self, name):
        if name in self.sensorList.keys():
            #print(name)
            #print(self.sensorList[name])
            class_ = getattr(self.sensorList[name]['module'], name)
            instance = class_()
            return instance
        else:
            print("Sensor not found: " + name)

        return False
