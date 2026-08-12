
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrhf_daily_der_table_7(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.VOLUME_RATIO = NIO_MATRIX()
        self.TCV = NIO_MATRIX()
        self.PCV = NIO_MATRIX()
        self.NCV = NIO_MATRIX()
        self.ECV = NIO_MATRIX()
        self.TCV_L = NIO_MATRIX()
        self.PCV_GE = NIO_MATRIX()
        self.NCV_GE = NIO_MATRIX()
        self.OCVP = NIO_MATRIX()
        self.BCVP = NIO_MATRIX()
        self.BCVP15MIN = NIO_MATRIX()
        self.OBCVP_ORI = NIO_MATRIX()
        self.VWPIN = NIO_MATRIX()
        self.NET_BUY_RATIO_L = NIO_MATRIX()
        self.ORDER_RATIO_L = NIO_MATRIX()
        self.SELL_RATIO_L = NIO_MATRIX()
        self.BUY_RATIO_L = NIO_MATRIX()
        self.BUY_CONCENTRATE = NIO_MATRIX()
        self.SELL_CONCENTRATE = NIO_MATRIX()
        self.NET_BUY_CONCENTRATE = NIO_MATRIX()
        self.ORDER_CONCENTRATE = NIO_MATRIX()
        self.OPEN_VOLUME_RATE = NIO_MATRIX()
        self.CLOSE_VOLUME_RATE = NIO_MATRIX()
        self.BUY_ACTIVE_RATE = NIO_MATRIX()
        self.SELL_ACTIVE_RATE = NIO_MATRIX()
        self.ACT = NIO_MATRIX()
        self.L_ACT = NIO_MATRIX()
        self.M_ACT = NIO_MATRIX()
        self.S_ACT = NIO_MATRIX()
        self.X_ACT = NIO_MATRIX()
        self.XLS_ORDER_RATIO = NIO_MATRIX()
        self.L_ORDER_RATIO = NIO_MATRIX()
        self.M_ORDER_RATIO = NIO_MATRIX()
        self.S_ORDER_RATIO = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.VOLUME_RATIO,self.tag + '.VOLUME_RATIO')
        self.addDailyData(self.TCV,self.tag + '.TCV')
        self.addDailyData(self.PCV,self.tag + '.PCV')
        self.addDailyData(self.NCV,self.tag + '.NCV')
        self.addDailyData(self.ECV,self.tag + '.ECV')
        self.addDailyData(self.TCV_L,self.tag + '.TCV_L')
        self.addDailyData(self.PCV_GE,self.tag + '.PCV_GE')
        self.addDailyData(self.NCV_GE,self.tag + '.NCV_GE')
        self.addDailyData(self.OCVP,self.tag + '.OCVP')
        self.addDailyData(self.BCVP,self.tag + '.BCVP')
        self.addDailyData(self.BCVP15MIN,self.tag + '.BCVP15MIN')
        self.addDailyData(self.OBCVP_ORI,self.tag + '.OBCVP_ORI')
        self.addDailyData(self.VWPIN,self.tag + '.VWPIN')
        self.addDailyData(self.NET_BUY_RATIO_L,self.tag + '.NET_BUY_RATIO_L')
        self.addDailyData(self.ORDER_RATIO_L,self.tag + '.ORDER_RATIO_L')
        self.addDailyData(self.SELL_RATIO_L,self.tag + '.SELL_RATIO_L')
        self.addDailyData(self.BUY_RATIO_L,self.tag + '.BUY_RATIO_L')
        self.addDailyData(self.BUY_CONCENTRATE,self.tag + '.BUY_CONCENTRATE')
        self.addDailyData(self.SELL_CONCENTRATE,self.tag + '.SELL_CONCENTRATE')
        self.addDailyData(self.NET_BUY_CONCENTRATE,self.tag + '.NET_BUY_CONCENTRATE')
        self.addDailyData(self.ORDER_CONCENTRATE,self.tag + '.ORDER_CONCENTRATE')
        self.addDailyData(self.OPEN_VOLUME_RATE,self.tag + '.OPEN_VOLUME_RATE')
        self.addDailyData(self.CLOSE_VOLUME_RATE,self.tag + '.CLOSE_VOLUME_RATE')
        self.addDailyData(self.BUY_ACTIVE_RATE,self.tag + '.BUY_ACTIVE_RATE')
        self.addDailyData(self.SELL_ACTIVE_RATE,self.tag + '.SELL_ACTIVE_RATE')
        self.addDailyData(self.ACT,self.tag + '.ACT')
        self.addDailyData(self.L_ACT,self.tag + '.L_ACT')
        self.addDailyData(self.M_ACT,self.tag + '.M_ACT')
        self.addDailyData(self.S_ACT,self.tag + '.S_ACT')
        self.addDailyData(self.X_ACT,self.tag + '.X_ACT')
        self.addDailyData(self.XLS_ORDER_RATIO,self.tag + '.XLS_ORDER_RATIO')
        self.addDailyData(self.L_ORDER_RATIO,self.tag + '.L_ORDER_RATIO')
        self.addDailyData(self.M_ORDER_RATIO,self.tag + '.M_ORDER_RATIO')
        self.addDailyData(self.S_ORDER_RATIO,self.tag + '.S_ORDER_RATIO')
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
            self.VOLUME_RATIO[di, ii]  = float(linespt[3])
            self.TCV[di, ii]  = float(linespt[4])
            self.PCV[di, ii]  = float(linespt[5])
            self.NCV[di, ii]  = float(linespt[6])
            self.ECV[di, ii]  = float(linespt[7])
            self.TCV_L[di, ii]  = float(linespt[8])
            self.PCV_GE[di, ii]  = float(linespt[9])
            self.NCV_GE[di, ii]  = float(linespt[10])
            self.OCVP[di, ii]  = float(linespt[11])
            self.BCVP[di, ii]  = float(linespt[12])
            self.BCVP15MIN[di, ii]  = float(linespt[13])
            self.OBCVP_ORI[di, ii]  = float(linespt[14])
            self.VWPIN[di, ii]  = float(linespt[15])
            self.NET_BUY_RATIO_L[di, ii]  = float(linespt[16])
            self.ORDER_RATIO_L[di, ii]  = float(linespt[17])
            self.SELL_RATIO_L[di, ii]  = float(linespt[18])
            self.BUY_RATIO_L[di, ii]  = float(linespt[19])
            self.BUY_CONCENTRATE[di, ii]  = float(linespt[20])
            self.SELL_CONCENTRATE[di, ii]  = float(linespt[21])
            self.NET_BUY_CONCENTRATE[di, ii]  = float(linespt[22])
            self.ORDER_CONCENTRATE[di, ii]  = float(linespt[23])
            self.OPEN_VOLUME_RATE[di, ii]  = float(linespt[24])
            self.CLOSE_VOLUME_RATE[di, ii]  = float(linespt[25])
            self.BUY_ACTIVE_RATE[di, ii]  = float(linespt[26])
            self.SELL_ACTIVE_RATE[di, ii]  = float(linespt[27])
            self.ACT[di, ii]  = float(linespt[28])
            self.L_ACT[di, ii]  = float(linespt[29])
            self.M_ACT[di, ii]  = float(linespt[30])
            self.S_ACT[di, ii]  = float(linespt[31])
            self.X_ACT[di, ii]  = float(linespt[32])
            self.XLS_ORDER_RATIO[di, ii]  = float(linespt[33])
            self.L_ORDER_RATIO[di, ii]  = float(linespt[34])
            self.M_ORDER_RATIO[di, ii]  = float(linespt[35])
            self.S_ORDER_RATIO[di, ii]  = float(linespt[36])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.VOLUME_RATIO[di] = self.VOLUME_RATIO[di - 1]
        self.TCV[di] = self.TCV[di - 1]
        self.PCV[di] = self.PCV[di - 1]
        self.NCV[di] = self.NCV[di - 1]
        self.ECV[di] = self.ECV[di - 1]
        self.TCV_L[di] = self.TCV_L[di - 1]
        self.PCV_GE[di] = self.PCV_GE[di - 1]
        self.NCV_GE[di] = self.NCV_GE[di - 1]
        self.OCVP[di] = self.OCVP[di - 1]
        self.BCVP[di] = self.BCVP[di - 1]
        self.BCVP15MIN[di] = self.BCVP15MIN[di - 1]
        self.OBCVP_ORI[di] = self.OBCVP_ORI[di - 1]
        self.VWPIN[di] = self.VWPIN[di - 1]
        self.NET_BUY_RATIO_L[di] = self.NET_BUY_RATIO_L[di - 1]
        self.ORDER_RATIO_L[di] = self.ORDER_RATIO_L[di - 1]
        self.SELL_RATIO_L[di] = self.SELL_RATIO_L[di - 1]
        self.BUY_RATIO_L[di] = self.BUY_RATIO_L[di - 1]
        self.BUY_CONCENTRATE[di] = self.BUY_CONCENTRATE[di - 1]
        self.SELL_CONCENTRATE[di] = self.SELL_CONCENTRATE[di - 1]
        self.NET_BUY_CONCENTRATE[di] = self.NET_BUY_CONCENTRATE[di - 1]
        self.ORDER_CONCENTRATE[di] = self.ORDER_CONCENTRATE[di - 1]
        self.OPEN_VOLUME_RATE[di] = self.OPEN_VOLUME_RATE[di - 1]
        self.CLOSE_VOLUME_RATE[di] = self.CLOSE_VOLUME_RATE[di - 1]
        self.BUY_ACTIVE_RATE[di] = self.BUY_ACTIVE_RATE[di - 1]
        self.SELL_ACTIVE_RATE[di] = self.SELL_ACTIVE_RATE[di - 1]
        self.ACT[di] = self.ACT[di - 1]
        self.L_ACT[di] = self.L_ACT[di - 1]
        self.M_ACT[di] = self.M_ACT[di - 1]
        self.S_ACT[di] = self.S_ACT[di - 1]
        self.X_ACT[di] = self.X_ACT[di - 1]
        self.XLS_ORDER_RATIO[di] = self.XLS_ORDER_RATIO[di - 1]
        self.L_ORDER_RATIO[di] = self.L_ORDER_RATIO[di - 1]
        self.M_ORDER_RATIO[di] = self.M_ORDER_RATIO[di - 1]
        self.S_ORDER_RATIO[di] = self.S_ORDER_RATIO[di - 1]