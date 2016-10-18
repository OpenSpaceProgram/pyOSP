# -*- coding: utf-8 -*-

import sys
from gps import *
#add the project folder to pythpath
sys.path.append('../../')

from library.components.SensorModule import SensorModule as Sensor
from library.components.MetaData import MetaData as MetaData


class Gps(Sensor):
    session = None

    def __init__(self):
        super(Gps, self).__init__()
        # Create the GPSD client instance
        self.session = gps(mode=WATCH_ENABLE)

        # Lat
        latitudeMetaData = MetaData("Latitude")
        latitudeMetaData.setUnit("Degrees Lat")
        latitudeMetaData.setValueCallback(self.getLatitude)

        self.addMetaData(latitudeMetaData)

        # Lon
        logitudeMetaData = MetaData("Longitude")
        logitudeMetaData.setUnit("Degrees Lon")
        logitudeMetaData.setValueCallback(self.getLongitude)

        self.addMetaData(logitudeMetaData)
        # UTC
        utcMetaData = MetaData("UTC")
        utcMetaData.setUnit(" UTC")
        utcMetaData.setValueCallback(self.getUtc)

        self.addMetaData(utcMetaData)
        # Altitude
        altitudeMetaData = MetaData("Altitude")
        altitudeMetaData.setUnit("m ")
        altitudeMetaData.setValueCallback(self.getAltitude)

        self.addMetaData(altitudeMetaData)
        # Speed
        speedMetaData = MetaData("Speed")
        speedMetaData.setUnit("m/s")
        speedMetaData.setValueCallback(self.getSpeed)

        self.addMetaData(speedMetaData)

    def getLatitude(self):
        # Loop through the reports from the GPSD client
        for report in self.session:
            # If we have lat as a key in the report
            # we can get the reading for lat!
            if ('lat' in report.keys()):
                return str(report['lat'])

    def getLongitude(self):
        # Loop through the reports from the GPSD client
        for report in self.session:
            # If we have lon as a key in the report
            # we can get the reading for lon!
            if ('lon' in report.keys()):
                return str(report['lon'])

    def getUtc(self):
        # Loop through the reports from the GPSD client
        for report in self.session:
            # If we have time as a key in the report
            # we can get the reading for time!
            if ('time' in report.keys()):
                return str(report['time'])

    def getAltitude(self):
        # Loop through the reports from the GPSD client
        for report in self.session:
            # If we have alt as a key in the report
            # we can get the reading for altitude!
            if ('alt' in report.keys()):
                return str(report['alt'])

    def getSpeed(self):
        # Loop through the reports from the GPSD client
        for report in self.session:
            # If we have speed as a key in the report
            # we can get the reading for speed!
            if ('speed' in report.keys()):
                return str(report['speed'])

    def getMetaData(self):
        return super(Gps, self).getMetaData()