
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrhf_daily_auction_table(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.OVERNIGHT_RET = NIO_MATRIX()
        self.STAGE_ONE_RET = NIO_MATRIX()
        self.STAGE_TWO_RET = NIO_MATRIX()
        self.VOLUME_RATIO = NIO_MATRIX()
        self.STAGE_ONE_UP_LIMIT = NIO_MATRIX()
        self.STAGE_ONE_DOWN_LIMIT = NIO_MATRIX()
        self.UP_LIMIT = NIO_MATRIX()
        self.DOWN_LIMIT = NIO_MATRIX()
        self.STAGE_TWO_LAST_UP = NIO_MATRIX()
        self.STAGE_TWO_LAST_DOWN = NIO_MATRIX()
        self.STAGE_TWO_CLOSE = NIO_MATRIX()
        self.STAGE_ONE_COMMISSION = NIO_MATRIX()
        self.STAGE_TWO_COMMISSION = NIO_MATRIX()
        self.STAGE_TWO_LEAVE_RATIO = NIO_MATRIX()
        self.LAST_QUARTER_MINUTE_RET = NIO_MATRIX()
        self.LAST_HALF_MINUTE_RET = NIO_MATRIX()
        self.LAST_MINUTE_RET = NIO_MATRIX()
        self.JUMP_RET = NIO_MATRIX()
        self.OVERNIGHT_RET_BM = NIO_MATRIX()
        self.OVERNIGHT_RET_IND_1ST = NIO_MATRIX()
        self.OVERNIGHT_RET_IND_2ND = NIO_MATRIX()
        self.OVERNIGHT_RET_IND_3RD = NIO_MATRIX()
        self.RET_PRED = NIO_MATRIX()
        self.RET_PRED_0935 = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.OVERNIGHT_RET,self.tag + '.OVERNIGHT_RET')
        self.addDailyData(self.STAGE_ONE_RET,self.tag + '.STAGE_ONE_RET')
        self.addDailyData(self.STAGE_TWO_RET,self.tag + '.STAGE_TWO_RET')
        self.addDailyData(self.VOLUME_RATIO,self.tag + '.VOLUME_RATIO')
        self.addDailyData(self.STAGE_ONE_UP_LIMIT,self.tag + '.STAGE_ONE_UP_LIMIT')
        self.addDailyData(self.STAGE_ONE_DOWN_LIMIT,self.tag + '.STAGE_ONE_DOWN_LIMIT')
        self.addDailyData(self.UP_LIMIT,self.tag + '.UP_LIMIT')
        self.addDailyData(self.DOWN_LIMIT,self.tag + '.DOWN_LIMIT')
        self.addDailyData(self.STAGE_TWO_LAST_UP,self.tag + '.STAGE_TWO_LAST_UP')
        self.addDailyData(self.STAGE_TWO_LAST_DOWN,self.tag + '.STAGE_TWO_LAST_DOWN')
        self.addDailyData(self.STAGE_TWO_CLOSE,self.tag + '.STAGE_TWO_CLOSE')
        self.addDailyData(self.STAGE_ONE_COMMISSION,self.tag + '.STAGE_ONE_COMMISSION')
        self.addDailyData(self.STAGE_TWO_COMMISSION,self.tag + '.STAGE_TWO_COMMISSION')
        self.addDailyData(self.STAGE_TWO_LEAVE_RATIO,self.tag + '.STAGE_TWO_LEAVE_RATIO')
        self.addDailyData(self.LAST_QUARTER_MINUTE_RET,self.tag + '.LAST_QUARTER_MINUTE_RET')
        self.addDailyData(self.LAST_HALF_MINUTE_RET,self.tag + '.LAST_HALF_MINUTE_RET')
        self.addDailyData(self.LAST_MINUTE_RET,self.tag + '.LAST_MINUTE_RET')
        self.addDailyData(self.JUMP_RET,self.tag + '.JUMP_RET')
        self.addDailyData(self.OVERNIGHT_RET_BM,self.tag + '.OVERNIGHT_RET_BM')
        self.addDailyData(self.OVERNIGHT_RET_IND_1ST,self.tag + '.OVERNIGHT_RET_IND_1ST')
        self.addDailyData(self.OVERNIGHT_RET_IND_2ND,self.tag + '.OVERNIGHT_RET_IND_2ND')
        self.addDailyData(self.OVERNIGHT_RET_IND_3RD,self.tag + '.OVERNIGHT_RET_IND_3RD')
        self.addDailyData(self.RET_PRED,self.tag + '.RET_PRED')
        self.addDailyData(self.RET_PRED_0935,self.tag + '.RET_PRED_0935')
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
            self.OVERNIGHT_RET[di, ii]  = float(linespt[4])
            self.STAGE_ONE_RET[di, ii]  = float(linespt[5])
            self.STAGE_TWO_RET[di, ii]  = float(linespt[6])
            self.VOLUME_RATIO[di, ii]  = float(linespt[7])
            self.STAGE_ONE_UP_LIMIT[di, ii]  = float(linespt[8])
            self.STAGE_ONE_DOWN_LIMIT[di, ii]  = float(linespt[9])
            self.UP_LIMIT[di, ii]  = float(linespt[10])
            self.DOWN_LIMIT[di, ii]  = float(linespt[11])
            self.STAGE_TWO_LAST_UP[di, ii]  = float(linespt[12])
            self.STAGE_TWO_LAST_DOWN[di, ii]  = float(linespt[13])
            self.STAGE_TWO_CLOSE[di, ii]  = float(linespt[14])
            self.STAGE_ONE_COMMISSION[di, ii]  = float(linespt[15])
            self.STAGE_TWO_COMMISSION[di, ii]  = float(linespt[16])
            self.STAGE_TWO_LEAVE_RATIO[di, ii]  = float(linespt[17])
            self.LAST_QUARTER_MINUTE_RET[di, ii]  = float(linespt[18])
            self.LAST_HALF_MINUTE_RET[di, ii]  = float(linespt[19])
            self.LAST_MINUTE_RET[di, ii]  = float(linespt[20])
            self.JUMP_RET[di, ii]  = float(linespt[21])
            self.OVERNIGHT_RET_BM[di, ii]  = float(linespt[22])
            self.OVERNIGHT_RET_IND_1ST[di, ii]  = float(linespt[23])
            self.OVERNIGHT_RET_IND_2ND[di, ii]  = float(linespt[24])
            self.OVERNIGHT_RET_IND_3RD[di, ii]  = float(linespt[25])
            self.RET_PRED[di, ii]  = float(linespt[26])
            self.RET_PRED_0935[di, ii]  = float(linespt[27])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.OVERNIGHT_RET[di] = self.OVERNIGHT_RET[di - 1]
        self.STAGE_ONE_RET[di] = self.STAGE_ONE_RET[di - 1]
        self.STAGE_TWO_RET[di] = self.STAGE_TWO_RET[di - 1]
        self.VOLUME_RATIO[di] = self.VOLUME_RATIO[di - 1]
        self.STAGE_ONE_UP_LIMIT[di] = self.STAGE_ONE_UP_LIMIT[di - 1]
        self.STAGE_ONE_DOWN_LIMIT[di] = self.STAGE_ONE_DOWN_LIMIT[di - 1]
        self.UP_LIMIT[di] = self.UP_LIMIT[di - 1]
        self.DOWN_LIMIT[di] = self.DOWN_LIMIT[di - 1]
        self.STAGE_TWO_LAST_UP[di] = self.STAGE_TWO_LAST_UP[di - 1]
        self.STAGE_TWO_LAST_DOWN[di] = self.STAGE_TWO_LAST_DOWN[di - 1]
        self.STAGE_TWO_CLOSE[di] = self.STAGE_TWO_CLOSE[di - 1]
        self.STAGE_ONE_COMMISSION[di] = self.STAGE_ONE_COMMISSION[di - 1]
        self.STAGE_TWO_COMMISSION[di] = self.STAGE_TWO_COMMISSION[di - 1]
        self.STAGE_TWO_LEAVE_RATIO[di] = self.STAGE_TWO_LEAVE_RATIO[di - 1]
        self.LAST_QUARTER_MINUTE_RET[di] = self.LAST_QUARTER_MINUTE_RET[di - 1]
        self.LAST_HALF_MINUTE_RET[di] = self.LAST_HALF_MINUTE_RET[di - 1]
        self.LAST_MINUTE_RET[di] = self.LAST_MINUTE_RET[di - 1]
        self.JUMP_RET[di] = self.JUMP_RET[di - 1]
        self.OVERNIGHT_RET_BM[di] = self.OVERNIGHT_RET_BM[di - 1]
        self.OVERNIGHT_RET_IND_1ST[di] = self.OVERNIGHT_RET_IND_1ST[di - 1]
        self.OVERNIGHT_RET_IND_2ND[di] = self.OVERNIGHT_RET_IND_2ND[di - 1]
        self.OVERNIGHT_RET_IND_3RD[di] = self.OVERNIGHT_RET_IND_3RD[di - 1]
        self.RET_PRED[di] = self.RET_PRED[di - 1]
        self.RET_PRED_0935[di] = self.RET_PRED_0935[di - 1]
