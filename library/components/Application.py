# -*- coding: utf-8 -*-


from collections import defaultdict

class Application(object):

    flags = defaultdict(list)

    def __init__(self):
        object.__init__(self)

    def setFlag(self, flagName, flagValue):
        self.flags[flagName] = flagValue
        return

    def getFlag(self, flagName):
        return self.flags[flagName]