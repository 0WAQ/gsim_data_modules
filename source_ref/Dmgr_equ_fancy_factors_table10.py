
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrequ_fancy_factors_table10(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.GR_PE_TTM = NIO_MATRIX()
        self.GR_PE_Q = NIO_MATRIX()
        self.GR_PB = NIO_MATRIX()
        self.GR_PCF_TTM = NIO_MATRIX()
        self.GR_PCF_Q = NIO_MATRIX()
        self.GR_PS_TTM = NIO_MATRIX()
        self.GR_PS_Q = NIO_MATRIX()
        self.DEP_ABR_RATIO = NIO_MATRIX()
        self.TRANS_RATIO = NIO_MATRIX()
        self.CREDIT_DEBT_RATIO = NIO_MATRIX()
        self.FOREX_RATIO = NIO_MATRIX()
        self.STATIC_NOTE_RATIO = NIO_MATRIX()
        self.ABS_GPG_Q = NIO_MATRIX()
        self.ABS_INVG = NIO_MATRIX()
        self.KCI = NIO_MATRIX()
        self.DTOA_YOYD = NIO_MATRIX()
        self.IT_Q_YOYD = NIO_MATRIX()
        self.IT_TTM_QOQD = NIO_MATRIX()
        self.ART_Q_YOYD = NIO_MATRIX()
        self.FAT_Q_YOYD = NIO_MATRIX()
        self.FAT_TTM_QOQD = NIO_MATRIX()
        self.OPER_L_YOY = NIO_MATRIX()
        self.OPER_L_QOQ = NIO_MATRIX()
        self.OPER_LR_YOYD = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.GR_PE_TTM,self.tag + '.GR_PE_TTM')
        self.addDailyData(self.GR_PE_Q,self.tag + '.GR_PE_Q')
        self.addDailyData(self.GR_PB,self.tag + '.GR_PB')
        self.addDailyData(self.GR_PCF_TTM,self.tag + '.GR_PCF_TTM')
        self.addDailyData(self.GR_PCF_Q,self.tag + '.GR_PCF_Q')
        self.addDailyData(self.GR_PS_TTM,self.tag + '.GR_PS_TTM')
        self.addDailyData(self.GR_PS_Q,self.tag + '.GR_PS_Q')
        self.addDailyData(self.DEP_ABR_RATIO,self.tag + '.DEP_ABR_RATIO')
        self.addDailyData(self.TRANS_RATIO,self.tag + '.TRANS_RATIO')
        self.addDailyData(self.CREDIT_DEBT_RATIO,self.tag + '.CREDIT_DEBT_RATIO')
        self.addDailyData(self.FOREX_RATIO,self.tag + '.FOREX_RATIO')
        self.addDailyData(self.STATIC_NOTE_RATIO,self.tag + '.STATIC_NOTE_RATIO')
        self.addDailyData(self.ABS_GPG_Q,self.tag + '.ABS_GPG_Q')
        self.addDailyData(self.ABS_INVG,self.tag + '.ABS_INVG')
        self.addDailyData(self.KCI,self.tag + '.KCI')
        self.addDailyData(self.DTOA_YOYD,self.tag + '.DTOA_YOYD')
        self.addDailyData(self.IT_Q_YOYD,self.tag + '.IT_Q_YOYD')
        self.addDailyData(self.IT_TTM_QOQD,self.tag + '.IT_TTM_QOQD')
        self.addDailyData(self.ART_Q_YOYD,self.tag + '.ART_Q_YOYD')
        self.addDailyData(self.FAT_Q_YOYD,self.tag + '.FAT_Q_YOYD')
        self.addDailyData(self.FAT_TTM_QOQD,self.tag + '.FAT_TTM_QOQD')
        self.addDailyData(self.OPER_L_YOY,self.tag + '.OPER_L_YOY')
        self.addDailyData(self.OPER_L_QOQ,self.tag + '.OPER_L_QOQ')
        self.addDailyData(self.OPER_LR_YOYD,self.tag + '.OPER_LR_YOYD')
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
            self.GR_PE_TTM[di, ii]  = float(linespt[3])
            self.GR_PE_Q[di, ii]  = float(linespt[4])
            self.GR_PB[di, ii]  = float(linespt[5])
            self.GR_PCF_TTM[di, ii]  = float(linespt[6])
            self.GR_PCF_Q[di, ii]  = float(linespt[7])
            self.GR_PS_TTM[di, ii]  = float(linespt[8])
            self.GR_PS_Q[di, ii]  = float(linespt[9])
            self.DEP_ABR_RATIO[di, ii]  = float(linespt[10])
            self.TRANS_RATIO[di, ii]  = float(linespt[11])
            self.CREDIT_DEBT_RATIO[di, ii]  = float(linespt[12])
            self.FOREX_RATIO[di, ii]  = float(linespt[13])
            self.STATIC_NOTE_RATIO[di, ii]  = float(linespt[14])
            self.ABS_GPG_Q[di, ii]  = float(linespt[15])
            self.ABS_INVG[di, ii]  = float(linespt[16])
            self.KCI[di, ii]  = float(linespt[17])
            self.DTOA_YOYD[di, ii]  = float(linespt[18])
            self.IT_Q_YOYD[di, ii]  = float(linespt[19])
            self.IT_TTM_QOQD[di, ii]  = float(linespt[20])
            self.ART_Q_YOYD[di, ii]  = float(linespt[21])
            self.FAT_Q_YOYD[di, ii]  = float(linespt[22])
            self.FAT_TTM_QOQD[di, ii]  = float(linespt[23])
            self.OPER_L_YOY[di, ii]  = float(linespt[24])
            self.OPER_L_QOQ[di, ii]  = float(linespt[25])
            self.OPER_LR_YOYD[di, ii]  = float(linespt[26])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.GR_PE_TTM[di] = self.GR_PE_TTM[di - 1]
        self.GR_PE_Q[di] = self.GR_PE_Q[di - 1]
        self.GR_PB[di] = self.GR_PB[di - 1]
        self.GR_PCF_TTM[di] = self.GR_PCF_TTM[di - 1]
        self.GR_PCF_Q[di] = self.GR_PCF_Q[di - 1]
        self.GR_PS_TTM[di] = self.GR_PS_TTM[di - 1]
        self.GR_PS_Q[di] = self.GR_PS_Q[di - 1]
        self.DEP_ABR_RATIO[di] = self.DEP_ABR_RATIO[di - 1]
        self.TRANS_RATIO[di] = self.TRANS_RATIO[di - 1]
        self.CREDIT_DEBT_RATIO[di] = self.CREDIT_DEBT_RATIO[di - 1]
        self.FOREX_RATIO[di] = self.FOREX_RATIO[di - 1]
        self.STATIC_NOTE_RATIO[di] = self.STATIC_NOTE_RATIO[di - 1]
        self.ABS_GPG_Q[di] = self.ABS_GPG_Q[di - 1]
        self.ABS_INVG[di] = self.ABS_INVG[di - 1]
        self.KCI[di] = self.KCI[di - 1]
        self.DTOA_YOYD[di] = self.DTOA_YOYD[di - 1]
        self.IT_Q_YOYD[di] = self.IT_Q_YOYD[di - 1]
        self.IT_TTM_QOQD[di] = self.IT_TTM_QOQD[di - 1]
        self.ART_Q_YOYD[di] = self.ART_Q_YOYD[di - 1]
        self.FAT_Q_YOYD[di] = self.FAT_Q_YOYD[di - 1]
        self.FAT_TTM_QOQD[di] = self.FAT_TTM_QOQD[di - 1]
        self.OPER_L_YOY[di] = self.OPER_L_YOY[di - 1]
        self.OPER_L_QOQ[di] = self.OPER_L_QOQ[di - 1]
        self.OPER_LR_YOYD[di] = self.OPER_LR_YOYD[di - 1]