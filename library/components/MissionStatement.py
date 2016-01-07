# -*- coding: utf-8 -*-


import sys
from collections import defaultdict
import json
import yaml
sys.path.append('../../')
from library.components.Application import Application as Application


class MissionStatement(Application):

    missionList = defaultdict(list)
    missionStatementReference = object

    def __init__(self, missionStatementReference):
        super(MissionStatement, self).__init__()
        self.missionStatementReference = missionStatementReference
        self.loadMissions()

    def readMissionStatementFile(self, jsonFlag):
        if (jsonFlag):
            self.missionList = json.load(self.missionStatementReference['value'])
        else:
            missionFile = open(self.missionStatementReference['value'])
            self.missionList = yaml.load(missionFile.read())

    def getMissionList(self):
        return self.missionList

    def loadMissions(self):
        if self.missionStatementReference['type'] == 'file':
            #readfile
            self.readMissionStatementFile(False)
        elif self.missionStatementReference['type'] == 'filejson':
            #readfile
            self.readMissionStatementFile(True)
        elif self.missionStatementReference['type'] == 'web':
            print('foo')
            #getwebfile and cache it
        elif self.missionStatementReference['type'] == 'stream':
            #stream to var and cache it
            print('foo')
