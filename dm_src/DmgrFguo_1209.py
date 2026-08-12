from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np


class DmgrFguo1209(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.amihud_illiquidity = NIO_MATRIX()
        self.buy_count_ratio = NIO_MATRIX()
        self.buy_volume_ratio = NIO_MATRIX()
        self.effective_spread_avg = NIO_MATRIX()
        self.intraday_momentum = NIO_MATRIX()
        self.large_trade_count_ratio = NIO_MATRIX()
        self.large_trade_volume_ratio = NIO_MATRIX()
        self.mid_price_daily_avg = NIO_MATRIX()
        self.mid_price_daily_max = NIO_MATRIX()
        self.mid_price_daily_min = NIO_MATRIX()
        self.mid_price_daily_vwap = NIO_MATRIX()
        self.ofi_level1_daily_sum = NIO_MATRIX()
        self.ofi_level5_daily_sum = NIO_MATRIX()
        self.price_position_daily_avg = NIO_MATRIX()
        self.price_position_daily_max = NIO_MATRIX()
        self.price_position_daily_min = NIO_MATRIX()
        self.price_position_daily_vw = NIO_MATRIX()
        self.realized_volatility_daily = NIO_MATRIX()
        self.return_autocorr = NIO_MATRIX()
        self.rolling_volatility_10_avg = NIO_MATRIX()
        self.rolling_volatility_10_max = NIO_MATRIX()
        self.rolling_volatility_30_avg = NIO_MATRIX()
        self.rolling_volatility_30_max = NIO_MATRIX()
        self.small_trade_count_ratio = NIO_MATRIX()
        self.small_trade_volume_ratio = NIO_MATRIX()
        self.tick_count = NIO_MATRIX()
        self.trade_size_cv = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.addDailyData(self.amihud_illiquidity, 'fguo_1209.amihud_illiquidity')
        self.addDailyData(self.buy_count_ratio, 'fguo_1209.buy_count_ratio')
        self.addDailyData(self.buy_volume_ratio, 'fguo_1209.buy_volume_ratio')
        self.addDailyData(self.effective_spread_avg, 'fguo_1209.effective_spread_avg')
        self.addDailyData(self.intraday_momentum, 'fguo_1209.intraday_momentum')
        self.addDailyData(self.large_trade_count_ratio, 'fguo_1209.large_trade_count_ratio')
        self.addDailyData(self.large_trade_volume_ratio, 'fguo_1209.large_trade_volume_ratio')
        self.addDailyData(self.mid_price_daily_avg, 'fguo_1209.mid_price_daily_avg')
        self.addDailyData(self.mid_price_daily_max, 'fguo_1209.mid_price_daily_max')
        self.addDailyData(self.mid_price_daily_min, 'fguo_1209.mid_price_daily_min')
        self.addDailyData(self.mid_price_daily_vwap, 'fguo_1209.mid_price_daily_vwap')
        self.addDailyData(self.ofi_level1_daily_sum, 'fguo_1209.ofi_level1_daily_sum')
        self.addDailyData(self.ofi_level5_daily_sum, 'fguo_1209.ofi_level5_daily_sum')
        self.addDailyData(self.price_position_daily_avg, 'fguo_1209.price_position_daily_avg')
        self.addDailyData(self.price_position_daily_max, 'fguo_1209.price_position_daily_max')
        self.addDailyData(self.price_position_daily_min, 'fguo_1209.price_position_daily_min')
        self.addDailyData(self.price_position_daily_vw, 'fguo_1209.price_position_daily_vw')
        self.addDailyData(self.realized_volatility_daily, 'fguo_1209.realized_volatility_daily')
        self.addDailyData(self.return_autocorr, 'fguo_1209.return_autocorr')
        self.addDailyData(self.rolling_volatility_10_avg, 'fguo_1209.rolling_volatility_10_avg')
        self.addDailyData(self.rolling_volatility_10_max, 'fguo_1209.rolling_volatility_10_max')
        self.addDailyData(self.rolling_volatility_30_avg, 'fguo_1209.rolling_volatility_30_avg')
        self.addDailyData(self.rolling_volatility_30_max, 'fguo_1209.rolling_volatility_30_max')
        self.addDailyData(self.small_trade_count_ratio, 'fguo_1209.small_trade_count_ratio')
        self.addDailyData(self.small_trade_volume_ratio, 'fguo_1209.small_trade_volume_ratio')
        self.addDailyData(self.tick_count, 'fguo_1209.tick_count')
        self.addDailyData(self.trade_size_cv, 'fguo_1209.trade_size_cv')
        return

    def loadDay(self, di):
        pass
