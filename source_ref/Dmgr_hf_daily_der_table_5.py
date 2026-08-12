
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrhf_daily_der_table_5(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.APB_1D = NIO_MATRIX()
        self.VWAP_1D = NIO_MATRIX()
        self.ARPP_1D = NIO_MATRIX()
        self.VOI = NIO_MATRIX()
        self.OIR = NIO_MATRIX()
        self.MPB = NIO_MATRIX()
        self.MCI_A = NIO_MATRIX()
        self.MCI_B = NIO_MATRIX()
        self.MCI_IMB = NIO_MATRIX()
        self.MPC_MAX = NIO_MATRIX()
        self.MPC_SKEW = NIO_MATRIX()
        self.BUYSELL_SHEET = NIO_MATRIX()
        self.BUY_NUMBER = NIO_MATRIX()
        self.SELL_NUMBER = NIO_MATRIX()
        self.SELL_SUB_BUY = NIO_MATRIX()
        self.SELL_PLUS_BUY = NIO_MATRIX()
        self.WEIGHTED_PRICE = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.APB_1D,self.tag + '.APB_1D')
        self.addDailyData(self.VWAP_1D,self.tag + '.VWAP_1D')
        self.addDailyData(self.ARPP_1D,self.tag + '.ARPP_1D')
        self.addDailyData(self.VOI,self.tag + '.VOI')
        self.addDailyData(self.OIR,self.tag + '.OIR')
        self.addDailyData(self.MPB,self.tag + '.MPB')
        self.addDailyData(self.MCI_A,self.tag + '.MCI_A')
        self.addDailyData(self.MCI_B,self.tag + '.MCI_B')
        self.addDailyData(self.MCI_IMB,self.tag + '.MCI_IMB')
        self.addDailyData(self.MPC_MAX,self.tag + '.MPC_MAX')
        self.addDailyData(self.MPC_SKEW,self.tag + '.MPC_SKEW')
        self.addDailyData(self.BUYSELL_SHEET,self.tag + '.BUYSELL_SHEET')
        self.addDailyData(self.BUY_NUMBER,self.tag + '.BUY_NUMBER')
        self.addDailyData(self.SELL_NUMBER,self.tag + '.SELL_NUMBER')
        self.addDailyData(self.SELL_SUB_BUY,self.tag + '.SELL_SUB_BUY')
        self.addDailyData(self.SELL_PLUS_BUY,self.tag + '.SELL_PLUS_BUY')
        self.addDailyData(self.WEIGHTED_PRICE,self.tag + '.WEIGHTED_PRICE')
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
            self.APB_1D[di, ii]  = float(linespt[3])
            self.VWAP_1D[di, ii]  = float(linespt[4])
            self.ARPP_1D[di, ii]  = float(linespt[5])
            self.VOI[di, ii]  = float(linespt[6])
            self.OIR[di, ii]  = float(linespt[7])
            self.MPB[di, ii]  = float(linespt[8])
            self.MCI_A[di, ii]  = float(linespt[9])
            self.MCI_B[di, ii]  = float(linespt[10])
            self.MCI_IMB[di, ii]  = float(linespt[11])
            self.MPC_MAX[di, ii]  = float(linespt[12])
            self.MPC_SKEW[di, ii]  = float(linespt[13])
            self.BUYSELL_SHEET[di, ii]  = float(linespt[14])
            self.BUY_NUMBER[di, ii]  = float(linespt[15])
            self.SELL_NUMBER[di, ii]  = float(linespt[16])
            self.SELL_SUB_BUY[di, ii]  = float(linespt[17])
            self.SELL_PLUS_BUY[di, ii]  = float(linespt[18])
            self.WEIGHTED_PRICE[di, ii]  = float(linespt[19])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.APB_1D[di] = self.APB_1D[di - 1]
        self.VWAP_1D[di] = self.VWAP_1D[di - 1]
        self.ARPP_1D[di] = self.ARPP_1D[di - 1]
        self.VOI[di] = self.VOI[di - 1]
        self.OIR[di] = self.OIR[di - 1]
        self.MPB[di] = self.MPB[di - 1]
        self.MCI_A[di] = self.MCI_A[di - 1]
        self.MCI_B[di] = self.MCI_B[di - 1]
        self.MCI_IMB[di] = self.MCI_IMB[di - 1]
        self.MPC_MAX[di] = self.MPC_MAX[di - 1]
        self.MPC_SKEW[di] = self.MPC_SKEW[di - 1]
        self.BUYSELL_SHEET[di] = self.BUYSELL_SHEET[di - 1]
        self.BUY_NUMBER[di] = self.BUY_NUMBER[di - 1]
        self.SELL_NUMBER[di] = self.SELL_NUMBER[di - 1]
        self.SELL_SUB_BUY[di] = self.SELL_SUB_BUY[di - 1]
        self.SELL_PLUS_BUY[di] = self.SELL_PLUS_BUY[di - 1]
        self.WEIGHTED_PRICE[di] = self.WEIGHTED_PRICE[di - 1]