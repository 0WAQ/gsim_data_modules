from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv


class DmgrLhw_L2FeatureCuts1430(DataManagerMapped):
    def __init__(self):
        DataManagerMapped.__init__(self)
        self.buy_amt_h4 = NIO_MATRIX()
        self.buy_amt_ratio_h4 = NIO_MATRIX()
        self.buy_sell_vol_ratio_h4 = NIO_MATRIX()
        self.buy_vol_h4 = NIO_MATRIX()
        self.consec_trade_ratio = NIO_MATRIX()
        self.downshadow_am_avg_5d = NIO_MATRIX()
        self.downshadow_daily_avg_5d = NIO_MATRIX()
        self.downshadow_daily_std_5d = NIO_MATRIX()
        self.downshadow_open30_avg_5d = NIO_MATRIX()
        self.downshadow_pm_avg_5d = NIO_MATRIX()
        self.extreme_ret_mean = NIO_MATRIX()
        self.high_ret_to_preclose = NIO_MATRIX()
        self.minute_ret_vol_of_vol = NIO_MATRIX()
        self.minute_vol_cv = NIO_MATRIX()
        self.ob_count_imb_l5_h4 = NIO_MATRIX()
        self.ob_level_imb_h3 = NIO_MATRIX()
        self.ob_level_imb_h4 = NIO_MATRIX()
        self.ob_level_imb_pm = NIO_MATRIX()
        self.order_size_l1_l5_ratio = NIO_MATRIX()
        self.price_vol_corr = NIO_MATRIX()
        self.range_efficiency_h4 = NIO_MATRIX()
        self.ret_to_preclose = NIO_MATRIX()
        self.sell_amt_ratio_h4 = NIO_MATRIX()
        self.sell_depth_l1_ratio = NIO_MATRIX()
        self.small_order_imb_h1_h4_diff = NIO_MATRIX()
        self.small_order_imb_h3 = NIO_MATRIX()
        self.small_order_imb_h4 = NIO_MATRIX()
        self.trade_size_hvol_lvol_ratio = NIO_MATRIX()
        self.unknown_side_ratio = NIO_MATRIX()
        self.vol_wtd_ret_p95_h4 = NIO_MATRIX()
        self.vol_wtd_ret_p95_pm = NIO_MATRIX()
        self.vwap_close_ratio = NIO_MATRIX()

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.addDailyData(self.buy_amt_h4, "feature_cuts_1430.buy_amt_h4")
        self.addDailyData(self.buy_amt_ratio_h4, "feature_cuts_1430.buy_amt_ratio_h4")
        self.addDailyData(self.buy_sell_vol_ratio_h4, "feature_cuts_1430.buy_sell_vol_ratio_h4")
        self.addDailyData(self.buy_vol_h4, "feature_cuts_1430.buy_vol_h4")
        self.addDailyData(self.consec_trade_ratio, "feature_cuts_1430.consec_trade_ratio")
        self.addDailyData(self.downshadow_am_avg_5d, "feature_cuts_1430.downshadow_am_avg_5d")
        self.addDailyData(self.downshadow_daily_avg_5d, "feature_cuts_1430.downshadow_daily_avg_5d")
        self.addDailyData(self.downshadow_daily_std_5d, "feature_cuts_1430.downshadow_daily_std_5d")
        self.addDailyData(self.downshadow_open30_avg_5d, "feature_cuts_1430.downshadow_open30_avg_5d")
        self.addDailyData(self.downshadow_pm_avg_5d, "feature_cuts_1430.downshadow_pm_avg_5d")
        self.addDailyData(self.extreme_ret_mean, "feature_cuts_1430.extreme_ret_mean")
        self.addDailyData(self.high_ret_to_preclose, "feature_cuts_1430.high_ret_to_preclose")
        self.addDailyData(self.minute_ret_vol_of_vol, "feature_cuts_1430.minute_ret_vol_of_vol")
        self.addDailyData(self.minute_vol_cv, "feature_cuts_1430.minute_vol_cv")
        self.addDailyData(self.ob_count_imb_l5_h4, "feature_cuts_1430.ob_count_imb_l5_h4")
        self.addDailyData(self.ob_level_imb_h3, "feature_cuts_1430.ob_level_imb_h3")
        self.addDailyData(self.ob_level_imb_h4, "feature_cuts_1430.ob_level_imb_h4")
        self.addDailyData(self.ob_level_imb_pm, "feature_cuts_1430.ob_level_imb_pm")
        self.addDailyData(self.order_size_l1_l5_ratio, "feature_cuts_1430.order_size_l1_l5_ratio")
        self.addDailyData(self.price_vol_corr, "feature_cuts_1430.price_vol_corr")
        self.addDailyData(self.range_efficiency_h4, "feature_cuts_1430.range_efficiency_h4")
        self.addDailyData(self.ret_to_preclose, "feature_cuts_1430.ret_to_preclose")
        self.addDailyData(self.sell_amt_ratio_h4, "feature_cuts_1430.sell_amt_ratio_h4")
        self.addDailyData(self.sell_depth_l1_ratio, "feature_cuts_1430.sell_depth_l1_ratio")
        self.addDailyData(self.small_order_imb_h1_h4_diff, "feature_cuts_1430.small_order_imb_h1_h4_diff")
        self.addDailyData(self.small_order_imb_h3, "feature_cuts_1430.small_order_imb_h3")
        self.addDailyData(self.small_order_imb_h4, "feature_cuts_1430.small_order_imb_h4")
        self.addDailyData(self.trade_size_hvol_lvol_ratio, "feature_cuts_1430.trade_size_hvol_lvol_ratio")
        self.addDailyData(self.unknown_side_ratio, "feature_cuts_1430.unknown_side_ratio")
        self.addDailyData(self.vol_wtd_ret_p95_h4, "feature_cuts_1430.vol_wtd_ret_p95_h4")
        self.addDailyData(self.vol_wtd_ret_p95_pm, "feature_cuts_1430.vol_wtd_ret_p95_pm")
        self.addDailyData(self.vwap_close_ratio, "feature_cuts_1430.vwap_close_ratio")

    def loadDay(self, di):
        pass


DmgrFeatureCuts1430 = DmgrLhw_L2FeatureCuts1430
