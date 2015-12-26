# -*- coding: utf-8 -*-
from collections import defaultdict
import json


class MissionStatement(object):

    missionList = defaultdict(list)
    missionStatementReference = object

    def __init__(self, sensorFactory, sensorList, missionStatementReference):
        super(MissionStatement, self).__init__()
        self.sensorFactory = sensorFactory
        self.missionStatementReference = missionStatementReference

    def readMissionStatementFile(self):
        self.missionList = json.load(self.missionStatementReference.value)

    def loadMissions(self):
        if self.missionStatementReference.Type == 'file':
            #readfile
            self.readMissionStatementFile();
        elif self.missionStatementReference.Type == 'web':
            print('foo')
            #getwebfile and cache it
        elif self.missionStatementReference.Type == 'stream':
            #stream to var and cache it
            print('foo')
