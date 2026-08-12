
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrhf_daily_der_table_4(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.RET_INTRADAY = NIO_MATRIX()
        self.REVERSE_VOLUME = NIO_MATRIX()
        self.REVERSE_STRUCTURE = NIO_MATRIX()
        self.REVERSE_VOLUME_CUT = NIO_MATRIX()
        self.REVERSE_APT_CUT = NIO_MATRIX()
        self.IMPROVED_REVERSE = NIO_MATRIX()
        self.OVP = NIO_MATRIX()
        self.OV_INTRADAY_REVERSE = NIO_MATRIX()
        self.RET_AM = NIO_MATRIX()
        self.RET_PM = NIO_MATRIX()
        self.INTRADAY_MOMENTUM_0H = NIO_MATRIX()
        self.INTRADAY_MOMENTUM_1H = NIO_MATRIX()
        self.INTRADAY_MOMENTUM_2H = NIO_MATRIX()
        self.INTRADAY_MOMENTUM_3H = NIO_MATRIX()
        self.INTRADAY_MOMENTUM_4H = NIO_MATRIX()
        self.INTRADAY_MOMENTUM = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.RET_INTRADAY,self.tag + '.RET_INTRADAY')
        self.addDailyData(self.REVERSE_VOLUME,self.tag + '.REVERSE_VOLUME')
        self.addDailyData(self.REVERSE_STRUCTURE,self.tag + '.REVERSE_STRUCTURE')
        self.addDailyData(self.REVERSE_VOLUME_CUT,self.tag + '.REVERSE_VOLUME_CUT')
        self.addDailyData(self.REVERSE_APT_CUT,self.tag + '.REVERSE_APT_CUT')
        self.addDailyData(self.IMPROVED_REVERSE,self.tag + '.IMPROVED_REVERSE')
        self.addDailyData(self.OVP,self.tag + '.OVP')
        self.addDailyData(self.OV_INTRADAY_REVERSE,self.tag + '.OV_INTRADAY_REVERSE')
        self.addDailyData(self.RET_AM,self.tag + '.RET_AM')
        self.addDailyData(self.RET_PM,self.tag + '.RET_PM')
        self.addDailyData(self.INTRADAY_MOMENTUM_0H,self.tag + '.INTRADAY_MOMENTUM_0H')
        self.addDailyData(self.INTRADAY_MOMENTUM_1H,self.tag + '.INTRADAY_MOMENTUM_1H')
        self.addDailyData(self.INTRADAY_MOMENTUM_2H,self.tag + '.INTRADAY_MOMENTUM_2H')
        self.addDailyData(self.INTRADAY_MOMENTUM_3H,self.tag + '.INTRADAY_MOMENTUM_3H')
        self.addDailyData(self.INTRADAY_MOMENTUM_4H,self.tag + '.INTRADAY_MOMENTUM_4H')
        self.addDailyData(self.INTRADAY_MOMENTUM,self.tag + '.INTRADAY_MOMENTUM')
        return

    def loadDay(self, di):
        self.fillnan(di)  # set default value
        if di == len(uv.Dates) - 1:
            return
        if di > 1 and self.backfill:  # backfill
            self.doBackfill(di)
        filepath = os.path.join(self.dataPath, '%d' % uv.Dates[di])
        if not os.path.isfile(filepath):
            print('[ %s ] %s missing on day %d' %  (self.tag, filepath, uv.Dates[di]))
            return
        infile = open(filepath, 'r')
        infile.readline() # skip title line
        updated = 0
        for line in infile:
            linespt = line.strip('\n').split(',')
            # a field could be blank if its value is missing
            linespt = [np.nan if x == '' else x for x in linespt]
            ticker = linespt[1][0:6]
            ii = uv.Instruments.lookup(ticker)
            if ii < 0:
                continue
            self.RET_INTRADAY[di, ii]  = float(linespt[3])
            self.REVERSE_VOLUME[di, ii]  = float(linespt[4])
            self.REVERSE_STRUCTURE[di, ii]  = float(linespt[5])
            self.REVERSE_VOLUME_CUT[di, ii]  = float(linespt[6])
            self.REVERSE_APT_CUT[di, ii]  = float(linespt[7])
            self.IMPROVED_REVERSE[di, ii]  = float(linespt[8])
            self.OVP[di, ii]  = float(linespt[9])
            self.OV_INTRADAY_REVERSE[di, ii]  = float(linespt[10])
            self.RET_AM[di, ii]  = float(linespt[11])
            self.RET_PM[di, ii]  = float(linespt[12])
            self.INTRADAY_MOMENTUM_0H[di, ii]  = float(linespt[13])
            self.INTRADAY_MOMENTUM_1H[di, ii]  = float(linespt[14])
            self.INTRADAY_MOMENTUM_2H[di, ii]  = float(linespt[15])
            self.INTRADAY_MOMENTUM_3H[di, ii]  = float(linespt[16])
            self.INTRADAY_MOMENTUM_4H[di, ii]  = float(linespt[17])
            self.INTRADAY_MOMENTUM[di, ii]  = float(linespt[18])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.RET_INTRADAY[di] = self.RET_INTRADAY[di - 1]
        self.REVERSE_VOLUME[di] = self.REVERSE_VOLUME[di - 1]
        self.REVERSE_STRUCTURE[di] = self.REVERSE_STRUCTURE[di - 1]
        self.REVERSE_VOLUME_CUT[di] = self.REVERSE_VOLUME_CUT[di - 1]
        self.REVERSE_APT_CUT[di] = self.REVERSE_APT_CUT[di - 1]
        self.IMPROVED_REVERSE[di] = self.IMPROVED_REVERSE[di - 1]
        self.OVP[di] = self.OVP[di - 1]
        self.OV_INTRADAY_REVERSE[di] = self.OV_INTRADAY_REVERSE[di - 1]
        self.RET_AM[di] = self.RET_AM[di - 1]
        self.RET_PM[di] = self.RET_PM[di - 1]
        self.INTRADAY_MOMENTUM_0H[di] = self.INTRADAY_MOMENTUM_0H[di - 1]
        self.INTRADAY_MOMENTUM_1H[di] = self.INTRADAY_MOMENTUM_1H[di - 1]
        self.INTRADAY_MOMENTUM_2H[di] = self.INTRADAY_MOMENTUM_2H[di - 1]
        self.INTRADAY_MOMENTUM_3H[di] = self.INTRADAY_MOMENTUM_3H[di - 1]
        self.INTRADAY_MOMENTUM_4H[di] = self.INTRADAY_MOMENTUM_4H[di - 1]
        self.INTRADAY_MOMENTUM[di] = self.INTRADAY_MOMENTUM[di - 1]