# -*- coding: utf-8 -*-

from library.components.MissionStatement import MissionStatement
from library.components.Mission import Mission
import os
import yaml

msrYamlDoc = """
value:  """+os.path.join(os.path.dirname(__file__), 'missionStatement')+"""
type: file
"""

missionStatementReference = yaml.load(msrYamlDoc)

print (missionStatementReference['value'])

missionStatement = MissionStatement(missionStatementReference)

#try:
#while True:
missionlist = missionStatement.getMissionList()

for missionInstance in missionlist:
    for missionName in missionInstance:
        #possible new thread here?
        theMission = Mission(missionName, missionInstance[missionName])
        missionStatement.setFlag('missionStatement', missionName)
        theMission.run()
#except KeyboardInterrupt:
#    print ('interrupted!')