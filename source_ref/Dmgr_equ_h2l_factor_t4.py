
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrequ_h2l_factor_t4(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.RET_VOL_C = NIO_MATRIX()
        self.RET_VOL_W = NIO_MATRIX()
        self.REV_ENHANCE = NIO_MATRIX()
        self.GMM_DMEAN = NIO_MATRIX()
        self.GMM_MEAN = NIO_MATRIX()
        self.MIN_BETA = NIO_MATRIX()
        self.MIN_IRET_KURT_AVE = NIO_MATRIX()
        self.MIN_IRET_SKEW_AVE = NIO_MATRIX()
        self.MIN_RET_KURT_AVE = NIO_MATRIX()
        self.MIN_RET_SKEW_AVE = NIO_MATRIX()
        self.SMART_MONEY = NIO_MATRIX()
        self.MCI_A = NIO_MATRIX()
        self.MCI_B = NIO_MATRIX()
        self.MCI_IMB = NIO_MATRIX()
        self.MPB = NIO_MATRIX()
        self.MPC_MAX = NIO_MATRIX()
        self.MPC_SKEW = NIO_MATRIX()
        self.OIR = NIO_MATRIX()
        self.VOI = NIO_MATRIX()
        self.MINTVAL_MTE = NIO_MATRIX()
        self.MINTVAL_MTS = NIO_MATRIX()
        self.MINTVAL_QUA = NIO_MATRIX()
        self.MINTVAL_SKEW = NIO_MATRIX()
        self.INF_BUY_RATIO_CLOSE = NIO_MATRIX()
        self.INF_SELL_RATIO_OPEN = NIO_MATRIX()
        self.SECTVAL_KURT = NIO_MATRIX()
        self.BUY_INTENT_RATIO_OPEN = NIO_MATRIX()
        self.BUY_INTENT_POWER_OPEN = NIO_MATRIX()
        self.NET_BUY_POWER_OPEN = NIO_MATRIX()
        self.OVAL_MBSR = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.RET_VOL_C,self.tag + '.RET_VOL_C')
        self.addDailyData(self.RET_VOL_W,self.tag + '.RET_VOL_W')
        self.addDailyData(self.REV_ENHANCE,self.tag + '.REV_ENHANCE')
        self.addDailyData(self.GMM_DMEAN,self.tag + '.GMM_DMEAN')
        self.addDailyData(self.GMM_MEAN,self.tag + '.GMM_MEAN')
        self.addDailyData(self.MIN_BETA,self.tag + '.MIN_BETA')
        self.addDailyData(self.MIN_IRET_KURT_AVE,self.tag + '.MIN_IRET_KURT_AVE')
        self.addDailyData(self.MIN_IRET_SKEW_AVE,self.tag + '.MIN_IRET_SKEW_AVE')
        self.addDailyData(self.MIN_RET_KURT_AVE,self.tag + '.MIN_RET_KURT_AVE')
        self.addDailyData(self.MIN_RET_SKEW_AVE,self.tag + '.MIN_RET_SKEW_AVE')
        self.addDailyData(self.SMART_MONEY,self.tag + '.SMART_MONEY')
        self.addDailyData(self.MCI_A,self.tag + '.MCI_A')
        self.addDailyData(self.MCI_B,self.tag + '.MCI_B')
        self.addDailyData(self.MCI_IMB,self.tag + '.MCI_IMB')
        self.addDailyData(self.MPB,self.tag + '.MPB')
        self.addDailyData(self.MPC_MAX,self.tag + '.MPC_MAX')
        self.addDailyData(self.MPC_SKEW,self.tag + '.MPC_SKEW')
        self.addDailyData(self.OIR,self.tag + '.OIR')
        self.addDailyData(self.VOI,self.tag + '.VOI')
        self.addDailyData(self.MINTVAL_MTE,self.tag + '.MINTVAL_MTE')
        self.addDailyData(self.MINTVAL_MTS,self.tag + '.MINTVAL_MTS')
        self.addDailyData(self.MINTVAL_QUA,self.tag + '.MINTVAL_QUA')
        self.addDailyData(self.MINTVAL_SKEW,self.tag + '.MINTVAL_SKEW')
        self.addDailyData(self.INF_BUY_RATIO_CLOSE,self.tag + '.INF_BUY_RATIO_CLOSE')
        self.addDailyData(self.INF_SELL_RATIO_OPEN,self.tag + '.INF_SELL_RATIO_OPEN')
        self.addDailyData(self.SECTVAL_KURT,self.tag + '.SECTVAL_KURT')
        self.addDailyData(self.BUY_INTENT_RATIO_OPEN,self.tag + '.BUY_INTENT_RATIO_OPEN')
        self.addDailyData(self.BUY_INTENT_POWER_OPEN,self.tag + '.BUY_INTENT_POWER_OPEN')
        self.addDailyData(self.NET_BUY_POWER_OPEN,self.tag + '.NET_BUY_POWER_OPEN')
        self.addDailyData(self.OVAL_MBSR,self.tag + '.OVAL_MBSR')
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
            self.RET_VOL_C[di, ii]  = float(linespt[3])
            self.RET_VOL_W[di, ii]  = float(linespt[4])
            self.REV_ENHANCE[di, ii]  = float(linespt[5])
            self.GMM_DMEAN[di, ii]  = float(linespt[6])
            self.GMM_MEAN[di, ii]  = float(linespt[7])
            self.MIN_BETA[di, ii]  = float(linespt[8])
            self.MIN_IRET_KURT_AVE[di, ii]  = float(linespt[9])
            self.MIN_IRET_SKEW_AVE[di, ii]  = float(linespt[10])
            self.MIN_RET_KURT_AVE[di, ii]  = float(linespt[11])
            self.MIN_RET_SKEW_AVE[di, ii]  = float(linespt[12])
            self.SMART_MONEY[di, ii]  = float(linespt[13])
            self.MCI_A[di, ii]  = float(linespt[14])
            self.MCI_B[di, ii]  = float(linespt[15])
            self.MCI_IMB[di, ii]  = float(linespt[16])
            self.MPB[di, ii]  = float(linespt[17])
            self.MPC_MAX[di, ii]  = float(linespt[18])
            self.MPC_SKEW[di, ii]  = float(linespt[19])
            self.OIR[di, ii]  = float(linespt[20])
            self.VOI[di, ii]  = float(linespt[21])
            self.MINTVAL_MTE[di, ii]  = float(linespt[22])
            self.MINTVAL_MTS[di, ii]  = float(linespt[23])
            self.MINTVAL_QUA[di, ii]  = float(linespt[24])
            self.MINTVAL_SKEW[di, ii]  = float(linespt[25])
            self.INF_BUY_RATIO_CLOSE[di, ii]  = float(linespt[26])
            self.INF_SELL_RATIO_OPEN[di, ii]  = float(linespt[27])
            self.SECTVAL_KURT[di, ii]  = float(linespt[28])
            self.BUY_INTENT_RATIO_OPEN[di, ii]  = float(linespt[29])
            self.BUY_INTENT_POWER_OPEN[di, ii]  = float(linespt[30])
            self.NET_BUY_POWER_OPEN[di, ii]  = float(linespt[31])
            self.OVAL_MBSR[di, ii]  = float(linespt[32])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.RET_VOL_C[di] = self.RET_VOL_C[di - 1]
        self.RET_VOL_W[di] = self.RET_VOL_W[di - 1]
        self.REV_ENHANCE[di] = self.REV_ENHANCE[di - 1]
        self.GMM_DMEAN[di] = self.GMM_DMEAN[di - 1]
        self.GMM_MEAN[di] = self.GMM_MEAN[di - 1]
        self.MIN_BETA[di] = self.MIN_BETA[di - 1]
        self.MIN_IRET_KURT_AVE[di] = self.MIN_IRET_KURT_AVE[di - 1]
        self.MIN_IRET_SKEW_AVE[di] = self.MIN_IRET_SKEW_AVE[di - 1]
        self.MIN_RET_KURT_AVE[di] = self.MIN_RET_KURT_AVE[di - 1]
        self.MIN_RET_SKEW_AVE[di] = self.MIN_RET_SKEW_AVE[di - 1]
        self.SMART_MONEY[di] = self.SMART_MONEY[di - 1]
        self.MCI_A[di] = self.MCI_A[di - 1]
        self.MCI_B[di] = self.MCI_B[di - 1]
        self.MCI_IMB[di] = self.MCI_IMB[di - 1]
        self.MPB[di] = self.MPB[di - 1]
        self.MPC_MAX[di] = self.MPC_MAX[di - 1]
        self.MPC_SKEW[di] = self.MPC_SKEW[di - 1]
        self.OIR[di] = self.OIR[di - 1]
        self.VOI[di] = self.VOI[di - 1]
        self.MINTVAL_MTE[di] = self.MINTVAL_MTE[di - 1]
        self.MINTVAL_MTS[di] = self.MINTVAL_MTS[di - 1]
        self.MINTVAL_QUA[di] = self.MINTVAL_QUA[di - 1]
        self.MINTVAL_SKEW[di] = self.MINTVAL_SKEW[di - 1]
        self.INF_BUY_RATIO_CLOSE[di] = self.INF_BUY_RATIO_CLOSE[di - 1]
        self.INF_SELL_RATIO_OPEN[di] = self.INF_SELL_RATIO_OPEN[di - 1]
        self.SECTVAL_KURT[di] = self.SECTVAL_KURT[di - 1]
        self.BUY_INTENT_RATIO_OPEN[di] = self.BUY_INTENT_RATIO_OPEN[di - 1]
        self.BUY_INTENT_POWER_OPEN[di] = self.BUY_INTENT_POWER_OPEN[di - 1]
        self.NET_BUY_POWER_OPEN[di] = self.NET_BUY_POWER_OPEN[di - 1]
        self.OVAL_MBSR[di] = self.OVAL_MBSR[di - 1]