
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrequ_fancy_factors_table3(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.AI_ETOP_Z90 = NIO_MATRIX()
        self.AI_ETOP_Z180 = NIO_MATRIX()
        self.CON_DA_PE_20 = NIO_MATRIX()
        self.CON_DA_PE_40 = NIO_MATRIX()
        self.CON_DA_PE_60 = NIO_MATRIX()
        self.CON_DA_PS_20 = NIO_MATRIX()
        self.CON_DA_PS_40 = NIO_MATRIX()
        self.CON_DA_PS_60 = NIO_MATRIX()
        self.AST_DA12_ETOP = NIO_MATRIX()
        self.AST_RANK_UPPCT = NIO_MATRIX()
        self.AST_PROFIT_UPPCT = NIO_MATRIX()
        self.GSA = NIO_MATRIX()
        self.HK_HOLDRATIO_ALL = NIO_MATRIX()
        self.HK_HOLDRATIO_B = NIO_MATRIX()
        self.HK_HOLDRATIO_C = NIO_MATRIX()
        self.FUND_TOP10_COUNT = NIO_MATRIX()
        self.FUND_TOP10_WEIGHT_MEAN = NIO_MATRIX()
        self.FUND_TOP10_WEIGHT_MAX = NIO_MATRIX()
        self.FUND_TOP10_NEGVALUE_PCT = NIO_MATRIX()
        self.NAIVE_WEIGHT_CHANGE_ASYM = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.AI_ETOP_Z90,self.tag + '.AI_ETOP_Z90')
        self.addDailyData(self.AI_ETOP_Z180,self.tag + '.AI_ETOP_Z180')
        self.addDailyData(self.CON_DA_PE_20,self.tag + '.CON_DA_PE_20')
        self.addDailyData(self.CON_DA_PE_40,self.tag + '.CON_DA_PE_40')
        self.addDailyData(self.CON_DA_PE_60,self.tag + '.CON_DA_PE_60')
        self.addDailyData(self.CON_DA_PS_20,self.tag + '.CON_DA_PS_20')
        self.addDailyData(self.CON_DA_PS_40,self.tag + '.CON_DA_PS_40')
        self.addDailyData(self.CON_DA_PS_60,self.tag + '.CON_DA_PS_60')
        self.addDailyData(self.AST_DA12_ETOP,self.tag + '.AST_DA12_ETOP')
        self.addDailyData(self.AST_RANK_UPPCT,self.tag + '.AST_RANK_UPPCT')
        self.addDailyData(self.AST_PROFIT_UPPCT,self.tag + '.AST_PROFIT_UPPCT')
        self.addDailyData(self.GSA,self.tag + '.GSA')
        self.addDailyData(self.HK_HOLDRATIO_ALL,self.tag + '.HK_HOLDRATIO_ALL')
        self.addDailyData(self.HK_HOLDRATIO_B,self.tag + '.HK_HOLDRATIO_B')
        self.addDailyData(self.HK_HOLDRATIO_C,self.tag + '.HK_HOLDRATIO_C')
        self.addDailyData(self.FUND_TOP10_COUNT,self.tag + '.FUND_TOP10_COUNT')
        self.addDailyData(self.FUND_TOP10_WEIGHT_MEAN,self.tag + '.FUND_TOP10_WEIGHT_MEAN')
        self.addDailyData(self.FUND_TOP10_WEIGHT_MAX,self.tag + '.FUND_TOP10_WEIGHT_MAX')
        self.addDailyData(self.FUND_TOP10_NEGVALUE_PCT,self.tag + '.FUND_TOP10_NEGVALUE_PCT')
        self.addDailyData(self.NAIVE_WEIGHT_CHANGE_ASYM,self.tag + '.NAIVE_WEIGHT_CHANGE_ASYM')
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
            self.AI_ETOP_Z90[di, ii]  = float(linespt[3])
            self.AI_ETOP_Z180[di, ii]  = float(linespt[4])
            self.CON_DA_PE_20[di, ii]  = float(linespt[5])
            self.CON_DA_PE_40[di, ii]  = float(linespt[6])
            self.CON_DA_PE_60[di, ii]  = float(linespt[7])
            self.CON_DA_PS_20[di, ii]  = float(linespt[8])
            self.CON_DA_PS_40[di, ii]  = float(linespt[9])
            self.CON_DA_PS_60[di, ii]  = float(linespt[10])
            self.AST_DA12_ETOP[di, ii]  = float(linespt[11])
            self.AST_RANK_UPPCT[di, ii]  = float(linespt[12])
            self.AST_PROFIT_UPPCT[di, ii]  = float(linespt[13])
            self.GSA[di, ii]  = float(linespt[14])
            self.HK_HOLDRATIO_ALL[di, ii]  = float(linespt[15])
            self.HK_HOLDRATIO_B[di, ii]  = float(linespt[16])
            self.HK_HOLDRATIO_C[di, ii]  = float(linespt[17])
            self.FUND_TOP10_COUNT[di, ii]  = float(linespt[18])
            self.FUND_TOP10_WEIGHT_MEAN[di, ii]  = float(linespt[19])
            self.FUND_TOP10_WEIGHT_MAX[di, ii]  = float(linespt[20])
            self.FUND_TOP10_NEGVALUE_PCT[di, ii]  = float(linespt[21])
            self.NAIVE_WEIGHT_CHANGE_ASYM[di, ii]  = float(linespt[22])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.AI_ETOP_Z90[di] = self.AI_ETOP_Z90[di - 1]
        self.AI_ETOP_Z180[di] = self.AI_ETOP_Z180[di - 1]
        self.CON_DA_PE_20[di] = self.CON_DA_PE_20[di - 1]
        self.CON_DA_PE_40[di] = self.CON_DA_PE_40[di - 1]
        self.CON_DA_PE_60[di] = self.CON_DA_PE_60[di - 1]
        self.CON_DA_PS_20[di] = self.CON_DA_PS_20[di - 1]
        self.CON_DA_PS_40[di] = self.CON_DA_PS_40[di - 1]
        self.CON_DA_PS_60[di] = self.CON_DA_PS_60[di - 1]
        self.AST_DA12_ETOP[di] = self.AST_DA12_ETOP[di - 1]
        self.AST_RANK_UPPCT[di] = self.AST_RANK_UPPCT[di - 1]
        self.AST_PROFIT_UPPCT[di] = self.AST_PROFIT_UPPCT[di - 1]
        self.GSA[di] = self.GSA[di - 1]
        self.HK_HOLDRATIO_ALL[di] = self.HK_HOLDRATIO_ALL[di - 1]
        self.HK_HOLDRATIO_B[di] = self.HK_HOLDRATIO_B[di - 1]
        self.HK_HOLDRATIO_C[di] = self.HK_HOLDRATIO_C[di - 1]
        self.FUND_TOP10_COUNT[di] = self.FUND_TOP10_COUNT[di - 1]
        self.FUND_TOP10_WEIGHT_MEAN[di] = self.FUND_TOP10_WEIGHT_MEAN[di - 1]
        self.FUND_TOP10_WEIGHT_MAX[di] = self.FUND_TOP10_WEIGHT_MAX[di - 1]
        self.FUND_TOP10_NEGVALUE_PCT[di] = self.FUND_TOP10_NEGVALUE_PCT[di - 1]
        self.NAIVE_WEIGHT_CHANGE_ASYM[di] = self.NAIVE_WEIGHT_CHANGE_ASYM[di - 1]