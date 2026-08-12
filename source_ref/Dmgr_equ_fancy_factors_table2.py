
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrequ_fancy_factors_table2(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.ROE_Q = NIO_MATRIX()
        self.ROE_TTM = NIO_MATRIX()
        self.ROE_Q_YOYD = NIO_MATRIX()
        self.ROE_TTM_QOQD = NIO_MATRIX()
        self.ROE_TTM_YOYD = NIO_MATRIX()
        self.DTOP = NIO_MATRIX()
        self.DIV_PAIDRATIO = NIO_MATRIX()
        self.Q_ETOP = NIO_MATRIX()
        self.Q_STOP = NIO_MATRIX()
        self.D_Q_ETOP = NIO_MATRIX()
        self.D_Q_STOP = NIO_MATRIX()
        self.AI_SUDE = NIO_MATRIX()
        self.CON_SUDE = NIO_MATRIX()
        self.AI_SUDREV = NIO_MATRIX()
        self.CON_SUDREV = NIO_MATRIX()
        self.AI_NP_YOY = NIO_MATRIX()
        self.AI_REV_YOY = NIO_MATRIX()
        self.CON_NP_YOY = NIO_MATRIX()
        self.CON_REV_YOY = NIO_MATRIX()
        self.AI_ETOP = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.ROE_Q,self.tag + '.ROE_Q')
        self.addDailyData(self.ROE_TTM,self.tag + '.ROE_TTM')
        self.addDailyData(self.ROE_Q_YOYD,self.tag + '.ROE_Q_YOYD')
        self.addDailyData(self.ROE_TTM_QOQD,self.tag + '.ROE_TTM_QOQD')
        self.addDailyData(self.ROE_TTM_YOYD,self.tag + '.ROE_TTM_YOYD')
        self.addDailyData(self.DTOP,self.tag + '.DTOP')
        self.addDailyData(self.DIV_PAIDRATIO,self.tag + '.DIV_PAIDRATIO')
        self.addDailyData(self.Q_ETOP,self.tag + '.Q_ETOP')
        self.addDailyData(self.Q_STOP,self.tag + '.Q_STOP')
        self.addDailyData(self.D_Q_ETOP,self.tag + '.D_Q_ETOP')
        self.addDailyData(self.D_Q_STOP,self.tag + '.D_Q_STOP')
        self.addDailyData(self.AI_SUDE,self.tag + '.AI_SUDE')
        self.addDailyData(self.CON_SUDE,self.tag + '.CON_SUDE')
        self.addDailyData(self.AI_SUDREV,self.tag + '.AI_SUDREV')
        self.addDailyData(self.CON_SUDREV,self.tag + '.CON_SUDREV')
        self.addDailyData(self.AI_NP_YOY,self.tag + '.AI_NP_YOY')
        self.addDailyData(self.AI_REV_YOY,self.tag + '.AI_REV_YOY')
        self.addDailyData(self.CON_NP_YOY,self.tag + '.CON_NP_YOY')
        self.addDailyData(self.CON_REV_YOY,self.tag + '.CON_REV_YOY')
        self.addDailyData(self.AI_ETOP,self.tag + '.AI_ETOP')
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
            self.ROE_Q[di, ii]  = float(linespt[3])
            self.ROE_TTM[di, ii]  = float(linespt[4])
            self.ROE_Q_YOYD[di, ii]  = float(linespt[5])
            self.ROE_TTM_QOQD[di, ii]  = float(linespt[6])
            self.ROE_TTM_YOYD[di, ii]  = float(linespt[7])
            self.DTOP[di, ii]  = float(linespt[8])
            self.DIV_PAIDRATIO[di, ii]  = float(linespt[9])
            self.Q_ETOP[di, ii]  = float(linespt[10])
            self.Q_STOP[di, ii]  = float(linespt[11])
            self.D_Q_ETOP[di, ii]  = float(linespt[12])
            self.D_Q_STOP[di, ii]  = float(linespt[13])
            self.AI_SUDE[di, ii]  = float(linespt[14])
            self.CON_SUDE[di, ii]  = float(linespt[15])
            self.AI_SUDREV[di, ii]  = float(linespt[16])
            self.CON_SUDREV[di, ii]  = float(linespt[17])
            self.AI_NP_YOY[di, ii]  = float(linespt[18])
            self.AI_REV_YOY[di, ii]  = float(linespt[19])
            self.CON_NP_YOY[di, ii]  = float(linespt[20])
            self.CON_REV_YOY[di, ii]  = float(linespt[21])
            self.AI_ETOP[di, ii]  = float(linespt[22])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.ROE_Q[di] = self.ROE_Q[di - 1]
        self.ROE_TTM[di] = self.ROE_TTM[di - 1]
        self.ROE_Q_YOYD[di] = self.ROE_Q_YOYD[di - 1]
        self.ROE_TTM_QOQD[di] = self.ROE_TTM_QOQD[di - 1]
        self.ROE_TTM_YOYD[di] = self.ROE_TTM_YOYD[di - 1]
        self.DTOP[di] = self.DTOP[di - 1]
        self.DIV_PAIDRATIO[di] = self.DIV_PAIDRATIO[di - 1]
        self.Q_ETOP[di] = self.Q_ETOP[di - 1]
        self.Q_STOP[di] = self.Q_STOP[di - 1]
        self.D_Q_ETOP[di] = self.D_Q_ETOP[di - 1]
        self.D_Q_STOP[di] = self.D_Q_STOP[di - 1]
        self.AI_SUDE[di] = self.AI_SUDE[di - 1]
        self.CON_SUDE[di] = self.CON_SUDE[di - 1]
        self.AI_SUDREV[di] = self.AI_SUDREV[di - 1]
        self.CON_SUDREV[di] = self.CON_SUDREV[di - 1]
        self.AI_NP_YOY[di] = self.AI_NP_YOY[di - 1]
        self.AI_REV_YOY[di] = self.AI_REV_YOY[di - 1]
        self.CON_NP_YOY[di] = self.CON_NP_YOY[di - 1]
        self.CON_REV_YOY[di] = self.CON_REV_YOY[di - 1]
        self.AI_ETOP[di] = self.AI_ETOP[di - 1]