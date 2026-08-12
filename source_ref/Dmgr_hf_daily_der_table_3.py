
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrhf_daily_der_table_3(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.APT_INFLOW_RATIO = NIO_MATRIX()
        self.APT_OUTFLOW_RATIO = NIO_MATRIX()
        self.APT_NET_INFLOW_RATIO = NIO_MATRIX()
        self.NET_INFLOW_L_RATIO = NIO_MATRIX()
        self.MOM_L = NIO_MATRIX()
        self.NET_INFLOW_L_RATIO_L = NIO_MATRIX()
        self.MOM_L_LARGE_ORDER = NIO_MATRIX()
        self.GAMMA_BIAS = NIO_MATRIX()
        self.ACTIVE_SELL_OPEN = NIO_MATRIX()
        self.ACTIVE_BUY_CLOSE = NIO_MATRIX()
        self.INTENT_RATIO_OPEN = NIO_MATRIX()
        self.INTENT_INT_OPEN = NIO_MATRIX()
        self.NET_ACTIVE_INT_OPEN = NIO_MATRIX()
        self.BUY_RATIO_L_TRANS_O = NIO_MATRIX()
        self.NET_BUY_RATIO_L_TRANS_O = NIO_MATRIX()
        self.INTENT_INT_TRANS_O = NIO_MATRIX()
        self.NET_ACTIVE_INT_TRANS_O = NIO_MATRIX()
        self.OPEN_COM_MEAN = NIO_MATRIX()
        self.AFTERNOON_COM_STD = NIO_MATRIX()
        self.OPEN_COM_SKEWNESS = NIO_MATRIX()
        self.CLOSE_COM_CORR = NIO_MATRIX()
        self.ACTIVE_NET_BUY_INT_OPEN = NIO_MATRIX()
        self.ACTIVE_NET_BUY_INT_INTRA = NIO_MATRIX()
        self.ACTIVE_BUY_RATIO_INTRA = NIO_MATRIX()
        self.APT_EIGHTY = NIO_MATRIX()
        self.BEHAVIOR_SENTIMENT = NIO_MATRIX()
        self.PRESSURE = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.APT_INFLOW_RATIO,self.tag + '.APT_INFLOW_RATIO')
        self.addDailyData(self.APT_OUTFLOW_RATIO,self.tag + '.APT_OUTFLOW_RATIO')
        self.addDailyData(self.APT_NET_INFLOW_RATIO,self.tag + '.APT_NET_INFLOW_RATIO')
        self.addDailyData(self.NET_INFLOW_L_RATIO,self.tag + '.NET_INFLOW_L_RATIO')
        self.addDailyData(self.MOM_L,self.tag + '.MOM_L')
        self.addDailyData(self.NET_INFLOW_L_RATIO_L,self.tag + '.NET_INFLOW_L_RATIO_L')
        self.addDailyData(self.MOM_L_LARGE_ORDER,self.tag + '.MOM_L_LARGE_ORDER')
        self.addDailyData(self.GAMMA_BIAS,self.tag + '.GAMMA_BIAS')
        self.addDailyData(self.ACTIVE_SELL_OPEN,self.tag + '.ACTIVE_SELL_OPEN')
        self.addDailyData(self.ACTIVE_BUY_CLOSE,self.tag + '.ACTIVE_BUY_CLOSE')
        self.addDailyData(self.INTENT_RATIO_OPEN,self.tag + '.INTENT_RATIO_OPEN')
        self.addDailyData(self.INTENT_INT_OPEN,self.tag + '.INTENT_INT_OPEN')
        self.addDailyData(self.NET_ACTIVE_INT_OPEN,self.tag + '.NET_ACTIVE_INT_OPEN')
        self.addDailyData(self.BUY_RATIO_L_TRANS_O,self.tag + '.BUY_RATIO_L_TRANS_O')
        self.addDailyData(self.NET_BUY_RATIO_L_TRANS_O,self.tag + '.NET_BUY_RATIO_L_TRANS_O')
        self.addDailyData(self.INTENT_INT_TRANS_O,self.tag + '.INTENT_INT_TRANS_O')
        self.addDailyData(self.NET_ACTIVE_INT_TRANS_O,self.tag + '.NET_ACTIVE_INT_TRANS_O')
        self.addDailyData(self.OPEN_COM_MEAN,self.tag + '.OPEN_COM_MEAN')
        self.addDailyData(self.AFTERNOON_COM_STD,self.tag + '.AFTERNOON_COM_STD')
        self.addDailyData(self.OPEN_COM_SKEWNESS,self.tag + '.OPEN_COM_SKEWNESS')
        self.addDailyData(self.CLOSE_COM_CORR,self.tag + '.CLOSE_COM_CORR')
        self.addDailyData(self.ACTIVE_NET_BUY_INT_OPEN,self.tag + '.ACTIVE_NET_BUY_INT_OPEN')
        self.addDailyData(self.ACTIVE_NET_BUY_INT_INTRA,self.tag + '.ACTIVE_NET_BUY_INT_INTRA')
        self.addDailyData(self.ACTIVE_BUY_RATIO_INTRA,self.tag + '.ACTIVE_BUY_RATIO_INTRA')
        self.addDailyData(self.APT_EIGHTY,self.tag + '.APT_EIGHTY')
        self.addDailyData(self.BEHAVIOR_SENTIMENT,self.tag + '.BEHAVIOR_SENTIMENT')
        self.addDailyData(self.PRESSURE,self.tag + '.PRESSURE')
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
            self.APT_INFLOW_RATIO[di, ii]  = float(linespt[3])
            self.APT_OUTFLOW_RATIO[di, ii]  = float(linespt[4])
            self.APT_NET_INFLOW_RATIO[di, ii]  = float(linespt[5])
            self.NET_INFLOW_L_RATIO[di, ii]  = float(linespt[6])
            self.MOM_L[di, ii]  = float(linespt[7])
            self.NET_INFLOW_L_RATIO_L[di, ii]  = float(linespt[8])
            self.MOM_L_LARGE_ORDER[di, ii]  = float(linespt[9])
            self.GAMMA_BIAS[di, ii]  = float(linespt[10])
            self.ACTIVE_SELL_OPEN[di, ii]  = float(linespt[11])
            self.ACTIVE_BUY_CLOSE[di, ii]  = float(linespt[12])
            self.INTENT_RATIO_OPEN[di, ii]  = float(linespt[13])
            self.INTENT_INT_OPEN[di, ii]  = float(linespt[14])
            self.NET_ACTIVE_INT_OPEN[di, ii]  = float(linespt[15])
            self.BUY_RATIO_L_TRANS_O[di, ii]  = float(linespt[16])
            self.NET_BUY_RATIO_L_TRANS_O[di, ii]  = float(linespt[17])
            self.INTENT_INT_TRANS_O[di, ii]  = float(linespt[18])
            self.NET_ACTIVE_INT_TRANS_O[di, ii]  = float(linespt[19])
            self.OPEN_COM_MEAN[di, ii]  = float(linespt[20])
            self.AFTERNOON_COM_STD[di, ii]  = float(linespt[21])
            self.OPEN_COM_SKEWNESS[di, ii]  = float(linespt[22])
            self.CLOSE_COM_CORR[di, ii]  = float(linespt[23])
            self.ACTIVE_NET_BUY_INT_OPEN[di, ii]  = float(linespt[24])
            self.ACTIVE_NET_BUY_INT_INTRA[di, ii]  = float(linespt[25])
            self.ACTIVE_BUY_RATIO_INTRA[di, ii]  = float(linespt[26])
            self.APT_EIGHTY[di, ii]  = float(linespt[27])
            self.BEHAVIOR_SENTIMENT[di, ii]  = float(linespt[28])
            self.PRESSURE[di, ii]  = float(linespt[29])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.APT_INFLOW_RATIO[di] = self.APT_INFLOW_RATIO[di - 1]
        self.APT_OUTFLOW_RATIO[di] = self.APT_OUTFLOW_RATIO[di - 1]
        self.APT_NET_INFLOW_RATIO[di] = self.APT_NET_INFLOW_RATIO[di - 1]
        self.NET_INFLOW_L_RATIO[di] = self.NET_INFLOW_L_RATIO[di - 1]
        self.MOM_L[di] = self.MOM_L[di - 1]
        self.NET_INFLOW_L_RATIO_L[di] = self.NET_INFLOW_L_RATIO_L[di - 1]
        self.MOM_L_LARGE_ORDER[di] = self.MOM_L_LARGE_ORDER[di - 1]
        self.GAMMA_BIAS[di] = self.GAMMA_BIAS[di - 1]
        self.ACTIVE_SELL_OPEN[di] = self.ACTIVE_SELL_OPEN[di - 1]
        self.ACTIVE_BUY_CLOSE[di] = self.ACTIVE_BUY_CLOSE[di - 1]
        self.INTENT_RATIO_OPEN[di] = self.INTENT_RATIO_OPEN[di - 1]
        self.INTENT_INT_OPEN[di] = self.INTENT_INT_OPEN[di - 1]
        self.NET_ACTIVE_INT_OPEN[di] = self.NET_ACTIVE_INT_OPEN[di - 1]
        self.BUY_RATIO_L_TRANS_O[di] = self.BUY_RATIO_L_TRANS_O[di - 1]
        self.NET_BUY_RATIO_L_TRANS_O[di] = self.NET_BUY_RATIO_L_TRANS_O[di - 1]
        self.INTENT_INT_TRANS_O[di] = self.INTENT_INT_TRANS_O[di - 1]
        self.NET_ACTIVE_INT_TRANS_O[di] = self.NET_ACTIVE_INT_TRANS_O[di - 1]
        self.OPEN_COM_MEAN[di] = self.OPEN_COM_MEAN[di - 1]
        self.AFTERNOON_COM_STD[di] = self.AFTERNOON_COM_STD[di - 1]
        self.OPEN_COM_SKEWNESS[di] = self.OPEN_COM_SKEWNESS[di - 1]
        self.CLOSE_COM_CORR[di] = self.CLOSE_COM_CORR[di - 1]
        self.ACTIVE_NET_BUY_INT_OPEN[di] = self.ACTIVE_NET_BUY_INT_OPEN[di - 1]
        self.ACTIVE_NET_BUY_INT_INTRA[di] = self.ACTIVE_NET_BUY_INT_INTRA[di - 1]
        self.ACTIVE_BUY_RATIO_INTRA[di] = self.ACTIVE_BUY_RATIO_INTRA[di - 1]
        self.APT_EIGHTY[di] = self.APT_EIGHTY[di - 1]
        self.BEHAVIOR_SENTIMENT[di] = self.BEHAVIOR_SENTIMENT[di - 1]
        self.PRESSURE[di] = self.PRESSURE[di - 1]