
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrhf_daily_der_table_8(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.LMS = NIO_MATRIX()
        self.MEMO_SKEW = NIO_MATRIX()
        self.MEMO_KURT = NIO_MATRIX()
        self.ORDER_ISLAND_BUY_MU = NIO_MATRIX()
        self.ORDER_ISLAND_BUY_SD = NIO_MATRIX()
        self.ORDER_ISLAND_SELL_MU = NIO_MATRIX()
        self.ORDER_ISLAND_SELL_SD = NIO_MATRIX()
        self.TRIX = NIO_MATRIX()
        self.TOX = NIO_MATRIX()
        self.AUCTION_CANCEL_RATIO = NIO_MATRIX()
        self.EARLY_BUY_SELL_RATIO = NIO_MATRIX()
        self.MARKET_OR = NIO_MATRIX()
        self.MARKET_LIMIT_OR = NIO_MATRIX()
        self.MARKET_BUY_MARKET_OR = NIO_MATRIX()
        self.MARKET_B_LIMIT_B_OR = NIO_MATRIX()
        self.MARKET_B_LIMIT_S_OR = NIO_MATRIX()
        self.MARKET_S_LIMIT_B_OR = NIO_MATRIX()
        self.MARKET_S_LIMIT_S_OR = NIO_MATRIX()
        self.LIMIT_BUY_LIMIT_OR = NIO_MATRIX()
        self.BUY_T_OR_OP1 = NIO_MATRIX()
        self.SELL_T_OR_OP1 = NIO_MATRIX()
        self.T_OR_OP1 = NIO_MATRIX()
        self.BUY_W_OR_OP1 = NIO_MATRIX()
        self.SELL_W_OR_OP1 = NIO_MATRIX()
        self.W_OR_OP1 = NIO_MATRIX()
        self.BUY_T_OR_OP2 = NIO_MATRIX()
        self.SELL_T_OR_OP2 = NIO_MATRIX()
        self.T_OR_OP2 = NIO_MATRIX()
        self.BUY_T_OR_CP = NIO_MATRIX()
        self.SELL_T_OR_CP = NIO_MATRIX()
        self.T_OR_CP = NIO_MATRIX()
        self.RET_OPEN_2AL1 = NIO_MATRIX()
        self.TRADE_CBUY_RATIO = NIO_MATRIX()
        self.TRADE_CRATIO = NIO_MATRIX()
        self.TRADE_CSELL_RATIO = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.LMS,self.tag + '.LMS')
        self.addDailyData(self.MEMO_SKEW,self.tag + '.MEMO_SKEW')
        self.addDailyData(self.MEMO_KURT,self.tag + '.MEMO_KURT')
        self.addDailyData(self.ORDER_ISLAND_BUY_MU,self.tag + '.ORDER_ISLAND_BUY_MU')
        self.addDailyData(self.ORDER_ISLAND_BUY_SD,self.tag + '.ORDER_ISLAND_BUY_SD')
        self.addDailyData(self.ORDER_ISLAND_SELL_MU,self.tag + '.ORDER_ISLAND_SELL_MU')
        self.addDailyData(self.ORDER_ISLAND_SELL_SD,self.tag + '.ORDER_ISLAND_SELL_SD')
        self.addDailyData(self.TRIX,self.tag + '.TRIX')
        self.addDailyData(self.TOX,self.tag + '.TOX')
        self.addDailyData(self.AUCTION_CANCEL_RATIO,self.tag + '.AUCTION_CANCEL_RATIO')
        self.addDailyData(self.EARLY_BUY_SELL_RATIO,self.tag + '.EARLY_BUY_SELL_RATIO')
        self.addDailyData(self.MARKET_OR,self.tag + '.MARKET_OR')
        self.addDailyData(self.MARKET_LIMIT_OR,self.tag + '.MARKET_LIMIT_OR')
        self.addDailyData(self.MARKET_BUY_MARKET_OR,self.tag + '.MARKET_BUY_MARKET_OR')
        self.addDailyData(self.MARKET_B_LIMIT_B_OR,self.tag + '.MARKET_B_LIMIT_B_OR')
        self.addDailyData(self.MARKET_B_LIMIT_S_OR,self.tag + '.MARKET_B_LIMIT_S_OR')
        self.addDailyData(self.MARKET_S_LIMIT_B_OR,self.tag + '.MARKET_S_LIMIT_B_OR')
        self.addDailyData(self.MARKET_S_LIMIT_S_OR,self.tag + '.MARKET_S_LIMIT_S_OR')
        self.addDailyData(self.LIMIT_BUY_LIMIT_OR,self.tag + '.LIMIT_BUY_LIMIT_OR')
        self.addDailyData(self.BUY_T_OR_OP1,self.tag + '.BUY_T_OR_OP1')
        self.addDailyData(self.SELL_T_OR_OP1,self.tag + '.SELL_T_OR_OP1')
        self.addDailyData(self.T_OR_OP1,self.tag + '.T_OR_OP1')
        self.addDailyData(self.BUY_W_OR_OP1,self.tag + '.BUY_W_OR_OP1')
        self.addDailyData(self.SELL_W_OR_OP1,self.tag + '.SELL_W_OR_OP1')
        self.addDailyData(self.W_OR_OP1,self.tag + '.W_OR_OP1')
        self.addDailyData(self.BUY_T_OR_OP2,self.tag + '.BUY_T_OR_OP2')
        self.addDailyData(self.SELL_T_OR_OP2,self.tag + '.SELL_T_OR_OP2')
        self.addDailyData(self.T_OR_OP2,self.tag + '.T_OR_OP2')
        self.addDailyData(self.BUY_T_OR_CP,self.tag + '.BUY_T_OR_CP')
        self.addDailyData(self.SELL_T_OR_CP,self.tag + '.SELL_T_OR_CP')
        self.addDailyData(self.T_OR_CP,self.tag + '.T_OR_CP')
        self.addDailyData(self.RET_OPEN_2AL1,self.tag + '.RET_OPEN_2AL1')
        self.addDailyData(self.TRADE_CBUY_RATIO,self.tag + '.TRADE_CBUY_RATIO')
        self.addDailyData(self.TRADE_CRATIO,self.tag + '.TRADE_CRATIO')
        self.addDailyData(self.TRADE_CSELL_RATIO,self.tag + '.TRADE_CSELL_RATIO')
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
            self.LMS[di, ii]  = float(linespt[3])
            self.MEMO_SKEW[di, ii]  = float(linespt[4])
            self.MEMO_KURT[di, ii]  = float(linespt[5])
            self.ORDER_ISLAND_BUY_MU[di, ii]  = float(linespt[6])
            self.ORDER_ISLAND_BUY_SD[di, ii]  = float(linespt[7])
            self.ORDER_ISLAND_SELL_MU[di, ii]  = float(linespt[8])
            self.ORDER_ISLAND_SELL_SD[di, ii]  = float(linespt[9])
            self.TRIX[di, ii]  = float(linespt[10])
            self.TOX[di, ii]  = float(linespt[11])
            self.AUCTION_CANCEL_RATIO[di, ii]  = float(linespt[12])
            self.EARLY_BUY_SELL_RATIO[di, ii]  = float(linespt[13])
            self.MARKET_OR[di, ii]  = float(linespt[14])
            self.MARKET_LIMIT_OR[di, ii]  = float(linespt[15])
            self.MARKET_BUY_MARKET_OR[di, ii]  = float(linespt[16])
            self.MARKET_B_LIMIT_B_OR[di, ii]  = float(linespt[17])
            self.MARKET_B_LIMIT_S_OR[di, ii]  = float(linespt[18])
            self.MARKET_S_LIMIT_B_OR[di, ii]  = float(linespt[19])
            self.MARKET_S_LIMIT_S_OR[di, ii]  = float(linespt[20])
            self.LIMIT_BUY_LIMIT_OR[di, ii]  = float(linespt[21])
            self.BUY_T_OR_OP1[di, ii]  = float(linespt[22])
            self.SELL_T_OR_OP1[di, ii]  = float(linespt[23])
            self.T_OR_OP1[di, ii]  = float(linespt[24])
            self.BUY_W_OR_OP1[di, ii]  = float(linespt[25])
            self.SELL_W_OR_OP1[di, ii]  = float(linespt[26])
            self.W_OR_OP1[di, ii]  = float(linespt[27])
            self.BUY_T_OR_OP2[di, ii]  = float(linespt[28])
            self.SELL_T_OR_OP2[di, ii]  = float(linespt[29])
            self.T_OR_OP2[di, ii]  = float(linespt[30])
            self.BUY_T_OR_CP[di, ii]  = float(linespt[31])
            self.SELL_T_OR_CP[di, ii]  = float(linespt[32])
            self.T_OR_CP[di, ii]  = float(linespt[33])
            self.RET_OPEN_2AL1[di, ii]  = float(linespt[34])
            self.TRADE_CBUY_RATIO[di, ii]  = float(linespt[35])
            self.TRADE_CRATIO[di, ii]  = float(linespt[36])
            self.TRADE_CSELL_RATIO[di, ii]  = float(linespt[37])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.LMS[di] = self.LMS[di - 1]
        self.MEMO_SKEW[di] = self.MEMO_SKEW[di - 1]
        self.MEMO_KURT[di] = self.MEMO_KURT[di - 1]
        self.ORDER_ISLAND_BUY_MU[di] = self.ORDER_ISLAND_BUY_MU[di - 1]
        self.ORDER_ISLAND_BUY_SD[di] = self.ORDER_ISLAND_BUY_SD[di - 1]
        self.ORDER_ISLAND_SELL_MU[di] = self.ORDER_ISLAND_SELL_MU[di - 1]
        self.ORDER_ISLAND_SELL_SD[di] = self.ORDER_ISLAND_SELL_SD[di - 1]
        self.TRIX[di] = self.TRIX[di - 1]
        self.TOX[di] = self.TOX[di - 1]
        self.AUCTION_CANCEL_RATIO[di] = self.AUCTION_CANCEL_RATIO[di - 1]
        self.EARLY_BUY_SELL_RATIO[di] = self.EARLY_BUY_SELL_RATIO[di - 1]
        self.MARKET_OR[di] = self.MARKET_OR[di - 1]
        self.MARKET_LIMIT_OR[di] = self.MARKET_LIMIT_OR[di - 1]
        self.MARKET_BUY_MARKET_OR[di] = self.MARKET_BUY_MARKET_OR[di - 1]
        self.MARKET_B_LIMIT_B_OR[di] = self.MARKET_B_LIMIT_B_OR[di - 1]
        self.MARKET_B_LIMIT_S_OR[di] = self.MARKET_B_LIMIT_S_OR[di - 1]
        self.MARKET_S_LIMIT_B_OR[di] = self.MARKET_S_LIMIT_B_OR[di - 1]
        self.MARKET_S_LIMIT_S_OR[di] = self.MARKET_S_LIMIT_S_OR[di - 1]
        self.LIMIT_BUY_LIMIT_OR[di] = self.LIMIT_BUY_LIMIT_OR[di - 1]
        self.BUY_T_OR_OP1[di] = self.BUY_T_OR_OP1[di - 1]
        self.SELL_T_OR_OP1[di] = self.SELL_T_OR_OP1[di - 1]
        self.T_OR_OP1[di] = self.T_OR_OP1[di - 1]
        self.BUY_W_OR_OP1[di] = self.BUY_W_OR_OP1[di - 1]
        self.SELL_W_OR_OP1[di] = self.SELL_W_OR_OP1[di - 1]
        self.W_OR_OP1[di] = self.W_OR_OP1[di - 1]
        self.BUY_T_OR_OP2[di] = self.BUY_T_OR_OP2[di - 1]
        self.SELL_T_OR_OP2[di] = self.SELL_T_OR_OP2[di - 1]
        self.T_OR_OP2[di] = self.T_OR_OP2[di - 1]
        self.BUY_T_OR_CP[di] = self.BUY_T_OR_CP[di - 1]
        self.SELL_T_OR_CP[di] = self.SELL_T_OR_CP[di - 1]
        self.T_OR_CP[di] = self.T_OR_CP[di - 1]
        self.RET_OPEN_2AL1[di] = self.RET_OPEN_2AL1[di - 1]
        self.TRADE_CBUY_RATIO[di] = self.TRADE_CBUY_RATIO[di - 1]
        self.TRADE_CRATIO[di] = self.TRADE_CRATIO[di - 1]
        self.TRADE_CSELL_RATIO[di] = self.TRADE_CSELL_RATIO[di - 1]