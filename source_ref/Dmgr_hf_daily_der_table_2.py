
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrhf_daily_der_table_2(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.TR_INTRADAY = NIO_MATRIX()
        self.TR_YESTERDAY = NIO_MATRIX()
        self.TRAJ_LIQ = NIO_MATRIX()
        self.TRAJ_LIQ_1 = NIO_MATRIX()
        self.BUY_ILLIQ = NIO_MATRIX()
        self.SELL_ILLIQ = NIO_MATRIX()
        self.TR_0H = NIO_MATRIX()
        self.TR_1H = NIO_MATRIX()
        self.TR_2H = NIO_MATRIX()
        self.TR_3H = NIO_MATRIX()
        self.TR_4H = NIO_MATRIX()
        self.SPREAD_DATE = NIO_MATRIX()
        self.SPREAD = NIO_MATRIX()
        self.LIQ_ELAS = NIO_MATRIX()
        self.BUY_LAMBDA = NIO_MATRIX()
        self.SELL_LAMBDA = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.TR_INTRADAY,self.tag + '.TR_INTRADAY')
        self.addDailyData(self.TR_YESTERDAY,self.tag + '.TR_YESTERDAY')
        self.addDailyData(self.TRAJ_LIQ,self.tag + '.TRAJ_LIQ')
        self.addDailyData(self.TRAJ_LIQ_1,self.tag + '.TRAJ_LIQ_1')
        self.addDailyData(self.BUY_ILLIQ,self.tag + '.BUY_ILLIQ')
        self.addDailyData(self.SELL_ILLIQ,self.tag + '.SELL_ILLIQ')
        self.addDailyData(self.TR_0H,self.tag + '.TR_0H')
        self.addDailyData(self.TR_1H,self.tag + '.TR_1H')
        self.addDailyData(self.TR_2H,self.tag + '.TR_2H')
        self.addDailyData(self.TR_3H,self.tag + '.TR_3H')
        self.addDailyData(self.TR_4H,self.tag + '.TR_4H')
        self.addDailyData(self.SPREAD_DATE,self.tag + '.SPREAD_DATE')
        self.addDailyData(self.SPREAD,self.tag + '.SPREAD')
        self.addDailyData(self.LIQ_ELAS,self.tag + '.LIQ_ELAS')
        self.addDailyData(self.BUY_LAMBDA,self.tag + '.BUY_LAMBDA')
        self.addDailyData(self.SELL_LAMBDA,self.tag + '.SELL_LAMBDA')
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
            self.TR_INTRADAY[di, ii]  = float(linespt[3])
            self.TR_YESTERDAY[di, ii]  = float(linespt[4])
            self.TRAJ_LIQ[di, ii]  = float(linespt[5])
            self.TRAJ_LIQ_1[di, ii]  = float(linespt[6])
            self.BUY_ILLIQ[di, ii]  = float(linespt[7])
            self.SELL_ILLIQ[di, ii]  = float(linespt[8])
            self.TR_0H[di, ii]  = float(linespt[9])
            self.TR_1H[di, ii]  = float(linespt[10])
            self.TR_2H[di, ii]  = float(linespt[11])
            self.TR_3H[di, ii]  = float(linespt[12])
            self.TR_4H[di, ii]  = float(linespt[13])
            self.SPREAD_DATE[di, ii]  = float(linespt[14])
            self.SPREAD[di, ii]  = float(linespt[15])
            self.LIQ_ELAS[di, ii]  = float(linespt[16])
            self.BUY_LAMBDA[di, ii]  = float(linespt[17])
            self.SELL_LAMBDA[di, ii]  = float(linespt[18])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.TR_INTRADAY[di] = self.TR_INTRADAY[di - 1]
        self.TR_YESTERDAY[di] = self.TR_YESTERDAY[di - 1]
        self.TRAJ_LIQ[di] = self.TRAJ_LIQ[di - 1]
        self.TRAJ_LIQ_1[di] = self.TRAJ_LIQ_1[di - 1]
        self.BUY_ILLIQ[di] = self.BUY_ILLIQ[di - 1]
        self.SELL_ILLIQ[di] = self.SELL_ILLIQ[di - 1]
        self.TR_0H[di] = self.TR_0H[di - 1]
        self.TR_1H[di] = self.TR_1H[di - 1]
        self.TR_2H[di] = self.TR_2H[di - 1]
        self.TR_3H[di] = self.TR_3H[di - 1]
        self.TR_4H[di] = self.TR_4H[di - 1]
        self.SPREAD_DATE[di] = self.SPREAD_DATE[di - 1]
        self.SPREAD[di] = self.SPREAD[di - 1]
        self.LIQ_ELAS[di] = self.LIQ_ELAS[di - 1]
        self.BUY_LAMBDA[di] = self.BUY_LAMBDA[di - 1]
        self.SELL_LAMBDA[di] = self.SELL_LAMBDA[di - 1]