
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrequ_fancy_factors_table9(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.NEWS_NUM_30 = NIO_MATRIX()
        self.NEWS_NUM_NEG_30 = NIO_MATRIX()
        self.NEWS_NUM_VOL_30 = NIO_MATRIX()
        self.NEWS_NUM_POS_VOL_30 = NIO_MATRIX()
        self.NEWS_NUM_VOL_LT = NIO_MATRIX()
        self.GTRA_BUY_HOT = NIO_MATRIX()
        self.GTRA_BUY_HOT_CHG = NIO_MATRIX()
        self.GTRA_SELL_HOT_CHG = NIO_MATRIX()
        self.GTRA_BUY_PCT = NIO_MATRIX()
        self.GTRA_SELL_PCT = NIO_MATRIX()
        self.GTRA_BUY_PCT_VOL = NIO_MATRIX()
        self.GTRA_SELL_PCT_VOL = NIO_MATRIX()
        self.XTRA_BUY_HOT = NIO_MATRIX()
        self.XTRA_BUY_HOT_CHG = NIO_MATRIX()
        self.XTRA_SELL_HOT_CHG = NIO_MATRIX()
        self.XTRA_BUY_PCT = NIO_MATRIX()
        self.XTRA_SELL_PCT = NIO_MATRIX()
        self.XTRA_BUY_PCT_VOL = NIO_MATRIX()
        self.XTRA_SELL_PCT_VOL = NIO_MATRIX()
        self.GPOST_HOT = NIO_MATRIX()
        self.GPOST_POS_PCT_VOL = NIO_MATRIX()
        self.GPOST_NEG_PCT_VOL = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.NEWS_NUM_30,self.tag + '.NEWS_NUM_30')
        self.addDailyData(self.NEWS_NUM_NEG_30,self.tag + '.NEWS_NUM_NEG_30')
        self.addDailyData(self.NEWS_NUM_VOL_30,self.tag + '.NEWS_NUM_VOL_30')
        self.addDailyData(self.NEWS_NUM_POS_VOL_30,self.tag + '.NEWS_NUM_POS_VOL_30')
        self.addDailyData(self.NEWS_NUM_VOL_LT,self.tag + '.NEWS_NUM_VOL_LT')
        self.addDailyData(self.GTRA_BUY_HOT,self.tag + '.GTRA_BUY_HOT')
        self.addDailyData(self.GTRA_BUY_HOT_CHG,self.tag + '.GTRA_BUY_HOT_CHG')
        self.addDailyData(self.GTRA_SELL_HOT_CHG,self.tag + '.GTRA_SELL_HOT_CHG')
        self.addDailyData(self.GTRA_BUY_PCT,self.tag + '.GTRA_BUY_PCT')
        self.addDailyData(self.GTRA_SELL_PCT,self.tag + '.GTRA_SELL_PCT')
        self.addDailyData(self.GTRA_BUY_PCT_VOL,self.tag + '.GTRA_BUY_PCT_VOL')
        self.addDailyData(self.GTRA_SELL_PCT_VOL,self.tag + '.GTRA_SELL_PCT_VOL')
        self.addDailyData(self.XTRA_BUY_HOT,self.tag + '.XTRA_BUY_HOT')
        self.addDailyData(self.XTRA_BUY_HOT_CHG,self.tag + '.XTRA_BUY_HOT_CHG')
        self.addDailyData(self.XTRA_SELL_HOT_CHG,self.tag + '.XTRA_SELL_HOT_CHG')
        self.addDailyData(self.XTRA_BUY_PCT,self.tag + '.XTRA_BUY_PCT')
        self.addDailyData(self.XTRA_SELL_PCT,self.tag + '.XTRA_SELL_PCT')
        self.addDailyData(self.XTRA_BUY_PCT_VOL,self.tag + '.XTRA_BUY_PCT_VOL')
        self.addDailyData(self.XTRA_SELL_PCT_VOL,self.tag + '.XTRA_SELL_PCT_VOL')
        self.addDailyData(self.GPOST_HOT,self.tag + '.GPOST_HOT')
        self.addDailyData(self.GPOST_POS_PCT_VOL,self.tag + '.GPOST_POS_PCT_VOL')
        self.addDailyData(self.GPOST_NEG_PCT_VOL,self.tag + '.GPOST_NEG_PCT_VOL')
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
            self.NEWS_NUM_30[di, ii]  = float(linespt[3])
            self.NEWS_NUM_NEG_30[di, ii]  = float(linespt[4])
            self.NEWS_NUM_VOL_30[di, ii]  = float(linespt[5])
            self.NEWS_NUM_POS_VOL_30[di, ii]  = float(linespt[6])
            self.NEWS_NUM_VOL_LT[di, ii]  = float(linespt[7])
            self.GTRA_BUY_HOT[di, ii]  = float(linespt[8])
            self.GTRA_BUY_HOT_CHG[di, ii]  = float(linespt[9])
            self.GTRA_SELL_HOT_CHG[di, ii]  = float(linespt[10])
            self.GTRA_BUY_PCT[di, ii]  = float(linespt[11])
            self.GTRA_SELL_PCT[di, ii]  = float(linespt[12])
            self.GTRA_BUY_PCT_VOL[di, ii]  = float(linespt[13])
            self.GTRA_SELL_PCT_VOL[di, ii]  = float(linespt[14])
            self.XTRA_BUY_HOT[di, ii]  = float(linespt[15])
            self.XTRA_BUY_HOT_CHG[di, ii]  = float(linespt[16])
            self.XTRA_SELL_HOT_CHG[di, ii]  = float(linespt[17])
            self.XTRA_BUY_PCT[di, ii]  = float(linespt[18])
            self.XTRA_SELL_PCT[di, ii]  = float(linespt[19])
            self.XTRA_BUY_PCT_VOL[di, ii]  = float(linespt[20])
            self.XTRA_SELL_PCT_VOL[di, ii]  = float(linespt[21])
            self.GPOST_HOT[di, ii]  = float(linespt[22])
            self.GPOST_POS_PCT_VOL[di, ii]  = float(linespt[23])
            self.GPOST_NEG_PCT_VOL[di, ii]  = float(linespt[24])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.NEWS_NUM_30[di] = self.NEWS_NUM_30[di - 1]
        self.NEWS_NUM_NEG_30[di] = self.NEWS_NUM_NEG_30[di - 1]
        self.NEWS_NUM_VOL_30[di] = self.NEWS_NUM_VOL_30[di - 1]
        self.NEWS_NUM_POS_VOL_30[di] = self.NEWS_NUM_POS_VOL_30[di - 1]
        self.NEWS_NUM_VOL_LT[di] = self.NEWS_NUM_VOL_LT[di - 1]
        self.GTRA_BUY_HOT[di] = self.GTRA_BUY_HOT[di - 1]
        self.GTRA_BUY_HOT_CHG[di] = self.GTRA_BUY_HOT_CHG[di - 1]
        self.GTRA_SELL_HOT_CHG[di] = self.GTRA_SELL_HOT_CHG[di - 1]
        self.GTRA_BUY_PCT[di] = self.GTRA_BUY_PCT[di - 1]
        self.GTRA_SELL_PCT[di] = self.GTRA_SELL_PCT[di - 1]
        self.GTRA_BUY_PCT_VOL[di] = self.GTRA_BUY_PCT_VOL[di - 1]
        self.GTRA_SELL_PCT_VOL[di] = self.GTRA_SELL_PCT_VOL[di - 1]
        self.XTRA_BUY_HOT[di] = self.XTRA_BUY_HOT[di - 1]
        self.XTRA_BUY_HOT_CHG[di] = self.XTRA_BUY_HOT_CHG[di - 1]
        self.XTRA_SELL_HOT_CHG[di] = self.XTRA_SELL_HOT_CHG[di - 1]
        self.XTRA_BUY_PCT[di] = self.XTRA_BUY_PCT[di - 1]
        self.XTRA_SELL_PCT[di] = self.XTRA_SELL_PCT[di - 1]
        self.XTRA_BUY_PCT_VOL[di] = self.XTRA_BUY_PCT_VOL[di - 1]
        self.XTRA_SELL_PCT_VOL[di] = self.XTRA_SELL_PCT_VOL[di - 1]
        self.GPOST_HOT[di] = self.GPOST_HOT[di - 1]
        self.GPOST_POS_PCT_VOL[di] = self.GPOST_POS_PCT_VOL[di - 1]
        self.GPOST_NEG_PCT_VOL[di] = self.GPOST_NEG_PCT_VOL[di - 1]