# -*- coding: utf-8 -*-

from collections import defaultdict
import glob
import sys
#add the project folder to pythpath
sys.path.append('../../')


class TriggerFactory(object):

    triggerList = defaultdict(list)
    triggerPath = 'library/triggers/'
    triggerNameSpace = 'library.triggers.'

    def __init__(self):
        super(TriggerFactory, self).__init__()
        self.getSensorList()

    def getTriggerList(self):
        if (len(self.triggerList) == 0):
            for fileName in glob.glob(self.triggerPath + "*.py"):
                if (fileName != self.triggerPath + '__init__.py'):
                    shortName = fileName.replace(self.triggerPath, '').replace('.py', '')
                    module = __import__(self.triggerNameSpace + shortName, globals(), locals(), [shortName])
                    self.sensorList[shortName] = {
                        'fileName': fileName,
                        'module': module
                    }
                    print(self.sensorList[shortName])

        return self.sensorList

    def getTrigger(self, name):
        if name in self.sensorList.keys():
            #print(name)
            #print(self.sensorList[name])
            class_ = getattr(self.sensorList[name]['module'], name)
            instance = class_()
            return instance
