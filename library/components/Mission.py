# -*- coding: utf-8 -*-
from library.components.SensorFactory import SensorFactory as SensorFactory
from library.components.TriggerFactory import TriggerFactory as TriggerFactory


class Mission(object):

    missionReference = dict

    def __init__(self, missionReference):
        super(Mission, self).__init__()
        self.missionReference = missionReference
        self.loadTriggers()

    def run(self):
        senseFact = SensorFactory()
        trigFact = TriggerFactory()
        #print(senseFact.getSensorList())
        missTrig = trigFact.getTrigger(self.missionReference.trigger.name)
        if (missTrig.test(senseFact)):
            missTrig.run()