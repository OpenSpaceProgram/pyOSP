# -*- coding: utf-8 -*-
from library.components.JobFactory import JobFactory as JobFactory
from library.components.SensorFactory import SensorFactory as SensorFactory
from library.components.Condition import Condition as Condition
import time
from collections import defaultdict


class Mission(object):

    missionReference = defaultdict(list)
    missionName = ''
    lastRun = time.time

    def __init__(self, missionName, missionReference):
        super(Mission, self).__init__()
        self.missionReference = missionReference
        self.missionName = missionName

    def run(self):
        print("Doing mission: " + self.missionName)

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
            timedelay = str(time.time() + int(self.missionReference['delay']))
            #create and test time condition
            condition = Condition('gthan')
            if (condition.test(str(time.time(),timedelay)) == False):
                doJob = False

        jobFact = JobFactory()
        if ('job' in self.missionReference and doJob):
            for jobName in self.missionReference['job']:
                print(":Doing JOB " + jobName)
                job = jobFact.getJob(jobName, self.missionReference['job'][jobName])
                job.run()
        else:
            print('No jobs')
