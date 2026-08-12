
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class DmgrL2ZZK(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.total_order_volume_0915_0920 = NIO_MATRIX()
        self.buy_order_volume_0915_0920 = NIO_MATRIX()
        self.sell_order_volume_0915_0920 = NIO_MATRIX()
        self.total_order_volume_0920_0925 = NIO_MATRIX()
        self.buy_order_volume_0920_0925 = NIO_MATRIX()
        self.sell_order_volume_0920_0925 = NIO_MATRIX()
        self.order_cancellation_ratio_0915_0920 = NIO_MATRIX()
        self.opening_match_volume_0925 = NIO_MATRIX()
        self.closing_session_volume = NIO_MATRIX()
        self.daily_total_traded_volume = NIO_MATRIX()
        self.total_number_of_trades = NIO_MATRIX()
        self.closing_active_buy_volume_ratio = NIO_MATRIX()
        self.closing_active_sell_volume_ratio = NIO_MATRIX()
        self.active_buy_trade_count_ratio = NIO_MATRIX()
        self.active_sell_trade_count_ratio = NIO_MATRIX()
        self.large_active_buy_order_ratio = NIO_MATRIX()
        self.large_active_sell_order_ratio = NIO_MATRIX()
        self.order_fill_ratio_0920_0925 = NIO_MATRIX()
        self.order_fill_ratio_0915_0925 = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.total_order_volume_0915_0920,self.tag + '.total_order_volume_0915_0920')
        self.addDailyData(self.buy_order_volume_0915_0920,self.tag + '.buy_order_volume_0915_0920')
        self.addDailyData(self.sell_order_volume_0915_0920,self.tag + '.sell_order_volume_0915_0920')
        self.addDailyData(self.total_order_volume_0920_0925,self.tag + '.total_order_volume_0920_0925')
        self.addDailyData(self.buy_order_volume_0920_0925,self.tag + '.buy_order_volume_0920_0925')
        self.addDailyData(self.sell_order_volume_0920_0925,self.tag + '.sell_order_volume_0920_0925')
        self.addDailyData(self.order_cancellation_ratio_0915_0920,self.tag + '.order_cancellation_ratio_0915_0920')
        self.addDailyData(self.opening_match_volume_0925,self.tag + '.opening_match_volume_0925')
        self.addDailyData(self.closing_session_volume,self.tag + '.closing_session_volume')
        self.addDailyData(self.daily_total_traded_volume,self.tag + '.daily_total_traded_volume')
        self.addDailyData(self.total_number_of_trades,self.tag + '.total_number_of_trades')
        self.addDailyData(self.closing_active_buy_volume_ratio,self.tag + '.closing_active_buy_volume_ratio')
        self.addDailyData(self.closing_active_sell_volume_ratio,self.tag + '.closing_active_sell_volume_ratio')
        self.addDailyData(self.active_buy_trade_count_ratio,self.tag + '.active_buy_trade_count_ratio')
        self.addDailyData(self.active_sell_trade_count_ratio,self.tag + '.active_sell_trade_count_ratio')
        self.addDailyData(self.large_active_buy_order_ratio,self.tag + '.large_active_buy_order_ratio')
        self.addDailyData(self.large_active_sell_order_ratio,self.tag + '.large_active_sell_order_ratio')
        self.addDailyData(self.order_fill_ratio_0920_0925,self.tag + '.order_fill_ratio_0920_0925')
        self.addDailyData(self.order_fill_ratio_0915_0925,self.tag + '.order_fill_ratio_0915_0925')
        return

    def loadDay(self, di):
        self.fillnan(di)  # set default value
        if di == len(uv.Dates) - 1:
            return
        if di > 1 and self.backfill:  # backfill
            self.doBackfill(di)
        filepath = os.path.join(self.dataPath, '%d' % uv.Dates[di]+".csv")
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
            ticker = linespt[0][2:]
            ii = uv.Instruments.lookup(ticker)
            if ii < 0:
                continue
            self.total_order_volume_0915_0920[di, ii]  = float(linespt[1])
            self.buy_order_volume_0915_0920[di, ii]  = float(linespt[2])
            self.sell_order_volume_0915_0920[di, ii]  = float(linespt[3])
            self.total_order_volume_0920_0925[di, ii]  = float(linespt[4])
            self.buy_order_volume_0920_0925[di, ii]  = float(linespt[5])
            self.sell_order_volume_0920_0925[di, ii]  = float(linespt[6])
            self.order_cancellation_ratio_0915_0920[di, ii]  = float(linespt[7])
            self.opening_match_volume_0925[di, ii]  = float(linespt[8])
            self.closing_session_volume[di, ii]  = float(linespt[9])
            self.daily_total_traded_volume[di, ii]  = float(linespt[10])
            self.total_number_of_trades[di, ii]  = float(linespt[11])
            self.closing_active_buy_volume_ratio[di, ii]  = float(linespt[12])
            self.closing_active_sell_volume_ratio[di, ii]  = float(linespt[13])
            self.active_buy_trade_count_ratio[di, ii]  = float(linespt[14])
            self.active_sell_trade_count_ratio[di, ii]  = float(linespt[15])
            self.large_active_buy_order_ratio[di, ii]  = float(linespt[16])
            self.large_active_sell_order_ratio[di, ii]  = float(linespt[17])
            self.order_fill_ratio_0920_0925[di, ii]  = float(linespt[18])
            self.order_fill_ratio_0915_0925[di, ii]  = float(linespt[19])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.total_order_volume_0915_0920[di] = self.total_order_volume_0915_0920[di - 1]
        self.buy_order_volume_0915_0920[di] = self.buy_order_volume_0915_0920[di - 1]
        self.sell_order_volume_0915_0920[di] = self.sell_order_volume_0915_0920[di - 1]
        self.total_order_volume_0920_0925[di] = self.total_order_volume_0920_0925[di - 1]
        self.buy_order_volume_0920_0925[di] = self.buy_order_volume_0920_0925[di - 1]
        self.sell_order_volume_0920_0925[di] = self.sell_order_volume_0920_0925[di - 1]
        self.order_cancellation_ratio_0915_0920[di] = self.order_cancellation_ratio_0915_0920[di - 1]
        self.opening_match_volume_0925[di] = self.opening_match_volume_0925[di - 1]
        self.closing_session_volume[di] = self.closing_session_volume[di - 1]
        self.daily_total_traded_volume[di] = self.daily_total_traded_volume[di - 1]
        self.total_number_of_trades[di] = self.total_number_of_trades[di - 1]
        self.closing_active_buy_volume_ratio[di] = self.closing_active_buy_volume_ratio[di - 1]
        self.closing_active_sell_volume_ratio[di] = self.closing_active_sell_volume_ratio[di - 1]
        self.active_buy_trade_count_ratio[di] = self.active_buy_trade_count_ratio[di - 1]
        self.active_sell_trade_count_ratio[di] = self.active_sell_trade_count_ratio[di - 1]
        self.large_active_buy_order_ratio[di] = self.large_active_buy_order_ratio[di - 1]
        self.large_active_sell_order_ratio[di] = self.large_active_sell_order_ratio[di - 1]
        self.order_fill_ratio_0920_0925[di] = self.order_fill_ratio_0920_0925[di - 1]
        self.order_fill_ratio_0915_0925[di] = self.order_fill_ratio_0915_0925[di - 1]
