
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrhf_daily_der_table_9(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.TRADE_IMB_ISOLATE = NIO_MATRIX()
        self.TRADE_IMB_FOLLOW = NIO_MATRIX()
        self.NORMAL_BIG_BUY_RATIO = NIO_MATRIX()
        self.NORMAL_BIG_BR_OPEN = NIO_MATRIX()
        self.BIG_BUY_RATIO = NIO_MATRIX()
        self.HCVOLES2 = NIO_MATRIX()
        self.LCVOLES1 = NIO_MATRIX()
        self.LCPES = NIO_MATRIX()
        self.CORR_PM = NIO_MATRIX()
        self.CORR_PV = NIO_MATRIX()
        self.CORR_PVPM = NIO_MATRIX()
        self.HP_DEAL_RATIO = NIO_MATRIX()
        self.HP_VOL_RATIO = NIO_MATRIX()
        self.LP_APB_RATIO = NIO_MATRIX()
        self.BB_SB_BS_LS = NIO_MATRIX()
        self.BB_SB_BS_SS = NIO_MATRIX()
        self.BB_SB_SS_LS = NIO_MATRIX()
        self.SB_SB_BS_LS_BFC = NIO_MATRIX()
        self.SB_SB_SS_LS = NIO_MATRIX()
        self.SHORT_B_LONG_S_1P0 = NIO_MATRIX()
        self.BIGBUY_1P0_AFO = NIO_MATRIX()
        self.BIGBUY_BIGSELL_1P0 = NIO_MATRIX()
        self.BIG_B_BIG_S_1P0_AFO = NIO_MATRIX()
        self.BIG_B_BIG_S_1P0_BFC = NIO_MATRIX()
        self.RL_LONG_ORDER_RATIO = NIO_MATRIX()
        self.RL_OBC_ORDER_RATIO = NIO_MATRIX()
        self.CROWD_FFTV20_3S = NIO_MATRIX()
        self.CROWD_FFTV5 = NIO_MATRIX()
        self.CROWD_FFTV50 = NIO_MATRIX()
        self.ESI = NIO_MATRIX()
        self.PRSI = NIO_MATRIX()
        self.CPQSI = NIO_MATRIX()
        self.BREAK_LEVELS = NIO_MATRIX()
        self.AFH_OPEN = NIO_MATRIX()
        self.AFH_CLOSE = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.TRADE_IMB_ISOLATE,self.tag + '.TRADE_IMB_ISOLATE')
        self.addDailyData(self.TRADE_IMB_FOLLOW,self.tag + '.TRADE_IMB_FOLLOW')
        self.addDailyData(self.NORMAL_BIG_BUY_RATIO,self.tag + '.NORMAL_BIG_BUY_RATIO')
        self.addDailyData(self.NORMAL_BIG_BR_OPEN,self.tag + '.NORMAL_BIG_BR_OPEN')
        self.addDailyData(self.BIG_BUY_RATIO,self.tag + '.BIG_BUY_RATIO')
        self.addDailyData(self.HCVOLES2,self.tag + '.HCVOLES2')
        self.addDailyData(self.LCVOLES1,self.tag + '.LCVOLES1')
        self.addDailyData(self.LCPES,self.tag + '.LCPES')
        self.addDailyData(self.CORR_PM,self.tag + '.CORR_PM')
        self.addDailyData(self.CORR_PV,self.tag + '.CORR_PV')
        self.addDailyData(self.CORR_PVPM,self.tag + '.CORR_PVPM')
        self.addDailyData(self.HP_DEAL_RATIO,self.tag + '.HP_DEAL_RATIO')
        self.addDailyData(self.HP_VOL_RATIO,self.tag + '.HP_VOL_RATIO')
        self.addDailyData(self.LP_APB_RATIO,self.tag + '.LP_APB_RATIO')
        self.addDailyData(self.BB_SB_BS_LS,self.tag + '.BB_SB_BS_LS')
        self.addDailyData(self.BB_SB_BS_SS,self.tag + '.BB_SB_BS_SS')
        self.addDailyData(self.BB_SB_SS_LS,self.tag + '.BB_SB_SS_LS')
        self.addDailyData(self.SB_SB_BS_LS_BFC,self.tag + '.SB_SB_BS_LS_BFC')
        self.addDailyData(self.SB_SB_SS_LS,self.tag + '.SB_SB_SS_LS')
        self.addDailyData(self.SHORT_B_LONG_S_1P0,self.tag + '.SHORT_B_LONG_S_1P0')
        self.addDailyData(self.BIGBUY_1P0_AFO,self.tag + '.BIGBUY_1P0_AFO')
        self.addDailyData(self.BIGBUY_BIGSELL_1P0,self.tag + '.BIGBUY_BIGSELL_1P0')
        self.addDailyData(self.BIG_B_BIG_S_1P0_AFO,self.tag + '.BIG_B_BIG_S_1P0_AFO')
        self.addDailyData(self.BIG_B_BIG_S_1P0_BFC,self.tag + '.BIG_B_BIG_S_1P0_BFC')
        self.addDailyData(self.RL_LONG_ORDER_RATIO,self.tag + '.RL_LONG_ORDER_RATIO')
        self.addDailyData(self.RL_OBC_ORDER_RATIO,self.tag + '.RL_OBC_ORDER_RATIO')
        self.addDailyData(self.CROWD_FFTV20_3S,self.tag + '.CROWD_FFTV20_3S')
        self.addDailyData(self.CROWD_FFTV5,self.tag + '.CROWD_FFTV5')
        self.addDailyData(self.CROWD_FFTV50,self.tag + '.CROWD_FFTV50')
        self.addDailyData(self.ESI,self.tag + '.ESI')
        self.addDailyData(self.PRSI,self.tag + '.PRSI')
        self.addDailyData(self.CPQSI,self.tag + '.CPQSI')
        self.addDailyData(self.BREAK_LEVELS,self.tag + '.BREAK_LEVELS')
        self.addDailyData(self.AFH_OPEN,self.tag + '.AFH_OPEN')
        self.addDailyData(self.AFH_CLOSE,self.tag + '.AFH_CLOSE')
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
            self.TRADE_IMB_ISOLATE[di, ii]  = float(linespt[3])
            self.TRADE_IMB_FOLLOW[di, ii]  = float(linespt[4])
            self.NORMAL_BIG_BUY_RATIO[di, ii]  = float(linespt[5])
            self.NORMAL_BIG_BR_OPEN[di, ii]  = float(linespt[6])
            self.BIG_BUY_RATIO[di, ii]  = float(linespt[7])
            self.HCVOLES2[di, ii]  = float(linespt[8])
            self.LCVOLES1[di, ii]  = float(linespt[9])
            self.LCPES[di, ii]  = float(linespt[10])
            self.CORR_PM[di, ii]  = float(linespt[11])
            self.CORR_PV[di, ii]  = float(linespt[12])
            self.CORR_PVPM[di, ii]  = float(linespt[13])
            self.HP_DEAL_RATIO[di, ii]  = float(linespt[14])
            self.HP_VOL_RATIO[di, ii]  = float(linespt[15])
            self.LP_APB_RATIO[di, ii]  = float(linespt[16])
            self.BB_SB_BS_LS[di, ii]  = float(linespt[17])
            self.BB_SB_BS_SS[di, ii]  = float(linespt[18])
            self.BB_SB_SS_LS[di, ii]  = float(linespt[19])
            self.SB_SB_BS_LS_BFC[di, ii]  = float(linespt[20])
            self.SB_SB_SS_LS[di, ii]  = float(linespt[21])
            self.SHORT_B_LONG_S_1P0[di, ii]  = float(linespt[22])
            self.BIGBUY_1P0_AFO[di, ii]  = float(linespt[23])
            self.BIGBUY_BIGSELL_1P0[di, ii]  = float(linespt[24])
            self.BIG_B_BIG_S_1P0_AFO[di, ii]  = float(linespt[25])
            self.BIG_B_BIG_S_1P0_BFC[di, ii]  = float(linespt[26])
            self.RL_LONG_ORDER_RATIO[di, ii]  = float(linespt[27])
            self.RL_OBC_ORDER_RATIO[di, ii]  = float(linespt[28])
            self.CROWD_FFTV20_3S[di, ii]  = float(linespt[29])
            self.CROWD_FFTV5[di, ii]  = float(linespt[30])
            self.CROWD_FFTV50[di, ii]  = float(linespt[31])
            self.ESI[di, ii]  = float(linespt[32])
            self.PRSI[di, ii]  = float(linespt[33])
            self.CPQSI[di, ii]  = float(linespt[34])
            self.BREAK_LEVELS[di, ii]  = float(linespt[35])
            self.AFH_OPEN[di, ii]  = float(linespt[36])
            self.AFH_CLOSE[di, ii]  = float(linespt[37])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.TRADE_IMB_ISOLATE[di] = self.TRADE_IMB_ISOLATE[di - 1]
        self.TRADE_IMB_FOLLOW[di] = self.TRADE_IMB_FOLLOW[di - 1]
        self.NORMAL_BIG_BUY_RATIO[di] = self.NORMAL_BIG_BUY_RATIO[di - 1]
        self.NORMAL_BIG_BR_OPEN[di] = self.NORMAL_BIG_BR_OPEN[di - 1]
        self.BIG_BUY_RATIO[di] = self.BIG_BUY_RATIO[di - 1]
        self.HCVOLES2[di] = self.HCVOLES2[di - 1]
        self.LCVOLES1[di] = self.LCVOLES1[di - 1]
        self.LCPES[di] = self.LCPES[di - 1]
        self.CORR_PM[di] = self.CORR_PM[di - 1]
        self.CORR_PV[di] = self.CORR_PV[di - 1]
        self.CORR_PVPM[di] = self.CORR_PVPM[di - 1]
        self.HP_DEAL_RATIO[di] = self.HP_DEAL_RATIO[di - 1]
        self.HP_VOL_RATIO[di] = self.HP_VOL_RATIO[di - 1]
        self.LP_APB_RATIO[di] = self.LP_APB_RATIO[di - 1]
        self.BB_SB_BS_LS[di] = self.BB_SB_BS_LS[di - 1]
        self.BB_SB_BS_SS[di] = self.BB_SB_BS_SS[di - 1]
        self.BB_SB_SS_LS[di] = self.BB_SB_SS_LS[di - 1]
        self.SB_SB_BS_LS_BFC[di] = self.SB_SB_BS_LS_BFC[di - 1]
        self.SB_SB_SS_LS[di] = self.SB_SB_SS_LS[di - 1]
        self.SHORT_B_LONG_S_1P0[di] = self.SHORT_B_LONG_S_1P0[di - 1]
        self.BIGBUY_1P0_AFO[di] = self.BIGBUY_1P0_AFO[di - 1]
        self.BIGBUY_BIGSELL_1P0[di] = self.BIGBUY_BIGSELL_1P0[di - 1]
        self.BIG_B_BIG_S_1P0_AFO[di] = self.BIG_B_BIG_S_1P0_AFO[di - 1]
        self.BIG_B_BIG_S_1P0_BFC[di] = self.BIG_B_BIG_S_1P0_BFC[di - 1]
        self.RL_LONG_ORDER_RATIO[di] = self.RL_LONG_ORDER_RATIO[di - 1]
        self.RL_OBC_ORDER_RATIO[di] = self.RL_OBC_ORDER_RATIO[di - 1]
        self.CROWD_FFTV20_3S[di] = self.CROWD_FFTV20_3S[di - 1]
        self.CROWD_FFTV5[di] = self.CROWD_FFTV5[di - 1]
        self.CROWD_FFTV50[di] = self.CROWD_FFTV50[di - 1]
        self.ESI[di] = self.ESI[di - 1]
        self.PRSI[di] = self.PRSI[di - 1]
        self.CPQSI[di] = self.CPQSI[di - 1]
        self.BREAK_LEVELS[di] = self.BREAK_LEVELS[di - 1]
        self.AFH_OPEN[di] = self.AFH_OPEN[di - 1]
        self.AFH_CLOSE[di] = self.AFH_CLOSE[di - 1]