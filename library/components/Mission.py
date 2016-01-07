# -*- coding: utf-8 -*-
from library.components.JobFactory import JobFactory as JobFactory
from library.components.SensorFactory import SensorFactory as SensorFactory
from library.components.Condition import Condition as Condition
import time
import sys
from collections import defaultdict
sys.path.append('../../')
from library.components.Application import Application as Application


class Mission(Application):

    missionReference = defaultdict(list)
    missionName = ''
    lastRun = 0

    def __init__(self, missionName, missionReference):
        super(Mission, self).__init__()
        self.missionReference = missionReference
        self.missionName = missionName

    def run(self):
        print("Doing mission: " + self.missionName)
        print("\\GetFLAG::" + self.getFlag('missionStatement'))

        doJob = True

        if ('conditions' in self.missionReference):
            senseFact = SensorFactory()
            for mCondition in self.missionReference['conditions']:
                for conditionName in mCondition:
                    sensorOptions = mCondition[conditionName][0].partition(',')
                    sensorName = sensorOptions[0].strip()
                    metaDataName = sensorOptions[2].strip()
                    print(sensorName)
                    sensor = senseFact.getSensor(sensorName)
                    if (sensor != False):
                        metaData = sensor.getMetaData()
                        condition = Condition(conditionName)
                        if (condition.test(metaData[metaDataName].getValue() , mCondition[conditionName][1]) == False):
                            doJob = False

#            if (isinstance(s, str)):
#            value1 = 1
#            value1 = 2
#            condition = Condition(mCondition)
        if ('delay' in self.missionReference):
            timedelay = str(self.lastRun + int(self.missionReference['delay']))
            #create and test time condition
            condition = Condition('gthan')
            if (condition.test(str(time.time()),timedelay) is False):
                doJob = False

        jobFact = JobFactory()
        if ('job' in self.missionReference and doJob):
            for jobName in self.missionReference['job']:
                print(":Doing JOB " + jobName)
                job = jobFact.getJob(jobName, self.missionReference['job'][jobName])
                job.run()
        else:
            print('No jobs')
