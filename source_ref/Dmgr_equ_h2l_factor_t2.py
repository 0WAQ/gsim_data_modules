
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrequ_h2l_factor_t2(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.DVN_DVN_CORR = NIO_MATRIX()
        self.DVN_DVP_CORR = NIO_MATRIX()
        self.DVN_V_CORR = NIO_MATRIX()
        self.DVP_DPN_CORR = NIO_MATRIX()
        self.DVP_DPP_CORR = NIO_MATRIX()
        self.DVP_DVN_CORR = NIO_MATRIX()
        self.DVP_DVP_CORR = NIO_MATRIX()
        self.DVP_V_CORR = NIO_MATRIX()
        self.PV_CORR = NIO_MATRIX()
        self.RV_CORR = NIO_MATRIX()
        self.V_AR_CORR = NIO_MATRIX()
        self.VWCE = NIO_MATRIX()
        self.VWCR = NIO_MATRIX()
        self.VWCS = NIO_MATRIX()
        self.BUY_ILLIQ = NIO_MATRIX()
        self.ILLIQ = NIO_MATRIX()
        self.RESILIENCY = NIO_MATRIX()
        self.SELL_ILLIQ = NIO_MATRIX()
        self.TR_0H = NIO_MATRIX()
        self.TR_1H = NIO_MATRIX()
        self.TR_2H = NIO_MATRIX()
        self.TR_3H = NIO_MATRIX()
        self.TR_4H = NIO_MATRIX()
        self.TR_PURE_0H = NIO_MATRIX()
        self.TR_PURE_1H = NIO_MATRIX()
        self.TR_PURE_2H = NIO_MATRIX()
        self.TR_PURE_3H = NIO_MATRIX()
        self.TR_PURE_4H = NIO_MATRIX()
        self.TR_PURE_REFORM = NIO_MATRIX()
        self.APT_INFLOW_RATIO = NIO_MATRIX()
        self.APT_NET_INFLOW_RATIO = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.DVN_DVN_CORR,self.tag + '.DVN_DVN_CORR')
        self.addDailyData(self.DVN_DVP_CORR,self.tag + '.DVN_DVP_CORR')
        self.addDailyData(self.DVN_V_CORR,self.tag + '.DVN_V_CORR')
        self.addDailyData(self.DVP_DPN_CORR,self.tag + '.DVP_DPN_CORR')
        self.addDailyData(self.DVP_DPP_CORR,self.tag + '.DVP_DPP_CORR')
        self.addDailyData(self.DVP_DVN_CORR,self.tag + '.DVP_DVN_CORR')
        self.addDailyData(self.DVP_DVP_CORR,self.tag + '.DVP_DVP_CORR')
        self.addDailyData(self.DVP_V_CORR,self.tag + '.DVP_V_CORR')
        self.addDailyData(self.PV_CORR,self.tag + '.PV_CORR')
        self.addDailyData(self.RV_CORR,self.tag + '.RV_CORR')
        self.addDailyData(self.V_AR_CORR,self.tag + '.V_AR_CORR')
        self.addDailyData(self.VWCE,self.tag + '.VWCE')
        self.addDailyData(self.VWCR,self.tag + '.VWCR')
        self.addDailyData(self.VWCS,self.tag + '.VWCS')
        self.addDailyData(self.BUY_ILLIQ,self.tag + '.BUY_ILLIQ')
        self.addDailyData(self.ILLIQ,self.tag + '.ILLIQ')
        self.addDailyData(self.RESILIENCY,self.tag + '.RESILIENCY')
        self.addDailyData(self.SELL_ILLIQ,self.tag + '.SELL_ILLIQ')
        self.addDailyData(self.TR_0H,self.tag + '.TR_0H')
        self.addDailyData(self.TR_1H,self.tag + '.TR_1H')
        self.addDailyData(self.TR_2H,self.tag + '.TR_2H')
        self.addDailyData(self.TR_3H,self.tag + '.TR_3H')
        self.addDailyData(self.TR_4H,self.tag + '.TR_4H')
        self.addDailyData(self.TR_PURE_0H,self.tag + '.TR_PURE_0H')
        self.addDailyData(self.TR_PURE_1H,self.tag + '.TR_PURE_1H')
        self.addDailyData(self.TR_PURE_2H,self.tag + '.TR_PURE_2H')
        self.addDailyData(self.TR_PURE_3H,self.tag + '.TR_PURE_3H')
        self.addDailyData(self.TR_PURE_4H,self.tag + '.TR_PURE_4H')
        self.addDailyData(self.TR_PURE_REFORM,self.tag + '.TR_PURE_REFORM')
        self.addDailyData(self.APT_INFLOW_RATIO,self.tag + '.APT_INFLOW_RATIO')
        self.addDailyData(self.APT_NET_INFLOW_RATIO,self.tag + '.APT_NET_INFLOW_RATIO')
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
            self.DVN_DVN_CORR[di, ii]  = float(linespt[3])
            self.DVN_DVP_CORR[di, ii]  = float(linespt[4])
            self.DVN_V_CORR[di, ii]  = float(linespt[5])
            self.DVP_DPN_CORR[di, ii]  = float(linespt[6])
            self.DVP_DPP_CORR[di, ii]  = float(linespt[7])
            self.DVP_DVN_CORR[di, ii]  = float(linespt[8])
            self.DVP_DVP_CORR[di, ii]  = float(linespt[9])
            self.DVP_V_CORR[di, ii]  = float(linespt[10])
            self.PV_CORR[di, ii]  = float(linespt[11])
            self.RV_CORR[di, ii]  = float(linespt[12])
            self.V_AR_CORR[di, ii]  = float(linespt[13])
            self.VWCE[di, ii]  = float(linespt[14])
            self.VWCR[di, ii]  = float(linespt[15])
            self.VWCS[di, ii]  = float(linespt[16])
            self.BUY_ILLIQ[di, ii]  = float(linespt[17])
            self.ILLIQ[di, ii]  = float(linespt[18])
            self.RESILIENCY[di, ii]  = float(linespt[19])
            self.SELL_ILLIQ[di, ii]  = float(linespt[20])
            self.TR_0H[di, ii]  = float(linespt[21])
            self.TR_1H[di, ii]  = float(linespt[22])
            self.TR_2H[di, ii]  = float(linespt[23])
            self.TR_3H[di, ii]  = float(linespt[24])
            self.TR_4H[di, ii]  = float(linespt[25])
            self.TR_PURE_0H[di, ii]  = float(linespt[26])
            self.TR_PURE_1H[di, ii]  = float(linespt[27])
            self.TR_PURE_2H[di, ii]  = float(linespt[28])
            self.TR_PURE_3H[di, ii]  = float(linespt[29])
            self.TR_PURE_4H[di, ii]  = float(linespt[30])
            self.TR_PURE_REFORM[di, ii]  = float(linespt[31])
            self.APT_INFLOW_RATIO[di, ii]  = float(linespt[32])
            self.APT_NET_INFLOW_RATIO[di, ii]  = float(linespt[33])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.DVN_DVN_CORR[di] = self.DVN_DVN_CORR[di - 1]
        self.DVN_DVP_CORR[di] = self.DVN_DVP_CORR[di - 1]
        self.DVN_V_CORR[di] = self.DVN_V_CORR[di - 1]
        self.DVP_DPN_CORR[di] = self.DVP_DPN_CORR[di - 1]
        self.DVP_DPP_CORR[di] = self.DVP_DPP_CORR[di - 1]
        self.DVP_DVN_CORR[di] = self.DVP_DVN_CORR[di - 1]
        self.DVP_DVP_CORR[di] = self.DVP_DVP_CORR[di - 1]
        self.DVP_V_CORR[di] = self.DVP_V_CORR[di - 1]
        self.PV_CORR[di] = self.PV_CORR[di - 1]
        self.RV_CORR[di] = self.RV_CORR[di - 1]
        self.V_AR_CORR[di] = self.V_AR_CORR[di - 1]
        self.VWCE[di] = self.VWCE[di - 1]
        self.VWCR[di] = self.VWCR[di - 1]
        self.VWCS[di] = self.VWCS[di - 1]
        self.BUY_ILLIQ[di] = self.BUY_ILLIQ[di - 1]
        self.ILLIQ[di] = self.ILLIQ[di - 1]
        self.RESILIENCY[di] = self.RESILIENCY[di - 1]
        self.SELL_ILLIQ[di] = self.SELL_ILLIQ[di - 1]
        self.TR_0H[di] = self.TR_0H[di - 1]
        self.TR_1H[di] = self.TR_1H[di - 1]
        self.TR_2H[di] = self.TR_2H[di - 1]
        self.TR_3H[di] = self.TR_3H[di - 1]
        self.TR_4H[di] = self.TR_4H[di - 1]
        self.TR_PURE_0H[di] = self.TR_PURE_0H[di - 1]
        self.TR_PURE_1H[di] = self.TR_PURE_1H[di - 1]
        self.TR_PURE_2H[di] = self.TR_PURE_2H[di - 1]
        self.TR_PURE_3H[di] = self.TR_PURE_3H[di - 1]
        self.TR_PURE_4H[di] = self.TR_PURE_4H[di - 1]
        self.TR_PURE_REFORM[di] = self.TR_PURE_REFORM[di - 1]
        self.APT_INFLOW_RATIO[di] = self.APT_INFLOW_RATIO[di - 1]
        self.APT_NET_INFLOW_RATIO[di] = self.APT_NET_INFLOW_RATIO[di - 1]