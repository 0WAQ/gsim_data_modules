
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrequ_fancy_factors_table8(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.CCR_Q = NIO_MATRIX()
        self.TOE_TTM_STD = NIO_MATRIX()
        self.CFP_TTM_STD = NIO_MATRIX()
        self.GOVERNANCE = NIO_MATRIX()
        self.PROFIT_QQC = NIO_MATRIX()
        self.GROWTH_QQC = NIO_MATRIX()
        self.OPERATION_QQC = NIO_MATRIX()
        self.Q_SCORE = NIO_MATRIX()
        self.CON_DTOP = NIO_MATRIX()
        self.CON_DTOP_Z90 = NIO_MATRIX()
        self.CON_DTOP_Z180 = NIO_MATRIX()
        self.CON_DTOP_DA30 = NIO_MATRIX()
        self.CON_DTOP_DA90 = NIO_MATRIX()
        self.CON_DPR = NIO_MATRIX()
        self.AI_DTOP = NIO_MATRIX()
        self.AI_DTOP_Z90 = NIO_MATRIX()
        self.AI_DTOP_Z180 = NIO_MATRIX()
        self.AI_DTOP_DA30 = NIO_MATRIX()
        self.AI_DTOP_DA90 = NIO_MATRIX()
        self.AI_DPR = NIO_MATRIX()
        self.QES = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.CCR_Q,self.tag + '.CCR_Q')
        self.addDailyData(self.TOE_TTM_STD,self.tag + '.TOE_TTM_STD')
        self.addDailyData(self.CFP_TTM_STD,self.tag + '.CFP_TTM_STD')
        self.addDailyData(self.GOVERNANCE,self.tag + '.GOVERNANCE')
        self.addDailyData(self.PROFIT_QQC,self.tag + '.PROFIT_QQC')
        self.addDailyData(self.GROWTH_QQC,self.tag + '.GROWTH_QQC')
        self.addDailyData(self.OPERATION_QQC,self.tag + '.OPERATION_QQC')
        self.addDailyData(self.Q_SCORE,self.tag + '.Q_SCORE')
        self.addDailyData(self.CON_DTOP,self.tag + '.CON_DTOP')
        self.addDailyData(self.CON_DTOP_Z90,self.tag + '.CON_DTOP_Z90')
        self.addDailyData(self.CON_DTOP_Z180,self.tag + '.CON_DTOP_Z180')
        self.addDailyData(self.CON_DTOP_DA30,self.tag + '.CON_DTOP_DA30')
        self.addDailyData(self.CON_DTOP_DA90,self.tag + '.CON_DTOP_DA90')
        self.addDailyData(self.CON_DPR,self.tag + '.CON_DPR')
        self.addDailyData(self.AI_DTOP,self.tag + '.AI_DTOP')
        self.addDailyData(self.AI_DTOP_Z90,self.tag + '.AI_DTOP_Z90')
        self.addDailyData(self.AI_DTOP_Z180,self.tag + '.AI_DTOP_Z180')
        self.addDailyData(self.AI_DTOP_DA30,self.tag + '.AI_DTOP_DA30')
        self.addDailyData(self.AI_DTOP_DA90,self.tag + '.AI_DTOP_DA90')
        self.addDailyData(self.AI_DPR,self.tag + '.AI_DPR')
        self.addDailyData(self.QES,self.tag + '.QES')
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
            self.CCR_Q[di, ii]  = float(linespt[3])
            self.TOE_TTM_STD[di, ii]  = float(linespt[4])
            self.CFP_TTM_STD[di, ii]  = float(linespt[5])
            self.GOVERNANCE[di, ii]  = float(linespt[6])
            self.PROFIT_QQC[di, ii]  = float(linespt[7])
            self.GROWTH_QQC[di, ii]  = float(linespt[8])
            self.OPERATION_QQC[di, ii]  = float(linespt[9])
            self.Q_SCORE[di, ii]  = float(linespt[10])
            self.CON_DTOP[di, ii]  = float(linespt[11])
            self.CON_DTOP_Z90[di, ii]  = float(linespt[12])
            self.CON_DTOP_Z180[di, ii]  = float(linespt[13])
            self.CON_DTOP_DA30[di, ii]  = float(linespt[14])
            self.CON_DTOP_DA90[di, ii]  = float(linespt[15])
            self.CON_DPR[di, ii]  = float(linespt[16])
            self.AI_DTOP[di, ii]  = float(linespt[17])
            self.AI_DTOP_Z90[di, ii]  = float(linespt[18])
            self.AI_DTOP_Z180[di, ii]  = float(linespt[19])
            self.AI_DTOP_DA30[di, ii]  = float(linespt[20])
            self.AI_DTOP_DA90[di, ii]  = float(linespt[21])
            self.AI_DPR[di, ii]  = float(linespt[22])
            self.QES[di, ii]  = float(linespt[23])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.CCR_Q[di] = self.CCR_Q[di - 1]
        self.TOE_TTM_STD[di] = self.TOE_TTM_STD[di - 1]
        self.CFP_TTM_STD[di] = self.CFP_TTM_STD[di - 1]
        self.GOVERNANCE[di] = self.GOVERNANCE[di - 1]
        self.PROFIT_QQC[di] = self.PROFIT_QQC[di - 1]
        self.GROWTH_QQC[di] = self.GROWTH_QQC[di - 1]
        self.OPERATION_QQC[di] = self.OPERATION_QQC[di - 1]
        self.Q_SCORE[di] = self.Q_SCORE[di - 1]
        self.CON_DTOP[di] = self.CON_DTOP[di - 1]
        self.CON_DTOP_Z90[di] = self.CON_DTOP_Z90[di - 1]
        self.CON_DTOP_Z180[di] = self.CON_DTOP_Z180[di - 1]
        self.CON_DTOP_DA30[di] = self.CON_DTOP_DA30[di - 1]
        self.CON_DTOP_DA90[di] = self.CON_DTOP_DA90[di - 1]
        self.CON_DPR[di] = self.CON_DPR[di - 1]
        self.AI_DTOP[di] = self.AI_DTOP[di - 1]
        self.AI_DTOP_Z90[di] = self.AI_DTOP_Z90[di - 1]
        self.AI_DTOP_Z180[di] = self.AI_DTOP_Z180[di - 1]
        self.AI_DTOP_DA30[di] = self.AI_DTOP_DA30[di - 1]
        self.AI_DTOP_DA90[di] = self.AI_DTOP_DA90[di - 1]
        self.AI_DPR[di] = self.AI_DPR[di - 1]
        self.QES[di] = self.QES[di - 1]