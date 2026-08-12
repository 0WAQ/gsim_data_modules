
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrequ_fancy_factors_table7(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.FUND_TRACTION_20 = NIO_MATRIX()
        self.FUND_TRACTION_60 = NIO_MATRIX()
        self.SUR_EVENT = NIO_MATRIX()
        self.SUR_INST = NIO_MATRIX()
        self.GB_POST_NUM_30 = NIO_MATRIX()
        self.GB_POST_NUM_60 = NIO_MATRIX()
        self.GB_POST_NUM_90 = NIO_MATRIX()
        self.GB_POST_NUM_DA30 = NIO_MATRIX()
        self.T_ACCR_IS = NIO_MATRIX()
        self.D_ACCR_IS = NIO_MATRIX()
        self.T_ACCR_BS = NIO_MATRIX()
        self.D_ACCR_BS = NIO_MATRIX()
        self.NP_Q_ACC = NIO_MATRIX()
        self.REV_Q_ACC = NIO_MATRIX()
        self.NP_Q_SD = NIO_MATRIX()
        self.OP_Q_SD = NIO_MATRIX()
        self.REV_Q_SD = NIO_MATRIX()
        self.ROIC_Q = NIO_MATRIX()
        self.CFOA_Q = NIO_MATRIX()
        self.PROFIT_TREND = NIO_MATRIX()
        self.AT_TTM_QOQD = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.FUND_TRACTION_20,self.tag + '.FUND_TRACTION_20')
        self.addDailyData(self.FUND_TRACTION_60,self.tag + '.FUND_TRACTION_60')
        self.addDailyData(self.SUR_EVENT,self.tag + '.SUR_EVENT')
        self.addDailyData(self.SUR_INST,self.tag + '.SUR_INST')
        self.addDailyData(self.GB_POST_NUM_30,self.tag + '.GB_POST_NUM_30')
        self.addDailyData(self.GB_POST_NUM_60,self.tag + '.GB_POST_NUM_60')
        self.addDailyData(self.GB_POST_NUM_90,self.tag + '.GB_POST_NUM_90')
        self.addDailyData(self.GB_POST_NUM_DA30,self.tag + '.GB_POST_NUM_DA30')
        self.addDailyData(self.T_ACCR_IS,self.tag + '.T_ACCR_IS')
        self.addDailyData(self.D_ACCR_IS,self.tag + '.D_ACCR_IS')
        self.addDailyData(self.T_ACCR_BS,self.tag + '.T_ACCR_BS')
        self.addDailyData(self.D_ACCR_BS,self.tag + '.D_ACCR_BS')
        self.addDailyData(self.NP_Q_ACC,self.tag + '.NP_Q_ACC')
        self.addDailyData(self.REV_Q_ACC,self.tag + '.REV_Q_ACC')
        self.addDailyData(self.NP_Q_SD,self.tag + '.NP_Q_SD')
        self.addDailyData(self.OP_Q_SD,self.tag + '.OP_Q_SD')
        self.addDailyData(self.REV_Q_SD,self.tag + '.REV_Q_SD')
        self.addDailyData(self.ROIC_Q,self.tag + '.ROIC_Q')
        self.addDailyData(self.CFOA_Q,self.tag + '.CFOA_Q')
        self.addDailyData(self.PROFIT_TREND,self.tag + '.PROFIT_TREND')
        self.addDailyData(self.AT_TTM_QOQD,self.tag + '.AT_TTM_QOQD')
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
            self.FUND_TRACTION_20[di, ii]  = float(linespt[3])
            self.FUND_TRACTION_60[di, ii]  = float(linespt[4])
            self.SUR_EVENT[di, ii]  = float(linespt[5])
            self.SUR_INST[di, ii]  = float(linespt[6])
            self.GB_POST_NUM_30[di, ii]  = float(linespt[7])
            self.GB_POST_NUM_60[di, ii]  = float(linespt[8])
            self.GB_POST_NUM_90[di, ii]  = float(linespt[9])
            self.GB_POST_NUM_DA30[di, ii]  = float(linespt[10])
            self.T_ACCR_IS[di, ii]  = float(linespt[11])
            self.D_ACCR_IS[di, ii]  = float(linespt[12])
            self.T_ACCR_BS[di, ii]  = float(linespt[13])
            self.D_ACCR_BS[di, ii]  = float(linespt[14])
            self.NP_Q_ACC[di, ii]  = float(linespt[15])
            self.REV_Q_ACC[di, ii]  = float(linespt[16])
            self.NP_Q_SD[di, ii]  = float(linespt[17])
            self.OP_Q_SD[di, ii]  = float(linespt[18])
            self.REV_Q_SD[di, ii]  = float(linespt[19])
            self.ROIC_Q[di, ii]  = float(linespt[20])
            self.CFOA_Q[di, ii]  = float(linespt[21])
            self.PROFIT_TREND[di, ii]  = float(linespt[22])
            self.AT_TTM_QOQD[di, ii]  = float(linespt[23])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.FUND_TRACTION_20[di] = self.FUND_TRACTION_20[di - 1]
        self.FUND_TRACTION_60[di] = self.FUND_TRACTION_60[di - 1]
        self.SUR_EVENT[di] = self.SUR_EVENT[di - 1]
        self.SUR_INST[di] = self.SUR_INST[di - 1]
        self.GB_POST_NUM_30[di] = self.GB_POST_NUM_30[di - 1]
        self.GB_POST_NUM_60[di] = self.GB_POST_NUM_60[di - 1]
        self.GB_POST_NUM_90[di] = self.GB_POST_NUM_90[di - 1]
        self.GB_POST_NUM_DA30[di] = self.GB_POST_NUM_DA30[di - 1]
        self.T_ACCR_IS[di] = self.T_ACCR_IS[di - 1]
        self.D_ACCR_IS[di] = self.D_ACCR_IS[di - 1]
        self.T_ACCR_BS[di] = self.T_ACCR_BS[di - 1]
        self.D_ACCR_BS[di] = self.D_ACCR_BS[di - 1]
        self.NP_Q_ACC[di] = self.NP_Q_ACC[di - 1]
        self.REV_Q_ACC[di] = self.REV_Q_ACC[di - 1]
        self.NP_Q_SD[di] = self.NP_Q_SD[di - 1]
        self.OP_Q_SD[di] = self.OP_Q_SD[di - 1]
        self.REV_Q_SD[di] = self.REV_Q_SD[di - 1]
        self.ROIC_Q[di] = self.ROIC_Q[di - 1]
        self.CFOA_Q[di] = self.CFOA_Q[di - 1]
        self.PROFIT_TREND[di] = self.PROFIT_TREND[di - 1]
        self.AT_TTM_QOQD[di] = self.AT_TTM_QOQD[di - 1]