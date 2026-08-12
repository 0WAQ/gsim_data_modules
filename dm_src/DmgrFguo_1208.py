from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np


class DmgrFguo1208(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.avg_book_slope_buy = NIO_MATRIX()
        self.avg_book_slope_sell = NIO_MATRIX()
        self.avg_imbalance_depth10 = NIO_MATRIX()
        self.avg_imbalance_depth5 = NIO_MATRIX()
        self.avg_imbalance_level1 = NIO_MATRIX()
        self.avg_imbalance_weighted = NIO_MATRIX()
        self.avg_micro_price = NIO_MATRIX()
        self.avg_mid_price = NIO_MATRIX()
        self.avg_order_size_ratio = NIO_MATRIX()
        self.avg_price_dispersion_buy = NIO_MATRIX()
        self.avg_price_dispersion_sell = NIO_MATRIX()
        self.avg_price_stddev_buy = NIO_MATRIX()
        self.avg_price_stddev_sell = NIO_MATRIX()
        self.avg_spread_absolute = NIO_MATRIX()
        self.avg_spread_level_10 = NIO_MATRIX()
        self.avg_spread_level_5 = NIO_MATRIX()
        self.avg_spread_relative = NIO_MATRIX()
        self.avg_trade_size = NIO_MATRIX()
        self.avg_wt_price_deviation_buy = NIO_MATRIX()
        self.avg_wt_price_deviation_sell = NIO_MATRIX()
        self.daily_vwap = NIO_MATRIX()
        self.tick_count = NIO_MATRIX()
        self.total_amount = NIO_MATRIX()
        self.total_trade_count = NIO_MATRIX()
        self.total_volume = NIO_MATRIX()
        self.vw_imbalance_depth10 = NIO_MATRIX()
        self.vw_imbalance_depth5 = NIO_MATRIX()
        self.vw_imbalance_level1 = NIO_MATRIX()
        self.vw_spread_absolute = NIO_MATRIX()
        self.vw_spread_relative = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.addDailyData(self.avg_book_slope_buy, 'fguo_1208.avg_book_slope_buy')
        self.addDailyData(self.avg_book_slope_sell, 'fguo_1208.avg_book_slope_sell')
        self.addDailyData(self.avg_imbalance_depth10, 'fguo_1208.avg_imbalance_depth10')
        self.addDailyData(self.avg_imbalance_depth5, 'fguo_1208.avg_imbalance_depth5')
        self.addDailyData(self.avg_imbalance_level1, 'fguo_1208.avg_imbalance_level1')
        self.addDailyData(self.avg_imbalance_weighted, 'fguo_1208.avg_imbalance_weighted')
        self.addDailyData(self.avg_micro_price, 'fguo_1208.avg_micro_price')
        self.addDailyData(self.avg_mid_price, 'fguo_1208.avg_mid_price')
        self.addDailyData(self.avg_order_size_ratio, 'fguo_1208.avg_order_size_ratio')
        self.addDailyData(self.avg_price_dispersion_buy, 'fguo_1208.avg_price_dispersion_buy')
        self.addDailyData(self.avg_price_dispersion_sell, 'fguo_1208.avg_price_dispersion_sell')
        self.addDailyData(self.avg_price_stddev_buy, 'fguo_1208.avg_price_stddev_buy')
        self.addDailyData(self.avg_price_stddev_sell, 'fguo_1208.avg_price_stddev_sell')
        self.addDailyData(self.avg_spread_absolute, 'fguo_1208.avg_spread_absolute')
        self.addDailyData(self.avg_spread_level_10, 'fguo_1208.avg_spread_level_10')
        self.addDailyData(self.avg_spread_level_5, 'fguo_1208.avg_spread_level_5')
        self.addDailyData(self.avg_spread_relative, 'fguo_1208.avg_spread_relative')
        self.addDailyData(self.avg_trade_size, 'fguo_1208.avg_trade_size')
        self.addDailyData(self.avg_wt_price_deviation_buy, 'fguo_1208.avg_wt_price_deviation_buy')
        self.addDailyData(self.avg_wt_price_deviation_sell, 'fguo_1208.avg_wt_price_deviation_sell')
        self.addDailyData(self.daily_vwap, 'fguo_1208.daily_vwap')
        self.addDailyData(self.tick_count, 'fguo_1208.tick_count')
        self.addDailyData(self.total_amount, 'fguo_1208.total_amount')
        self.addDailyData(self.total_trade_count, 'fguo_1208.total_trade_count')
        self.addDailyData(self.total_volume, 'fguo_1208.total_volume')
        self.addDailyData(self.vw_imbalance_depth10, 'fguo_1208.vw_imbalance_depth10')
        self.addDailyData(self.vw_imbalance_depth5, 'fguo_1208.vw_imbalance_depth5')
        self.addDailyData(self.vw_imbalance_level1, 'fguo_1208.vw_imbalance_level1')
        self.addDailyData(self.vw_spread_absolute, 'fguo_1208.vw_spread_absolute')
        self.addDailyData(self.vw_spread_relative, 'fguo_1208.vw_spread_relative')
        return

    def loadDay(self, di):
        pass
