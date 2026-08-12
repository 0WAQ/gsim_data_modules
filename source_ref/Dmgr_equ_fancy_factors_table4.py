
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrequ_fancy_factors_table4(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.FUND_TOP10_CHG_WEIGHT = NIO_MATRIX()
        self.FUND_TOP10_CHG_VALUERAITO = NIO_MATRIX()
        self.P_REPORT_DATE = NIO_MATRIX()
        self.P_REPORT_DIFF = NIO_MATRIX()
        self.HK_HOLDVOL_CHG_B20 = NIO_MATRIX()
        self.HK_HOLDVOL_CHG_C20 = NIO_MATRIX()
        self.HK_HOLDVOL_CHG_ALL20 = NIO_MATRIX()
        self.HK_HOLDVOL_CHG_B60 = NIO_MATRIX()
        self.HK_HOLDVOL_CHG_C60 = NIO_MATRIX()
        self.HK_HOLDVOL_CHG_ALL60 = NIO_MATRIX()
        self.HK_HOLDVOL_CHG_B120 = NIO_MATRIX()
        self.HK_HOLDVOL_CHG_C120 = NIO_MATRIX()
        self.HK_HOLDVOL_CHG_ALL120 = NIO_MATRIX()
        self.AI_DA_NP_30 = NIO_MATRIX()
        self.AI_DA_NP_60 = NIO_MATRIX()
        self.AI_DA_NP_90 = NIO_MATRIX()
        self.AI_DA_REV_30 = NIO_MATRIX()
        self.AI_DA_REV_60 = NIO_MATRIX()
        self.AI_DA_REV_90 = NIO_MATRIX()
        self.AI_DA_PE_30 = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.FUND_TOP10_CHG_WEIGHT,self.tag + '.FUND_TOP10_CHG_WEIGHT')
        self.addDailyData(self.FUND_TOP10_CHG_VALUERAITO,self.tag + '.FUND_TOP10_CHG_VALUERAITO')
        self.addDailyData(self.P_REPORT_DATE,self.tag + '.P_REPORT_DATE')
        self.addDailyData(self.P_REPORT_DIFF,self.tag + '.P_REPORT_DIFF')
        self.addDailyData(self.HK_HOLDVOL_CHG_B20,self.tag + '.HK_HOLDVOL_CHG_B20')
        self.addDailyData(self.HK_HOLDVOL_CHG_C20,self.tag + '.HK_HOLDVOL_CHG_C20')
        self.addDailyData(self.HK_HOLDVOL_CHG_ALL20,self.tag + '.HK_HOLDVOL_CHG_ALL20')
        self.addDailyData(self.HK_HOLDVOL_CHG_B60,self.tag + '.HK_HOLDVOL_CHG_B60')
        self.addDailyData(self.HK_HOLDVOL_CHG_C60,self.tag + '.HK_HOLDVOL_CHG_C60')
        self.addDailyData(self.HK_HOLDVOL_CHG_ALL60,self.tag + '.HK_HOLDVOL_CHG_ALL60')
        self.addDailyData(self.HK_HOLDVOL_CHG_B120,self.tag + '.HK_HOLDVOL_CHG_B120')
        self.addDailyData(self.HK_HOLDVOL_CHG_C120,self.tag + '.HK_HOLDVOL_CHG_C120')
        self.addDailyData(self.HK_HOLDVOL_CHG_ALL120,self.tag + '.HK_HOLDVOL_CHG_ALL120')
        self.addDailyData(self.AI_DA_NP_30,self.tag + '.AI_DA_NP_30')
        self.addDailyData(self.AI_DA_NP_60,self.tag + '.AI_DA_NP_60')
        self.addDailyData(self.AI_DA_NP_90,self.tag + '.AI_DA_NP_90')
        self.addDailyData(self.AI_DA_REV_30,self.tag + '.AI_DA_REV_30')
        self.addDailyData(self.AI_DA_REV_60,self.tag + '.AI_DA_REV_60')
        self.addDailyData(self.AI_DA_REV_90,self.tag + '.AI_DA_REV_90')
        self.addDailyData(self.AI_DA_PE_30,self.tag + '.AI_DA_PE_30')
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
            self.FUND_TOP10_CHG_WEIGHT[di, ii]  = float(linespt[3])
            self.FUND_TOP10_CHG_VALUERAITO[di, ii]  = float(linespt[4])
            self.P_REPORT_DATE[di, ii]  = float(linespt[5])
            self.P_REPORT_DIFF[di, ii]  = float(linespt[6])
            self.HK_HOLDVOL_CHG_B20[di, ii]  = float(linespt[7])
            self.HK_HOLDVOL_CHG_C20[di, ii]  = float(linespt[8])
            self.HK_HOLDVOL_CHG_ALL20[di, ii]  = float(linespt[9])
            self.HK_HOLDVOL_CHG_B60[di, ii]  = float(linespt[10])
            self.HK_HOLDVOL_CHG_C60[di, ii]  = float(linespt[11])
            self.HK_HOLDVOL_CHG_ALL60[di, ii]  = float(linespt[12])
            self.HK_HOLDVOL_CHG_B120[di, ii]  = float(linespt[13])
            self.HK_HOLDVOL_CHG_C120[di, ii]  = float(linespt[14])
            self.HK_HOLDVOL_CHG_ALL120[di, ii]  = float(linespt[15])
            self.AI_DA_NP_30[di, ii]  = float(linespt[16])
            self.AI_DA_NP_60[di, ii]  = float(linespt[17])
            self.AI_DA_NP_90[di, ii]  = float(linespt[18])
            self.AI_DA_REV_30[di, ii]  = float(linespt[19])
            self.AI_DA_REV_60[di, ii]  = float(linespt[20])
            self.AI_DA_REV_90[di, ii]  = float(linespt[21])
            self.AI_DA_PE_30[di, ii]  = float(linespt[22])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.FUND_TOP10_CHG_WEIGHT[di] = self.FUND_TOP10_CHG_WEIGHT[di - 1]
        self.FUND_TOP10_CHG_VALUERAITO[di] = self.FUND_TOP10_CHG_VALUERAITO[di - 1]
        self.P_REPORT_DATE[di] = self.P_REPORT_DATE[di - 1]
        self.P_REPORT_DIFF[di] = self.P_REPORT_DIFF[di - 1]
        self.HK_HOLDVOL_CHG_B20[di] = self.HK_HOLDVOL_CHG_B20[di - 1]
        self.HK_HOLDVOL_CHG_C20[di] = self.HK_HOLDVOL_CHG_C20[di - 1]
        self.HK_HOLDVOL_CHG_ALL20[di] = self.HK_HOLDVOL_CHG_ALL20[di - 1]
        self.HK_HOLDVOL_CHG_B60[di] = self.HK_HOLDVOL_CHG_B60[di - 1]
        self.HK_HOLDVOL_CHG_C60[di] = self.HK_HOLDVOL_CHG_C60[di - 1]
        self.HK_HOLDVOL_CHG_ALL60[di] = self.HK_HOLDVOL_CHG_ALL60[di - 1]
        self.HK_HOLDVOL_CHG_B120[di] = self.HK_HOLDVOL_CHG_B120[di - 1]
        self.HK_HOLDVOL_CHG_C120[di] = self.HK_HOLDVOL_CHG_C120[di - 1]
        self.HK_HOLDVOL_CHG_ALL120[di] = self.HK_HOLDVOL_CHG_ALL120[di - 1]
        self.AI_DA_NP_30[di] = self.AI_DA_NP_30[di - 1]
        self.AI_DA_NP_60[di] = self.AI_DA_NP_60[di - 1]
        self.AI_DA_NP_90[di] = self.AI_DA_NP_90[di - 1]
        self.AI_DA_REV_30[di] = self.AI_DA_REV_30[di - 1]
        self.AI_DA_REV_60[di] = self.AI_DA_REV_60[di - 1]
        self.AI_DA_REV_90[di] = self.AI_DA_REV_90[di - 1]
        self.AI_DA_PE_30[di] = self.AI_DA_PE_30[di - 1]