
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrhf_daily_der_table_6(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.VARIANCE_RATIO = NIO_MATRIX()
        self.FUZZY_VOV = NIO_MATRIX()
        self.IVOL_MIN = NIO_MATRIX()
        self.ISKEW_MIN = NIO_MATRIX()
        self.IKURT_MIN = NIO_MATRIX()
        self.UP_VOL_RATIO = NIO_MATRIX()
        self.DOWN_VOL_RATIO = NIO_MATRIX()
        self.RSJ_RATIO = NIO_MATRIX()
        self.RVOL = NIO_MATRIX()
        self.RSKEW = NIO_MATRIX()
        self.RKURT = NIO_MATRIX()
        self.VVOL = NIO_MATRIX()
        self.VSKEW = NIO_MATRIX()
        self.VKURT = NIO_MATRIX()
        self.TRVOL = NIO_MATRIX()
        self.TRSKEW = NIO_MATRIX()
        self.TRKURT = NIO_MATRIX()
        self.VWCR = NIO_MATRIX()
        self.VWCS = NIO_MATRIX()
        self.VWCE = NIO_MATRIX()
        self.VWTE = NIO_MATRIX()
        self.RESILIENCY = NIO_MATRIX()
        self.AMP_VOLATILITY = NIO_MATRIX()
        self.DEAL_AMOUNT_VOL = NIO_MATRIX()
        self.VOLUME_PEAK_COUNT = NIO_MATRIX()
        self.PROFIT_WAVE = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.VARIANCE_RATIO,self.tag + '.VARIANCE_RATIO')
        self.addDailyData(self.FUZZY_VOV,self.tag + '.FUZZY_VOV')
        self.addDailyData(self.IVOL_MIN,self.tag + '.IVOL_MIN')
        self.addDailyData(self.ISKEW_MIN,self.tag + '.ISKEW_MIN')
        self.addDailyData(self.IKURT_MIN,self.tag + '.IKURT_MIN')
        self.addDailyData(self.UP_VOL_RATIO,self.tag + '.UP_VOL_RATIO')
        self.addDailyData(self.DOWN_VOL_RATIO,self.tag + '.DOWN_VOL_RATIO')
        self.addDailyData(self.RSJ_RATIO,self.tag + '.RSJ_RATIO')
        self.addDailyData(self.RVOL,self.tag + '.RVOL')
        self.addDailyData(self.RSKEW,self.tag + '.RSKEW')
        self.addDailyData(self.RKURT,self.tag + '.RKURT')
        self.addDailyData(self.VVOL,self.tag + '.VVOL')
        self.addDailyData(self.VSKEW,self.tag + '.VSKEW')
        self.addDailyData(self.VKURT,self.tag + '.VKURT')
        self.addDailyData(self.TRVOL,self.tag + '.TRVOL')
        self.addDailyData(self.TRSKEW,self.tag + '.TRSKEW')
        self.addDailyData(self.TRKURT,self.tag + '.TRKURT')
        self.addDailyData(self.VWCR,self.tag + '.VWCR')
        self.addDailyData(self.VWCS,self.tag + '.VWCS')
        self.addDailyData(self.VWCE,self.tag + '.VWCE')
        self.addDailyData(self.VWTE,self.tag + '.VWTE')
        self.addDailyData(self.RESILIENCY,self.tag + '.RESILIENCY')
        self.addDailyData(self.AMP_VOLATILITY,self.tag + '.AMP_VOLATILITY')
        self.addDailyData(self.DEAL_AMOUNT_VOL,self.tag + '.DEAL_AMOUNT_VOL')
        self.addDailyData(self.VOLUME_PEAK_COUNT,self.tag + '.VOLUME_PEAK_COUNT')
        self.addDailyData(self.PROFIT_WAVE,self.tag + '.PROFIT_WAVE')
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
            self.VARIANCE_RATIO[di, ii]  = float(linespt[3])
            self.FUZZY_VOV[di, ii]  = float(linespt[4])
            self.IVOL_MIN[di, ii]  = float(linespt[5])
            self.ISKEW_MIN[di, ii]  = float(linespt[6])
            self.IKURT_MIN[di, ii]  = float(linespt[7])
            self.UP_VOL_RATIO[di, ii]  = float(linespt[8])
            self.DOWN_VOL_RATIO[di, ii]  = float(linespt[9])
            self.RSJ_RATIO[di, ii]  = float(linespt[10])
            self.RVOL[di, ii]  = float(linespt[11])
            self.RSKEW[di, ii]  = float(linespt[12])
            self.RKURT[di, ii]  = float(linespt[13])
            self.VVOL[di, ii]  = float(linespt[14])
            self.VSKEW[di, ii]  = float(linespt[15])
            self.VKURT[di, ii]  = float(linespt[16])
            self.TRVOL[di, ii]  = float(linespt[17])
            self.TRSKEW[di, ii]  = float(linespt[18])
            self.TRKURT[di, ii]  = float(linespt[19])
            self.VWCR[di, ii]  = float(linespt[20])
            self.VWCS[di, ii]  = float(linespt[21])
            self.VWCE[di, ii]  = float(linespt[22])
            self.VWTE[di, ii]  = float(linespt[23])
            self.RESILIENCY[di, ii]  = float(linespt[24])
            self.AMP_VOLATILITY[di, ii]  = float(linespt[25])
            self.DEAL_AMOUNT_VOL[di, ii]  = float(linespt[26])
            self.VOLUME_PEAK_COUNT[di, ii]  = float(linespt[27])
            self.PROFIT_WAVE[di, ii]  = float(linespt[28])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.VARIANCE_RATIO[di] = self.VARIANCE_RATIO[di - 1]
        self.FUZZY_VOV[di] = self.FUZZY_VOV[di - 1]
        self.IVOL_MIN[di] = self.IVOL_MIN[di - 1]
        self.ISKEW_MIN[di] = self.ISKEW_MIN[di - 1]
        self.IKURT_MIN[di] = self.IKURT_MIN[di - 1]
        self.UP_VOL_RATIO[di] = self.UP_VOL_RATIO[di - 1]
        self.DOWN_VOL_RATIO[di] = self.DOWN_VOL_RATIO[di - 1]
        self.RSJ_RATIO[di] = self.RSJ_RATIO[di - 1]
        self.RVOL[di] = self.RVOL[di - 1]
        self.RSKEW[di] = self.RSKEW[di - 1]
        self.RKURT[di] = self.RKURT[di - 1]
        self.VVOL[di] = self.VVOL[di - 1]
        self.VSKEW[di] = self.VSKEW[di - 1]
        self.VKURT[di] = self.VKURT[di - 1]
        self.TRVOL[di] = self.TRVOL[di - 1]
        self.TRSKEW[di] = self.TRSKEW[di - 1]
        self.TRKURT[di] = self.TRKURT[di - 1]
        self.VWCR[di] = self.VWCR[di - 1]
        self.VWCS[di] = self.VWCS[di - 1]
        self.VWCE[di] = self.VWCE[di - 1]
        self.VWTE[di] = self.VWTE[di - 1]
        self.RESILIENCY[di] = self.RESILIENCY[di - 1]
        self.AMP_VOLATILITY[di] = self.AMP_VOLATILITY[di - 1]
        self.DEAL_AMOUNT_VOL[di] = self.DEAL_AMOUNT_VOL[di - 1]
        self.VOLUME_PEAK_COUNT[di] = self.VOLUME_PEAK_COUNT[di - 1]
        self.PROFIT_WAVE[di] = self.PROFIT_WAVE[di - 1]