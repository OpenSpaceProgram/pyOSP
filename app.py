# -*- coding: utf-8 -*-

from library.components.SensorFactory import SensorFactory as SensorFactory

fact = SensorFactory()

print(fact.getSensorList())

newtemp = fact.getSensor('Temperature')

meta = newtemp.getMetaData()

for key in meta.keys():
    print(key)
    print(meta[key].getValue(), meta[key].getUnit())