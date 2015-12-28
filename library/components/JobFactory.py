# -*- coding: utf-8 -*-

from collections import defaultdict
import glob
import sys
#add the project folder to pythpath
sys.path.append('../../')


class JobFactory(object):

    jobList = defaultdict(list)
    jobPath = 'library/jobs/'
    jobNameSpace = 'library.jobs.'

    def __init__(self):
        super(JobFactory, self).__init__()
        self.getSensorList()

    def getjobList(self):
        if (len(self.jobList) == 0):
            for fileName in glob.glob(self.jobPath + "*.py"):
                if (fileName != self.jobPath + '__init__.py'):
                    shortName = fileName.replace(self.jobPath, '').replace('.py', '')
                    module = __import__(self.jobNameSpace + shortName, globals(), locals(), [shortName])
                    self.sensorList[shortName] = {
                        'fileName': fileName,
                        'module': module
                    }
                    print(self.sensorList[shortName])

        return self.sensorList

    def getJob(self, name):
        if name in self.sensorList.keys():
            #print(name)
            #print(self.sensorList[name])
            class_ = getattr(self.sensorList[name]['module'], name)
            instance = class_()
            return instance
