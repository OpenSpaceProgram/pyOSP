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

        doJob = True

        if ('conditions' in self.missionReference):
            senseFact = SensorFactory()
            for mCondition in self.missionReference['conditions']:
                for conditionName in mCondition:
                    conditionValue = mCondition[conditionName][1]

                    sensorOptions = mCondition[conditionName][0].partition(',')
                    sensorName = sensorOptions[0].strip()
                    metaDataName = sensorOptions[2].strip()

                    #create the sensor
                    sensor = senseFact.getSensor(sensorName)
                    if (sensor is False):
                        #sensor module did not load
                        doJob = False
                    else:
                        #get the sensors meta data
                        metaData = sensor.getMetaData()
                        #create a condition to test (equals, less than, greater than etc)
                        condition = Condition(conditionName)
                        #if the condition fails do not do job
                        if (condition.test(metaData[metaDataName].getValue(), conditionValue) is False):
                            doJob = False

        if ('delay' in self.missionReference):
            timedelay = str(self.lastRun + int(self.missionReference['delay']))
            #create and test time condition
            condition = Condition('gthan')
            if (condition.test(int(time.time()), timedelay) is False):
                doJob = False

        jobFact = JobFactory()
        if ('job' in self.missionReference and doJob is not False):
            #set the last run time
            self.lastRun = int(time.time())
            for jobName in self.missionReference['job']:
                print("." + jobName)
                #grab the job specification to pass to the factory
                jobSpec = self.missionReference['job'][jobName]
                job = jobFact.getJob(jobName, jobSpec)
                job.run()
        elif(doJob is False):
            print('-')
        else:
            print('Error: Job not found')