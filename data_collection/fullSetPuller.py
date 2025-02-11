# -*- coding: utf-8 -*-
__author__ = 'Ryan Boncheff'
__copyright__ = 'Ryan Boncheff'
__credits__ = None
__license__ = 'GNU General Public License v3.0'
__version__ = 'A001'
__maintainer__ =  'Ryan Boncheff'
__email__ = 'ryanboncheff@gmail.com'
__status__ = 'Alpha'

'''
Runs:
    detailsPuller.py
    wavePuller.py
    eventPuller.py

Resultant CSVs will be generated in the PAP_CODE folder
See readme for full description of each script

Before running this script:
    Set dbPath to the location of your iMatrix db
    Set eventPath to the location of your SD card
'''

dbPath = r'C:\Users\dfurt\Documents\iMatrix\PATIENT\000001\000001_patient.db'
sdPath = r'E:\testprojects\cpapDataSDCARD\THERAPY\RECORD'

from data_collection.detailsPuller import detailsPuller
from data_collection.wavePuller import wavePuller
from data_collection.eventPuller import eventPuller

def fullSetPuller():

    detailsPuller(dbPath)
    wavePuller(dbPath)
    eventPuller(sdPath)

if __name__ == '__main__':
    fullSetPuller()
