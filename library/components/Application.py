# -*- coding: utf-8 -*-


from collections import defaultdict

class Application():

    flags = defaultdict(list)

    def __init__(self):
        super(Application, self).__init__()

    def setFlag(self, flagName, flagValue):
        self.flags[flagName] = flagValue
        return

    def getFlag(self, flagName):
        return self.flags[flagName]