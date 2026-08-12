
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrequ_factor_af(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = True
        self.avg_order_size_ratio = NIO_MATRIX()
        self.close_30min_net_buy = NIO_MATRIX()
        self.rolling_volatility_10_max = NIO_MATRIX()
        self.price_range = NIO_MATRIX()
        self.avg_trade_volume = NIO_MATRIX()
        self.return_daily = NIO_MATRIX()
        self.retail_vs_institution = NIO_MATRIX()
        self.buy_sell_amount_ratio = NIO_MATRIX()
        self.side_switch_count = NIO_MATRIX()
        self.price_low = NIO_MATRIX()
        self.vwap = NIO_MATRIX()
        self.vw_imbalance_depth10 = NIO_MATRIX()
        self.trade_amount_kurt = NIO_MATRIX()
        self.small_avg_vs_total = NIO_MATRIX()
        self.amount_per_trade = NIO_MATRIX()
        self.large_avg_vs_total = NIO_MATRIX()
        self.avg_mid_price = NIO_MATRIX()
        self.buy_amount_ratio = NIO_MATRIX()
        self.large_small_amount_ratio = NIO_MATRIX()
        self.intraday_momentum = NIO_MATRIX()
        self.trade_amount_std = NIO_MATRIX()
        self.mid_price_daily_min = NIO_MATRIX()
        self.trade_amount_skew = NIO_MATRIX()
        self.avg_book_slope_buy = NIO_MATRIX()
        self.net_buy_ratio = NIO_MATRIX()
        self.sell_avg_amount = NIO_MATRIX()
        self.close_30min_large_ratio = NIO_MATRIX()
        self.buy_sell_volume_ratio = NIO_MATRIX()
        self.avg_trade_amount = NIO_MATRIX()
        self.price_position = NIO_MATRIX()
        self.avg_wt_price_deviation_buy = NIO_MATRIX()
        self.vw_spread_relative = NIO_MATRIX()
        self.buy_trade_count_ratio = NIO_MATRIX()
        self.vw_imbalance_depth5 = NIO_MATRIX()
        self.unknown_side_ratio = NIO_MATRIX()
        self.buy_count_ratio = NIO_MATRIX()
        self.sell_amount_ratio = NIO_MATRIX()
        self.avg_micro_price = NIO_MATRIX()
        self.volume_per_trade = NIO_MATRIX()
        self.median_trade_amount = NIO_MATRIX()
        self.large_buy_ratio = NIO_MATRIX()
        self.price_position_daily_avg = NIO_MATRIX()
        self.fill_ratio = NIO_MATRIX()
        self.cancel_volume_ratio = NIO_MATRIX()
        self.avg_imbalance_level1 = NIO_MATRIX()
        self.buy_avg_amount = NIO_MATRIX()
        self.morning_net_buy = NIO_MATRIX()
        self.mid_price_daily_max = NIO_MATRIX()
        self.large_order_ratio = NIO_MATRIX()
        self.large_trade_volume_ratio = NIO_MATRIX()
        self.large_trade_avg_amount = NIO_MATRIX()
        self.open_close_buy_diff = NIO_MATRIX()
        self.avg_imbalance_depth5 = NIO_MATRIX()
        self.open_vs_vwap = NIO_MATRIX()
        self.ofi_level1_daily_sum = NIO_MATRIX()
        self.xlarge_order_ratio = NIO_MATRIX()
        self.realized_volatility_daily = NIO_MATRIX()
        self.small_trade_count_ratio = NIO_MATRIX()
        self.consecutive_buy_max = NIO_MATRIX()
        self.rolling_volatility_30_avg = NIO_MATRIX()
        self.large_order_count = NIO_MATRIX()
        self.avg_price_dispersion_sell = NIO_MATRIX()
        self.trade_count = NIO_MATRIX()
        self.price_position_daily_vw = NIO_MATRIX()
        self.rolling_volatility_30_max = NIO_MATRIX()
        self.trade_size_cv = NIO_MATRIX()
        self.large_net_buy = NIO_MATRIX()
        self.open_position = NIO_MATRIX()
        self.total_volume = NIO_MATRIX()
        self.ofi_level5_daily_sum = NIO_MATRIX()
        self.avg_trade_size = NIO_MATRIX()
        self.avg_spread_absolute = NIO_MATRIX()
        self.vw_imbalance_level1 = NIO_MATRIX()
        self.open_30min_net_buy = NIO_MATRIX()
        self.open_30min_large_ratio = NIO_MATRIX()
        self.total_trade_count = NIO_MATRIX()
        self.net_buy_volume_ratio = NIO_MATRIX()
        self.avg_price_stddev_sell = NIO_MATRIX()
        self.low_vs_vwap = NIO_MATRIX()
        self.intraday_volatility = NIO_MATRIX()
        self.large_trade_count_ratio = NIO_MATRIX()
        self.close_vs_vwap = NIO_MATRIX()
        self.high_vs_vwap = NIO_MATRIX()
        self.afternoon_net_buy = NIO_MATRIX()
        self.mid_price_daily_vwap = NIO_MATRIX()
        self.avg_spread_level_10 = NIO_MATRIX()
        self.small_order_ratio = NIO_MATRIX()
        self.buy_sell_avg_ratio = NIO_MATRIX()
        self.avg_wt_price_deviation_sell = NIO_MATRIX()
        self.price_position_daily_min = NIO_MATRIX()
        self.avg_spread_level_5 = NIO_MATRIX()
        self.buy_volume_ratio = NIO_MATRIX()
        self.trade_size_dispersion = NIO_MATRIX()
        self.avg_imbalance_weighted = NIO_MATRIX()
        self.cancel_ratio = NIO_MATRIX()
        self.consecutive_sell_max = NIO_MATRIX()
        self.price_position_daily_max = NIO_MATRIX()
        self.total_amount = NIO_MATRIX()
        self.avg_spread_relative = NIO_MATRIX()
        self.price_high = NIO_MATRIX()
        self.return_autocorr = NIO_MATRIX()
        self.large_sell_ratio = NIO_MATRIX()
        self.price_close = NIO_MATRIX()
        self.kyle_lambda = NIO_MATRIX()
        self.tick_count = NIO_MATRIX()
        self.small_trade_avg_amount = NIO_MATRIX()
        self.avg_price_dispersion_buy = NIO_MATRIX()
        self.avg_imbalance_depth10 = NIO_MATRIX()
        self.amihud_illiquidity = NIO_MATRIX()
        self.rolling_volatility_10_avg = NIO_MATRIX()
        self.price_open = NIO_MATRIX()
        self.small_trade_volume_ratio = NIO_MATRIX()
        self.mid_price_daily_avg = NIO_MATRIX()
        self.buy_sell_count_ratio = NIO_MATRIX()
        self.avg_price_stddev_buy = NIO_MATRIX()
        self.vw_spread_absolute = NIO_MATRIX()
        self.volume_volatility = NIO_MATRIX()
        self.avg_book_slope_sell = NIO_MATRIX()
        self.smart_money_flow = NIO_MATRIX()
        self.effective_spread_avg = NIO_MATRIX()
        self.volume_concentration = NIO_MATRIX()
        self.daily_vwap = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', True)
        self.addDailyData(self.avg_order_size_ratio,self.tag + '.avg_order_size_ratio')
        self.addDailyData(self.close_30min_net_buy,self.tag + '.close_30min_net_buy')
        self.addDailyData(self.rolling_volatility_10_max,self.tag + '.rolling_volatility_10_max')
        self.addDailyData(self.price_range,self.tag + '.price_range')
        self.addDailyData(self.avg_trade_volume,self.tag + '.avg_trade_volume')
        self.addDailyData(self.return_daily,self.tag + '.return_daily')
        self.addDailyData(self.retail_vs_institution,self.tag + '.retail_vs_institution')
        self.addDailyData(self.buy_sell_amount_ratio,self.tag + '.buy_sell_amount_ratio')
        self.addDailyData(self.side_switch_count,self.tag + '.side_switch_count')
        self.addDailyData(self.price_low,self.tag + '.price_low')
        self.addDailyData(self.vwap,self.tag + '.vwap')
        self.addDailyData(self.vw_imbalance_depth10,self.tag + '.vw_imbalance_depth10')
        self.addDailyData(self.trade_amount_kurt,self.tag + '.trade_amount_kurt')
        self.addDailyData(self.small_avg_vs_total,self.tag + '.small_avg_vs_total')
        self.addDailyData(self.amount_per_trade,self.tag + '.amount_per_trade')
        self.addDailyData(self.large_avg_vs_total,self.tag + '.large_avg_vs_total')
        self.addDailyData(self.avg_mid_price,self.tag + '.avg_mid_price')
        self.addDailyData(self.buy_amount_ratio,self.tag + '.buy_amount_ratio')
        self.addDailyData(self.large_small_amount_ratio,self.tag + '.large_small_amount_ratio')
        self.addDailyData(self.intraday_momentum,self.tag + '.intraday_momentum')
        self.addDailyData(self.trade_amount_std,self.tag + '.trade_amount_std')
        self.addDailyData(self.mid_price_daily_min,self.tag + '.mid_price_daily_min')
        self.addDailyData(self.trade_amount_skew,self.tag + '.trade_amount_skew')
        self.addDailyData(self.avg_book_slope_buy,self.tag + '.avg_book_slope_buy')
        self.addDailyData(self.net_buy_ratio,self.tag + '.net_buy_ratio')
        self.addDailyData(self.sell_avg_amount,self.tag + '.sell_avg_amount')
        self.addDailyData(self.close_30min_large_ratio,self.tag + '.close_30min_large_ratio')
        self.addDailyData(self.buy_sell_volume_ratio,self.tag + '.buy_sell_volume_ratio')
        self.addDailyData(self.avg_trade_amount,self.tag + '.avg_trade_amount')
        self.addDailyData(self.price_position,self.tag + '.price_position')
        self.addDailyData(self.avg_wt_price_deviation_buy,self.tag + '.avg_wt_price_deviation_buy')
        self.addDailyData(self.vw_spread_relative,self.tag + '.vw_spread_relative')
        self.addDailyData(self.buy_trade_count_ratio,self.tag + '.buy_trade_count_ratio')
        self.addDailyData(self.vw_imbalance_depth5,self.tag + '.vw_imbalance_depth5')
        self.addDailyData(self.unknown_side_ratio,self.tag + '.unknown_side_ratio')
        self.addDailyData(self.buy_count_ratio,self.tag + '.buy_count_ratio')
        self.addDailyData(self.sell_amount_ratio,self.tag + '.sell_amount_ratio')
        self.addDailyData(self.avg_micro_price,self.tag + '.avg_micro_price')
        self.addDailyData(self.volume_per_trade,self.tag + '.volume_per_trade')
        self.addDailyData(self.median_trade_amount,self.tag + '.median_trade_amount')
        self.addDailyData(self.large_buy_ratio,self.tag + '.large_buy_ratio')
        self.addDailyData(self.price_position_daily_avg,self.tag + '.price_position_daily_avg')
        self.addDailyData(self.fill_ratio,self.tag + '.fill_ratio')
        self.addDailyData(self.cancel_volume_ratio,self.tag + '.cancel_volume_ratio')
        self.addDailyData(self.avg_imbalance_level1,self.tag + '.avg_imbalance_level1')
        self.addDailyData(self.buy_avg_amount,self.tag + '.buy_avg_amount')
        self.addDailyData(self.morning_net_buy,self.tag + '.morning_net_buy')
        self.addDailyData(self.mid_price_daily_max,self.tag + '.mid_price_daily_max')
        self.addDailyData(self.large_order_ratio,self.tag + '.large_order_ratio')
        self.addDailyData(self.large_trade_volume_ratio,self.tag + '.large_trade_volume_ratio')
        self.addDailyData(self.large_trade_avg_amount,self.tag + '.large_trade_avg_amount')
        self.addDailyData(self.open_close_buy_diff,self.tag + '.open_close_buy_diff')
        self.addDailyData(self.avg_imbalance_depth5,self.tag + '.avg_imbalance_depth5')
        self.addDailyData(self.open_vs_vwap,self.tag + '.open_vs_vwap')
        self.addDailyData(self.ofi_level1_daily_sum,self.tag + '.ofi_level1_daily_sum')
        self.addDailyData(self.xlarge_order_ratio,self.tag + '.xlarge_order_ratio')
        self.addDailyData(self.realized_volatility_daily,self.tag + '.realized_volatility_daily')
        self.addDailyData(self.small_trade_count_ratio,self.tag + '.small_trade_count_ratio')
        self.addDailyData(self.consecutive_buy_max,self.tag + '.consecutive_buy_max')
        self.addDailyData(self.rolling_volatility_30_avg,self.tag + '.rolling_volatility_30_avg')
        self.addDailyData(self.large_order_count,self.tag + '.large_order_count')
        self.addDailyData(self.avg_price_dispersion_sell,self.tag + '.avg_price_dispersion_sell')
        self.addDailyData(self.trade_count,self.tag + '.trade_count')
        self.addDailyData(self.price_position_daily_vw,self.tag + '.price_position_daily_vw')
        self.addDailyData(self.rolling_volatility_30_max,self.tag + '.rolling_volatility_30_max')
        self.addDailyData(self.trade_size_cv,self.tag + '.trade_size_cv')
        self.addDailyData(self.large_net_buy,self.tag + '.large_net_buy')
        self.addDailyData(self.open_position,self.tag + '.open_position')
        self.addDailyData(self.total_volume,self.tag + '.total_volume')
        self.addDailyData(self.ofi_level5_daily_sum,self.tag + '.ofi_level5_daily_sum')
        self.addDailyData(self.avg_trade_size,self.tag + '.avg_trade_size')
        self.addDailyData(self.avg_spread_absolute,self.tag + '.avg_spread_absolute')
        self.addDailyData(self.vw_imbalance_level1,self.tag + '.vw_imbalance_level1')
        self.addDailyData(self.open_30min_net_buy,self.tag + '.open_30min_net_buy')
        self.addDailyData(self.open_30min_large_ratio,self.tag + '.open_30min_large_ratio')
        self.addDailyData(self.total_trade_count,self.tag + '.total_trade_count')
        self.addDailyData(self.net_buy_volume_ratio,self.tag + '.net_buy_volume_ratio')
        self.addDailyData(self.avg_price_stddev_sell,self.tag + '.avg_price_stddev_sell')
        self.addDailyData(self.low_vs_vwap,self.tag + '.low_vs_vwap')
        self.addDailyData(self.intraday_volatility,self.tag + '.intraday_volatility')
        self.addDailyData(self.large_trade_count_ratio,self.tag + '.large_trade_count_ratio')
        self.addDailyData(self.close_vs_vwap,self.tag + '.close_vs_vwap')
        self.addDailyData(self.high_vs_vwap,self.tag + '.high_vs_vwap')
        self.addDailyData(self.afternoon_net_buy,self.tag + '.afternoon_net_buy')
        self.addDailyData(self.mid_price_daily_vwap,self.tag + '.mid_price_daily_vwap')
        self.addDailyData(self.avg_spread_level_10,self.tag + '.avg_spread_level_10')
        self.addDailyData(self.small_order_ratio,self.tag + '.small_order_ratio')
        self.addDailyData(self.buy_sell_avg_ratio,self.tag + '.buy_sell_avg_ratio')
        self.addDailyData(self.avg_wt_price_deviation_sell,self.tag + '.avg_wt_price_deviation_sell')
        self.addDailyData(self.price_position_daily_min,self.tag + '.price_position_daily_min')
        self.addDailyData(self.avg_spread_level_5,self.tag + '.avg_spread_level_5')
        self.addDailyData(self.buy_volume_ratio,self.tag + '.buy_volume_ratio')
        self.addDailyData(self.trade_size_dispersion,self.tag + '.trade_size_dispersion')
        self.addDailyData(self.avg_imbalance_weighted,self.tag + '.avg_imbalance_weighted')
        self.addDailyData(self.cancel_ratio,self.tag + '.cancel_ratio')
        self.addDailyData(self.consecutive_sell_max,self.tag + '.consecutive_sell_max')
        self.addDailyData(self.price_position_daily_max,self.tag + '.price_position_daily_max')
        self.addDailyData(self.total_amount,self.tag + '.total_amount')
        self.addDailyData(self.avg_spread_relative,self.tag + '.avg_spread_relative')
        self.addDailyData(self.price_high,self.tag + '.price_high')
        self.addDailyData(self.return_autocorr,self.tag + '.return_autocorr')
        self.addDailyData(self.large_sell_ratio,self.tag + '.large_sell_ratio')
        self.addDailyData(self.price_close,self.tag + '.price_close')
        self.addDailyData(self.kyle_lambda,self.tag + '.kyle_lambda')
        self.addDailyData(self.tick_count,self.tag + '.tick_count')
        self.addDailyData(self.small_trade_avg_amount,self.tag + '.small_trade_avg_amount')
        self.addDailyData(self.avg_price_dispersion_buy,self.tag + '.avg_price_dispersion_buy')
        self.addDailyData(self.avg_imbalance_depth10,self.tag + '.avg_imbalance_depth10')
        self.addDailyData(self.amihud_illiquidity,self.tag + '.amihud_illiquidity')
        self.addDailyData(self.rolling_volatility_10_avg,self.tag + '.rolling_volatility_10_avg')
        self.addDailyData(self.price_open,self.tag + '.price_open')
        self.addDailyData(self.small_trade_volume_ratio,self.tag + '.small_trade_volume_ratio')
        self.addDailyData(self.mid_price_daily_avg,self.tag + '.mid_price_daily_avg')
        self.addDailyData(self.buy_sell_count_ratio,self.tag + '.buy_sell_count_ratio')
        self.addDailyData(self.avg_price_stddev_buy,self.tag + '.avg_price_stddev_buy')
        self.addDailyData(self.vw_spread_absolute,self.tag + '.vw_spread_absolute')
        self.addDailyData(self.volume_volatility,self.tag + '.volume_volatility')
        self.addDailyData(self.avg_book_slope_sell,self.tag + '.avg_book_slope_sell')
        self.addDailyData(self.smart_money_flow,self.tag + '.smart_money_flow')
        self.addDailyData(self.effective_spread_avg,self.tag + '.effective_spread_avg')
        self.addDailyData(self.volume_concentration,self.tag + '.volume_concentration')
        self.addDailyData(self.daily_vwap,self.tag + '.daily_vwap')
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
            ticker = linespt[4][0:6]
            ii = uv.Instruments.lookup(ticker)
            if ii < 0:
                continue
            self.avg_order_size_ratio[di, ii]  = float(linespt[0])
            self.close_30min_net_buy[di, ii]  = float(linespt[1])
            self.rolling_volatility_10_max[di, ii]  = float(linespt[2])
            self.price_range[di, ii]  = float(linespt[3])
            self.avg_trade_volume[di, ii]  = float(linespt[4])
            self.return_daily[di, ii]  = float(linespt[5])
            self.retail_vs_institution[di, ii]  = float(linespt[6])
            self.buy_sell_amount_ratio[di, ii]  = float(linespt[7])
            self.side_switch_count[di, ii]  = float(linespt[8])
            self.price_low[di, ii]  = float(linespt[9])
            self.vwap[di, ii]  = float(linespt[10])
            self.vw_imbalance_depth10[di, ii]  = float(linespt[11])
            self.trade_amount_kurt[di, ii]  = float(linespt[12])
            self.small_avg_vs_total[di, ii]  = float(linespt[13])
            self.amount_per_trade[di, ii]  = float(linespt[14])
            self.large_avg_vs_total[di, ii]  = float(linespt[15])
            self.avg_mid_price[di, ii]  = float(linespt[16])
            self.buy_amount_ratio[di, ii]  = float(linespt[17])
            self.large_small_amount_ratio[di, ii]  = float(linespt[18])
            self.intraday_momentum[di, ii]  = float(linespt[19])
            self.trade_amount_std[di, ii]  = float(linespt[20])
            self.mid_price_daily_min[di, ii]  = float(linespt[21])
            self.trade_amount_skew[di, ii]  = float(linespt[22])
            self.avg_book_slope_buy[di, ii]  = float(linespt[24])
            self.net_buy_ratio[di, ii]  = float(linespt[25])
            self.sell_avg_amount[di, ii]  = float(linespt[26])
            self.close_30min_large_ratio[di, ii]  = float(linespt[27])
            self.buy_sell_volume_ratio[di, ii]  = float(linespt[28])
            self.avg_trade_amount[di, ii]  = float(linespt[29])
            self.price_position[di, ii]  = float(linespt[30])
            self.avg_wt_price_deviation_buy[di, ii]  = float(linespt[31])
            self.vw_spread_relative[di, ii]  = float(linespt[32])
            self.buy_trade_count_ratio[di, ii]  = float(linespt[33])
            self.vw_imbalance_depth5[di, ii]  = float(linespt[34])
            self.unknown_side_ratio[di, ii]  = float(linespt[35])
            self.buy_count_ratio[di, ii]  = float(linespt[36])
            self.sell_amount_ratio[di, ii]  = float(linespt[37])
            self.avg_micro_price[di, ii]  = float(linespt[38])
            self.volume_per_trade[di, ii]  = float(linespt[39])
            self.median_trade_amount[di, ii]  = float(linespt[40])
            self.large_buy_ratio[di, ii]  = float(linespt[41])
            self.price_position_daily_avg[di, ii]  = float(linespt[42])
            self.fill_ratio[di, ii]  = float(linespt[43])
            self.cancel_volume_ratio[di, ii]  = float(linespt[44])
            self.avg_imbalance_level1[di, ii]  = float(linespt[45])
            self.buy_avg_amount[di, ii]  = float(linespt[46])
            self.morning_net_buy[di, ii]  = float(linespt[47])
            self.mid_price_daily_max[di, ii]  = float(linespt[48])
            self.large_order_ratio[di, ii]  = float(linespt[49])
            self.large_trade_volume_ratio[di, ii]  = float(linespt[50])
            self.large_trade_avg_amount[di, ii]  = float(linespt[51])
            self.open_close_buy_diff[di, ii]  = float(linespt[52])
            self.avg_imbalance_depth5[di, ii]  = float(linespt[53])
            self.open_vs_vwap[di, ii]  = float(linespt[54])
            self.ofi_level1_daily_sum[di, ii]  = float(linespt[55])
            self.xlarge_order_ratio[di, ii]  = float(linespt[56])
            self.realized_volatility_daily[di, ii]  = float(linespt[57])
            self.small_trade_count_ratio[di, ii]  = float(linespt[58])
            self.consecutive_buy_max[di, ii]  = float(linespt[59])
            self.rolling_volatility_30_avg[di, ii]  = float(linespt[60])
            self.large_order_count[di, ii]  = float(linespt[61])
            self.avg_price_dispersion_sell[di, ii]  = float(linespt[62])
            self.trade_count[di, ii]  = float(linespt[63])
            self.price_position_daily_vw[di, ii]  = float(linespt[64])
            self.rolling_volatility_30_max[di, ii]  = float(linespt[65])
            self.trade_size_cv[di, ii]  = float(linespt[66])
            self.large_net_buy[di, ii]  = float(linespt[67])
            self.open_position[di, ii]  = float(linespt[68])
            self.total_volume[di, ii]  = float(linespt[69])
            self.ofi_level5_daily_sum[di, ii]  = float(linespt[70])
            self.avg_trade_size[di, ii]  = float(linespt[71])
            self.avg_spread_absolute[di, ii]  = float(linespt[72])
            self.vw_imbalance_level1[di, ii]  = float(linespt[73])
            self.open_30min_net_buy[di, ii]  = float(linespt[74])
            self.open_30min_large_ratio[di, ii]  = float(linespt[75])
            self.total_trade_count[di, ii]  = float(linespt[76])
            self.net_buy_volume_ratio[di, ii]  = float(linespt[77])
            self.avg_price_stddev_sell[di, ii]  = float(linespt[78])
            self.low_vs_vwap[di, ii]  = float(linespt[79])
            self.intraday_volatility[di, ii]  = float(linespt[80])
            self.large_trade_count_ratio[di, ii]  = float(linespt[81])
            self.close_vs_vwap[di, ii]  = float(linespt[82])
            self.high_vs_vwap[di, ii]  = float(linespt[83])
            self.afternoon_net_buy[di, ii]  = float(linespt[84])
            self.mid_price_daily_vwap[di, ii]  = float(linespt[85])
            self.avg_spread_level_10[di, ii]  = float(linespt[86])
            self.small_order_ratio[di, ii]  = float(linespt[87])
            self.buy_sell_avg_ratio[di, ii]  = float(linespt[88])
            self.avg_wt_price_deviation_sell[di, ii]  = float(linespt[89])
            self.price_position_daily_min[di, ii]  = float(linespt[90])
            self.avg_spread_level_5[di, ii]  = float(linespt[91])
            self.buy_volume_ratio[di, ii]  = float(linespt[92])
            self.trade_size_dispersion[di, ii]  = float(linespt[93])
            self.avg_imbalance_weighted[di, ii]  = float(linespt[94])
            self.cancel_ratio[di, ii]  = float(linespt[95])
            self.consecutive_sell_max[di, ii]  = float(linespt[96])
            self.price_position_daily_max[di, ii]  = float(linespt[97])
            self.total_amount[di, ii]  = float(linespt[98])
            self.avg_spread_relative[di, ii]  = float(linespt[99])
            self.price_high[di, ii]  = float(linespt[100])
            self.return_autocorr[di, ii]  = float(linespt[101])
            self.large_sell_ratio[di, ii]  = float(linespt[102])
            self.price_close[di, ii]  = float(linespt[103])
            self.kyle_lambda[di, ii]  = float(linespt[104])
            self.tick_count[di, ii]  = float(linespt[105])
            self.small_trade_avg_amount[di, ii]  = float(linespt[106])
            self.avg_price_dispersion_buy[di, ii]  = float(linespt[107])
            self.avg_imbalance_depth10[di, ii]  = float(linespt[108])
            self.amihud_illiquidity[di, ii]  = float(linespt[109])
            self.rolling_volatility_10_avg[di, ii]  = float(linespt[110])
            self.price_open[di, ii]  = float(linespt[111])
            self.small_trade_volume_ratio[di, ii]  = float(linespt[112])
            self.mid_price_daily_avg[di, ii]  = float(linespt[113])
            self.buy_sell_count_ratio[di, ii]  = float(linespt[114])
            self.avg_price_stddev_buy[di, ii]  = float(linespt[115])
            self.vw_spread_absolute[di, ii]  = float(linespt[116])
            self.volume_volatility[di, ii]  = float(linespt[117])
            self.avg_book_slope_sell[di, ii]  = float(linespt[118])
            self.smart_money_flow[di, ii]  = float(linespt[119])
            self.effective_spread_avg[di, ii]  = float(linespt[120])
            self.volume_concentration[di, ii]  = float(linespt[121])
            self.daily_vwap[di, ii]  = float(linespt[122])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.avg_order_size_ratio[di] = self.avg_order_size_ratio[di - 1]
        self.close_30min_net_buy[di] = self.close_30min_net_buy[di - 1]
        self.rolling_volatility_10_max[di] = self.rolling_volatility_10_max[di - 1]
        self.price_range[di] = self.price_range[di - 1]
        self.avg_trade_volume[di] = self.avg_trade_volume[di - 1]
        self.return_daily[di] = self.return_daily[di - 1]
        self.retail_vs_institution[di] = self.retail_vs_institution[di - 1]
        self.buy_sell_amount_ratio[di] = self.buy_sell_amount_ratio[di - 1]
        self.side_switch_count[di] = self.side_switch_count[di - 1]
        self.price_low[di] = self.price_low[di - 1]
        self.vwap[di] = self.vwap[di - 1]
        self.vw_imbalance_depth10[di] = self.vw_imbalance_depth10[di - 1]
        self.trade_amount_kurt[di] = self.trade_amount_kurt[di - 1]
        self.small_avg_vs_total[di] = self.small_avg_vs_total[di - 1]
        self.amount_per_trade[di] = self.amount_per_trade[di - 1]
        self.large_avg_vs_total[di] = self.large_avg_vs_total[di - 1]
        self.avg_mid_price[di] = self.avg_mid_price[di - 1]
        self.buy_amount_ratio[di] = self.buy_amount_ratio[di - 1]
        self.large_small_amount_ratio[di] = self.large_small_amount_ratio[di - 1]
        self.intraday_momentum[di] = self.intraday_momentum[di - 1]
        self.trade_amount_std[di] = self.trade_amount_std[di - 1]
        self.mid_price_daily_min[di] = self.mid_price_daily_min[di - 1]
        self.trade_amount_skew[di] = self.trade_amount_skew[di - 1]
        self.avg_book_slope_buy[di] = self.avg_book_slope_buy[di - 1]
        self.net_buy_ratio[di] = self.net_buy_ratio[di - 1]
        self.sell_avg_amount[di] = self.sell_avg_amount[di - 1]
        self.close_30min_large_ratio[di] = self.close_30min_large_ratio[di - 1]
        self.buy_sell_volume_ratio[di] = self.buy_sell_volume_ratio[di - 1]
        self.avg_trade_amount[di] = self.avg_trade_amount[di - 1]
        self.price_position[di] = self.price_position[di - 1]
        self.avg_wt_price_deviation_buy[di] = self.avg_wt_price_deviation_buy[di - 1]
        self.vw_spread_relative[di] = self.vw_spread_relative[di - 1]
        self.buy_trade_count_ratio[di] = self.buy_trade_count_ratio[di - 1]
        self.vw_imbalance_depth5[di] = self.vw_imbalance_depth5[di - 1]
        self.unknown_side_ratio[di] = self.unknown_side_ratio[di - 1]
        self.buy_count_ratio[di] = self.buy_count_ratio[di - 1]
        self.sell_amount_ratio[di] = self.sell_amount_ratio[di - 1]
        self.avg_micro_price[di] = self.avg_micro_price[di - 1]
        self.volume_per_trade[di] = self.volume_per_trade[di - 1]
        self.median_trade_amount[di] = self.median_trade_amount[di - 1]
        self.large_buy_ratio[di] = self.large_buy_ratio[di - 1]
        self.price_position_daily_avg[di] = self.price_position_daily_avg[di - 1]
        self.fill_ratio[di] = self.fill_ratio[di - 1]
        self.cancel_volume_ratio[di] = self.cancel_volume_ratio[di - 1]
        self.avg_imbalance_level1[di] = self.avg_imbalance_level1[di - 1]
        self.buy_avg_amount[di] = self.buy_avg_amount[di - 1]
        self.morning_net_buy[di] = self.morning_net_buy[di - 1]
        self.mid_price_daily_max[di] = self.mid_price_daily_max[di - 1]
        self.large_order_ratio[di] = self.large_order_ratio[di - 1]
        self.large_trade_volume_ratio[di] = self.large_trade_volume_ratio[di - 1]
        self.large_trade_avg_amount[di] = self.large_trade_avg_amount[di - 1]
        self.open_close_buy_diff[di] = self.open_close_buy_diff[di - 1]
        self.avg_imbalance_depth5[di] = self.avg_imbalance_depth5[di - 1]
        self.open_vs_vwap[di] = self.open_vs_vwap[di - 1]
        self.ofi_level1_daily_sum[di] = self.ofi_level1_daily_sum[di - 1]
        self.xlarge_order_ratio[di] = self.xlarge_order_ratio[di - 1]
        self.realized_volatility_daily[di] = self.realized_volatility_daily[di - 1]
        self.small_trade_count_ratio[di] = self.small_trade_count_ratio[di - 1]
        self.consecutive_buy_max[di] = self.consecutive_buy_max[di - 1]
        self.rolling_volatility_30_avg[di] = self.rolling_volatility_30_avg[di - 1]
        self.large_order_count[di] = self.large_order_count[di - 1]
        self.avg_price_dispersion_sell[di] = self.avg_price_dispersion_sell[di - 1]
        self.trade_count[di] = self.trade_count[di - 1]
        self.price_position_daily_vw[di] = self.price_position_daily_vw[di - 1]
        self.rolling_volatility_30_max[di] = self.rolling_volatility_30_max[di - 1]
        self.trade_size_cv[di] = self.trade_size_cv[di - 1]
        self.large_net_buy[di] = self.large_net_buy[di - 1]
        self.open_position[di] = self.open_position[di - 1]
        self.total_volume[di] = self.total_volume[di - 1]
        self.ofi_level5_daily_sum[di] = self.ofi_level5_daily_sum[di - 1]
        self.avg_trade_size[di] = self.avg_trade_size[di - 1]
        self.avg_spread_absolute[di] = self.avg_spread_absolute[di - 1]
        self.vw_imbalance_level1[di] = self.vw_imbalance_level1[di - 1]
        self.open_30min_net_buy[di] = self.open_30min_net_buy[di - 1]
        self.open_30min_large_ratio[di] = self.open_30min_large_ratio[di - 1]
        self.total_trade_count[di] = self.total_trade_count[di - 1]
        self.net_buy_volume_ratio[di] = self.net_buy_volume_ratio[di - 1]
        self.avg_price_stddev_sell[di] = self.avg_price_stddev_sell[di - 1]
        self.low_vs_vwap[di] = self.low_vs_vwap[di - 1]
        self.intraday_volatility[di] = self.intraday_volatility[di - 1]
        self.large_trade_count_ratio[di] = self.large_trade_count_ratio[di - 1]
        self.close_vs_vwap[di] = self.close_vs_vwap[di - 1]
        self.high_vs_vwap[di] = self.high_vs_vwap[di - 1]
        self.afternoon_net_buy[di] = self.afternoon_net_buy[di - 1]
        self.mid_price_daily_vwap[di] = self.mid_price_daily_vwap[di - 1]
        self.avg_spread_level_10[di] = self.avg_spread_level_10[di - 1]
        self.small_order_ratio[di] = self.small_order_ratio[di - 1]
        self.buy_sell_avg_ratio[di] = self.buy_sell_avg_ratio[di - 1]
        self.avg_wt_price_deviation_sell[di] = self.avg_wt_price_deviation_sell[di - 1]
        self.price_position_daily_min[di] = self.price_position_daily_min[di - 1]
        self.avg_spread_level_5[di] = self.avg_spread_level_5[di - 1]
        self.buy_volume_ratio[di] = self.buy_volume_ratio[di - 1]
        self.trade_size_dispersion[di] = self.trade_size_dispersion[di - 1]
        self.avg_imbalance_weighted[di] = self.avg_imbalance_weighted[di - 1]
        self.cancel_ratio[di] = self.cancel_ratio[di - 1]
        self.consecutive_sell_max[di] = self.consecutive_sell_max[di - 1]
        self.price_position_daily_max[di] = self.price_position_daily_max[di - 1]
        self.total_amount[di] = self.total_amount[di - 1]
        self.avg_spread_relative[di] = self.avg_spread_relative[di - 1]
        self.price_high[di] = self.price_high[di - 1]
        self.return_autocorr[di] = self.return_autocorr[di - 1]
        self.large_sell_ratio[di] = self.large_sell_ratio[di - 1]
        self.price_close[di] = self.price_close[di - 1]
        self.kyle_lambda[di] = self.kyle_lambda[di - 1]
        self.tick_count[di] = self.tick_count[di - 1]
        self.small_trade_avg_amount[di] = self.small_trade_avg_amount[di - 1]
        self.avg_price_dispersion_buy[di] = self.avg_price_dispersion_buy[di - 1]
        self.avg_imbalance_depth10[di] = self.avg_imbalance_depth10[di - 1]
        self.amihud_illiquidity[di] = self.amihud_illiquidity[di - 1]
        self.rolling_volatility_10_avg[di] = self.rolling_volatility_10_avg[di - 1]
        self.price_open[di] = self.price_open[di - 1]
        self.small_trade_volume_ratio[di] = self.small_trade_volume_ratio[di - 1]
        self.mid_price_daily_avg[di] = self.mid_price_daily_avg[di - 1]
        self.buy_sell_count_ratio[di] = self.buy_sell_count_ratio[di - 1]
        self.avg_price_stddev_buy[di] = self.avg_price_stddev_buy[di - 1]
        self.vw_spread_absolute[di] = self.vw_spread_absolute[di - 1]
        self.volume_volatility[di] = self.volume_volatility[di - 1]
        self.avg_book_slope_sell[di] = self.avg_book_slope_sell[di - 1]
        self.smart_money_flow[di] = self.smart_money_flow[di - 1]
        self.effective_spread_avg[di] = self.effective_spread_avg[di - 1]
        self.volume_concentration[di] = self.volume_concentration[di - 1]
        self.daily_vwap[di] = self.daily_vwap[di - 1]
