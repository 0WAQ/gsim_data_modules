
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrhf_daily_der_table_1(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.INTRADAY_CORR = NIO_MATRIX()
        self.RV_CORR = NIO_MATRIX()
        self.DP_POS_P_CORR = NIO_MATRIX()
        self.DP_NEG_P_CORR = NIO_MATRIX()
        self.DP_POS_DP_POS_CORR = NIO_MATRIX()
        self.DP_NEG_DP_NEG_CORR = NIO_MATRIX()
        self.DV_POS_V_CORR = NIO_MATRIX()
        self.DV_NEG_V_CORR = NIO_MATRIX()
        self.DV_POS_DV_POS_CORR = NIO_MATRIX()
        self.DV_POS_DV_NEG_CORR = NIO_MATRIX()
        self.DV_NEG_DV_NEG_CORR = NIO_MATRIX()
        self.DV_NEG_DV_POS_CORR = NIO_MATRIX()
        self.DV_POS_DP_POS_CORR = NIO_MATRIX()
        self.DV_POS_DP_NEG_CORR = NIO_MATRIX()
        self.DV_NEG_DP_POS_CORR = NIO_MATRIX()
        self.DV_NEG_DP_NEG_CORR = NIO_MATRIX()
        self.INTRADAY_BETA = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.INTRADAY_CORR,self.tag + '.INTRADAY_CORR')
        self.addDailyData(self.RV_CORR,self.tag + '.RV_CORR')
        self.addDailyData(self.DP_POS_P_CORR,self.tag + '.DP_POS_P_CORR')
        self.addDailyData(self.DP_NEG_P_CORR,self.tag + '.DP_NEG_P_CORR')
        self.addDailyData(self.DP_POS_DP_POS_CORR,self.tag + '.DP_POS_DP_POS_CORR')
        self.addDailyData(self.DP_NEG_DP_NEG_CORR,self.tag + '.DP_NEG_DP_NEG_CORR')
        self.addDailyData(self.DV_POS_V_CORR,self.tag + '.DV_POS_V_CORR')
        self.addDailyData(self.DV_NEG_V_CORR,self.tag + '.DV_NEG_V_CORR')
        self.addDailyData(self.DV_POS_DV_POS_CORR,self.tag + '.DV_POS_DV_POS_CORR')
        self.addDailyData(self.DV_POS_DV_NEG_CORR,self.tag + '.DV_POS_DV_NEG_CORR')
        self.addDailyData(self.DV_NEG_DV_NEG_CORR,self.tag + '.DV_NEG_DV_NEG_CORR')
        self.addDailyData(self.DV_NEG_DV_POS_CORR,self.tag + '.DV_NEG_DV_POS_CORR')
        self.addDailyData(self.DV_POS_DP_POS_CORR,self.tag + '.DV_POS_DP_POS_CORR')
        self.addDailyData(self.DV_POS_DP_NEG_CORR,self.tag + '.DV_POS_DP_NEG_CORR')
        self.addDailyData(self.DV_NEG_DP_POS_CORR,self.tag + '.DV_NEG_DP_POS_CORR')
        self.addDailyData(self.DV_NEG_DP_NEG_CORR,self.tag + '.DV_NEG_DP_NEG_CORR')
        self.addDailyData(self.INTRADAY_BETA,self.tag + '.INTRADAY_BETA')
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
            self.INTRADAY_CORR[di, ii]  = float(linespt[3])
            self.RV_CORR[di, ii]  = float(linespt[4])
            self.DP_POS_P_CORR[di, ii]  = float(linespt[5])
            self.DP_NEG_P_CORR[di, ii]  = float(linespt[6])
            self.DP_POS_DP_POS_CORR[di, ii]  = float(linespt[7])
            self.DP_NEG_DP_NEG_CORR[di, ii]  = float(linespt[8])
            self.DV_POS_V_CORR[di, ii]  = float(linespt[9])
            self.DV_NEG_V_CORR[di, ii]  = float(linespt[10])
            self.DV_POS_DV_POS_CORR[di, ii]  = float(linespt[11])
            self.DV_POS_DV_NEG_CORR[di, ii]  = float(linespt[12])
            self.DV_NEG_DV_NEG_CORR[di, ii]  = float(linespt[13])
            self.DV_NEG_DV_POS_CORR[di, ii]  = float(linespt[14])
            self.DV_POS_DP_POS_CORR[di, ii]  = float(linespt[15])
            self.DV_POS_DP_NEG_CORR[di, ii]  = float(linespt[16])
            self.DV_NEG_DP_POS_CORR[di, ii]  = float(linespt[17])
            self.DV_NEG_DP_NEG_CORR[di, ii]  = float(linespt[18])
            self.INTRADAY_BETA[di, ii]  = float(linespt[19])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.INTRADAY_CORR[di] = self.INTRADAY_CORR[di - 1]
        self.RV_CORR[di] = self.RV_CORR[di - 1]
        self.DP_POS_P_CORR[di] = self.DP_POS_P_CORR[di - 1]
        self.DP_NEG_P_CORR[di] = self.DP_NEG_P_CORR[di - 1]
        self.DP_POS_DP_POS_CORR[di] = self.DP_POS_DP_POS_CORR[di - 1]
        self.DP_NEG_DP_NEG_CORR[di] = self.DP_NEG_DP_NEG_CORR[di - 1]
        self.DV_POS_V_CORR[di] = self.DV_POS_V_CORR[di - 1]
        self.DV_NEG_V_CORR[di] = self.DV_NEG_V_CORR[di - 1]
        self.DV_POS_DV_POS_CORR[di] = self.DV_POS_DV_POS_CORR[di - 1]
        self.DV_POS_DV_NEG_CORR[di] = self.DV_POS_DV_NEG_CORR[di - 1]
        self.DV_NEG_DV_NEG_CORR[di] = self.DV_NEG_DV_NEG_CORR[di - 1]
        self.DV_NEG_DV_POS_CORR[di] = self.DV_NEG_DV_POS_CORR[di - 1]
        self.DV_POS_DP_POS_CORR[di] = self.DV_POS_DP_POS_CORR[di - 1]
        self.DV_POS_DP_NEG_CORR[di] = self.DV_POS_DP_NEG_CORR[di - 1]
        self.DV_NEG_DP_POS_CORR[di] = self.DV_NEG_DP_POS_CORR[di - 1]
        self.DV_NEG_DP_NEG_CORR[di] = self.DV_NEG_DP_NEG_CORR[di - 1]
        self.INTRADAY_BETA[di] = self.INTRADAY_BETA[di - 1]