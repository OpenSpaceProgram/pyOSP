# -*- coding: utf-8 -*-

from collections import defaultdict
from library.components.JobModule import JobModule as Job
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
        self.getJobList()

    def getJobList(self):
        if (len(self.jobList) == 0):
            for fileName in glob.glob(self.jobPath + "*.py"):
                if (fileName != self.jobPath + '__init__.py'):
                    shortName = fileName.replace(self.jobPath, '').replace('.py', '')
                    module = __import__(self.jobNameSpace + shortName, globals(), locals(), [shortName])
                    self.jobList[shortName] = {
                        'fileName': fileName,
                        'module': module
                    }

        return self.jobList

    def getJob(self, name, specification):
        if name in self.jobList.keys():
            class_ = getattr(self.jobList[name]['module'], name)
            instance = class_(specification)
            return instance
        else:
            print("Error: Job not found! " + name)
            job = Job(specification)
            return job
