"""Daily aggregates from official five-minute cubes for Rui features."""

import warnings

import numpy as np
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils.NioData import NIO_MATRIX


class DmgrRuiCube5mDaily(DataManagerMapped):
    def __init__(self):
        DataManagerMapped.__init__(self)
        self.cube5m_Interval5m_pctchange_tail_mean_minus_full_mean = NIO_MATRIX()
        self.cube5m_Interval5m_ret_tail_mean_minus_full_mean = NIO_MATRIX()
        self.cube5m_Interval5m_ret_upper_lower_tail_imbalance = NIO_MATRIX()
        self.cube5m_Interval5m_vwap_close_open_diff = NIO_MATRIX()
        self.cube5m_fb224_avg_imb_d10_5m_mean = NIO_MATRIX()
        self.cube5m_fb224_avg_imb_l1_5m_mean = NIO_MATRIX()
        self.cube5m_fb224_avg_imb_l1_5m_std = NIO_MATRIX()
        self.cube5m_fb224_avg_spread_rel_5m_mean = NIO_MATRIX()
        self.cube5m_fb224_book_slope_buy_5m_am_pm_diff = NIO_MATRIX()
        self.cube5m_fb224_book_slope_buy_5m_mean = NIO_MATRIX()
        self.cube5m_fb224_book_slope_buy_5m_std = NIO_MATRIX()
        self.cube5m_fb224_book_slope_sell_5m_am_pm_diff = NIO_MATRIX()
        self.cube5m_fb224_f5_tox_5m_mean = NIO_MATRIX()
        self.cube5m_fb224_f5_tox_5m_tail_mean_minus_full_mean = NIO_MATRIX()
        self.cube5m_fb224_f9_eff_spread_5m_mean = NIO_MATRIX()
        self.cube5m_fb224_large_buy_ratio_5m_am_pm_diff = NIO_MATRIX()
        self.cube5m_fb224_large_buy_ratio_5m_mean = NIO_MATRIX()
        self.cube5m_fb224_large_net_buy_5m_am_pm_diff = NIO_MATRIX()
        self.cube5m_fb224_large_net_buy_5m_mean = NIO_MATRIX()
        self.cube5m_fb224_large_net_buy_5m_tail_mean_minus_full_mean = NIO_MATRIX()
        self.cube5m_fb224_large_sell_ratio_5m_am_pm_diff = NIO_MATRIX()
        self.cube5m_fb224_large_sell_ratio_5m_mean = NIO_MATRIX()
        self.cube5m_fb224_side_switch_5m_mean = NIO_MATRIX()
        self.cube5m_fb224_vw_imb_l1_5m_std = NIO_MATRIX()
        self.cube5m_yq212_order_big_count_based_on_order_money_am_pm_diff = NIO_MATRIX()
        self.cube5m_yq212_order_big_total_money_based_on_order_money_am_pm_diff = NIO_MATRIX()
        self.cube5m_yq212_order_big_total_money_based_on_order_money_last = NIO_MATRIX()
        self.cube5m_yq212_order_big_total_money_based_on_order_money_mean = NIO_MATRIX()
        self.cube5m_yq212_order_buy_count_last = NIO_MATRIX()
        self.cube5m_yq212_order_buy_count_std = NIO_MATRIX()
        self.cube5m_yq212_order_buy_volume_am_pm_diff = NIO_MATRIX()
        self.cube5m_yq212_order_buy_volume_last = NIO_MATRIX()
        self.cube5m_yq212_order_sell_count_last = NIO_MATRIX()
        self.cube5m_yq212_order_sell_volume_std = NIO_MATRIX()
        self.cube5m_yq212_order_small_count_based_on_order_money_last = NIO_MATRIX()

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.addDailyData(
            self.cube5m_Interval5m_pctchange_tail_mean_minus_full_mean,
            self.tag + ".cube5m_Interval5m_pctchange_tail_mean_minus_full_mean",
        )
        self.addDailyData(
            self.cube5m_Interval5m_ret_tail_mean_minus_full_mean,
            self.tag + ".cube5m_Interval5m_ret_tail_mean_minus_full_mean",
        )
        self.addDailyData(
            self.cube5m_Interval5m_ret_upper_lower_tail_imbalance,
            self.tag + ".cube5m_Interval5m_ret_upper_lower_tail_imbalance",
        )
        self.addDailyData(
            self.cube5m_Interval5m_vwap_close_open_diff,
            self.tag + ".cube5m_Interval5m_vwap_close_open_diff",
        )
        self.addDailyData(
            self.cube5m_fb224_avg_imb_d10_5m_mean,
            self.tag + ".cube5m_fb224_avg_imb_d10_5m_mean",
        )
        self.addDailyData(
            self.cube5m_fb224_avg_imb_l1_5m_mean,
            self.tag + ".cube5m_fb224_avg_imb_l1_5m_mean",
        )
        self.addDailyData(
            self.cube5m_fb224_avg_imb_l1_5m_std,
            self.tag + ".cube5m_fb224_avg_imb_l1_5m_std",
        )
        self.addDailyData(
            self.cube5m_fb224_avg_spread_rel_5m_mean,
            self.tag + ".cube5m_fb224_avg_spread_rel_5m_mean",
        )
        self.addDailyData(
            self.cube5m_fb224_book_slope_buy_5m_am_pm_diff,
            self.tag + ".cube5m_fb224_book_slope_buy_5m_am_pm_diff",
        )
        self.addDailyData(
            self.cube5m_fb224_book_slope_buy_5m_mean,
            self.tag + ".cube5m_fb224_book_slope_buy_5m_mean",
        )
        self.addDailyData(
            self.cube5m_fb224_book_slope_buy_5m_std,
            self.tag + ".cube5m_fb224_book_slope_buy_5m_std",
        )
        self.addDailyData(
            self.cube5m_fb224_book_slope_sell_5m_am_pm_diff,
            self.tag + ".cube5m_fb224_book_slope_sell_5m_am_pm_diff",
        )
        self.addDailyData(
            self.cube5m_fb224_f5_tox_5m_mean,
            self.tag + ".cube5m_fb224_f5_tox_5m_mean",
        )
        self.addDailyData(
            self.cube5m_fb224_f5_tox_5m_tail_mean_minus_full_mean,
            self.tag + ".cube5m_fb224_f5_tox_5m_tail_mean_minus_full_mean",
        )
        self.addDailyData(
            self.cube5m_fb224_f9_eff_spread_5m_mean,
            self.tag + ".cube5m_fb224_f9_eff_spread_5m_mean",
        )
        self.addDailyData(
            self.cube5m_fb224_large_buy_ratio_5m_am_pm_diff,
            self.tag + ".cube5m_fb224_large_buy_ratio_5m_am_pm_diff",
        )
        self.addDailyData(
            self.cube5m_fb224_large_buy_ratio_5m_mean,
            self.tag + ".cube5m_fb224_large_buy_ratio_5m_mean",
        )
        self.addDailyData(
            self.cube5m_fb224_large_net_buy_5m_am_pm_diff,
            self.tag + ".cube5m_fb224_large_net_buy_5m_am_pm_diff",
        )
        self.addDailyData(
            self.cube5m_fb224_large_net_buy_5m_mean,
            self.tag + ".cube5m_fb224_large_net_buy_5m_mean",
        )
        self.addDailyData(
            self.cube5m_fb224_large_net_buy_5m_tail_mean_minus_full_mean,
            self.tag + ".cube5m_fb224_large_net_buy_5m_tail_mean_minus_full_mean",
        )
        self.addDailyData(
            self.cube5m_fb224_large_sell_ratio_5m_am_pm_diff,
            self.tag + ".cube5m_fb224_large_sell_ratio_5m_am_pm_diff",
        )
        self.addDailyData(
            self.cube5m_fb224_large_sell_ratio_5m_mean,
            self.tag + ".cube5m_fb224_large_sell_ratio_5m_mean",
        )
        self.addDailyData(
            self.cube5m_fb224_side_switch_5m_mean,
            self.tag + ".cube5m_fb224_side_switch_5m_mean",
        )
        self.addDailyData(
            self.cube5m_fb224_vw_imb_l1_5m_std,
            self.tag + ".cube5m_fb224_vw_imb_l1_5m_std",
        )
        self.addDailyData(
            self.cube5m_yq212_order_big_count_based_on_order_money_am_pm_diff,
            self.tag + ".cube5m_yq212_order_big_count_based_on_order_money_am_pm_diff",
        )
        self.addDailyData(
            self.cube5m_yq212_order_big_total_money_based_on_order_money_am_pm_diff,
            self.tag + ".cube5m_yq212_order_big_total_money_based_on_order_money_am_pm_diff",
        )
        self.addDailyData(
            self.cube5m_yq212_order_big_total_money_based_on_order_money_last,
            self.tag + ".cube5m_yq212_order_big_total_money_based_on_order_money_last",
        )
        self.addDailyData(
            self.cube5m_yq212_order_big_total_money_based_on_order_money_mean,
            self.tag + ".cube5m_yq212_order_big_total_money_based_on_order_money_mean",
        )
        self.addDailyData(
            self.cube5m_yq212_order_buy_count_last,
            self.tag + ".cube5m_yq212_order_buy_count_last",
        )
        self.addDailyData(
            self.cube5m_yq212_order_buy_count_std,
            self.tag + ".cube5m_yq212_order_buy_count_std",
        )
        self.addDailyData(
            self.cube5m_yq212_order_buy_volume_am_pm_diff,
            self.tag + ".cube5m_yq212_order_buy_volume_am_pm_diff",
        )
        self.addDailyData(
            self.cube5m_yq212_order_buy_volume_last,
            self.tag + ".cube5m_yq212_order_buy_volume_last",
        )
        self.addDailyData(
            self.cube5m_yq212_order_sell_count_last,
            self.tag + ".cube5m_yq212_order_sell_count_last",
        )
        self.addDailyData(
            self.cube5m_yq212_order_sell_volume_std,
            self.tag + ".cube5m_yq212_order_sell_volume_std",
        )
        self.addDailyData(
            self.cube5m_yq212_order_small_count_based_on_order_money_last,
            self.tag + ".cube5m_yq212_order_small_count_based_on_order_money_last",
        )

    def dependencies(self):
        DataManagerMapped.dependencies(self)
        dr.registerDependency(self.mid, "Interval5m.pctchange")
        dr.registerDependency(self.mid, "Interval5m.ret")
        dr.registerDependency(self.mid, "Interval5m.vwap")
        dr.registerDependency(self.mid, "fb_224_5min.avg_imb_d10_5m")
        dr.registerDependency(self.mid, "fb_224_5min.avg_imb_l1_5m")
        dr.registerDependency(self.mid, "fb_224_5min.avg_spread_rel_5m")
        dr.registerDependency(self.mid, "fb_224_5min.book_slope_buy_5m")
        dr.registerDependency(self.mid, "fb_224_5min.book_slope_sell_5m")
        dr.registerDependency(self.mid, "fb_224_5min.f5_tox_5m")
        dr.registerDependency(self.mid, "fb_224_5min.f9_eff_spread_5m")
        dr.registerDependency(self.mid, "fb_224_5min.large_buy_ratio_5m")
        dr.registerDependency(self.mid, "fb_224_5min.large_net_buy_5m")
        dr.registerDependency(self.mid, "fb_224_5min.large_sell_ratio_5m")
        dr.registerDependency(self.mid, "fb_224_5min.side_switch_5m")
        dr.registerDependency(self.mid, "fb_224_5min.vw_imb_l1_5m")
        dr.registerDependency(self.mid, "yq_212_5min.order_big_count_based_on_order_money")
        dr.registerDependency(self.mid, "yq_212_5min.order_big_total_money_based_on_order_money")
        dr.registerDependency(self.mid, "yq_212_5min.order_buy_count")
        dr.registerDependency(self.mid, "yq_212_5min.order_buy_volume")
        dr.registerDependency(self.mid, "yq_212_5min.order_sell_count")
        dr.registerDependency(self.mid, "yq_212_5min.order_sell_volume")
        dr.registerDependency(self.mid, "yq_212_5min.order_small_count_based_on_order_money")

    def loadData(self, di_start):
        self.fillnan(di_start, len(uv.Dates))
        interval5m_pctchange = dr.getData("Interval5m.pctchange").data
        interval5m_ret = dr.getData("Interval5m.ret").data
        interval5m_vwap = dr.getData("Interval5m.vwap").data
        fb_224_5min_avg_imb_d10_5m = dr.getData("fb_224_5min.avg_imb_d10_5m").data
        fb_224_5min_avg_imb_l1_5m = dr.getData("fb_224_5min.avg_imb_l1_5m").data
        fb_224_5min_avg_spread_rel_5m = dr.getData("fb_224_5min.avg_spread_rel_5m").data
        fb_224_5min_book_slope_buy_5m = dr.getData("fb_224_5min.book_slope_buy_5m").data
        fb_224_5min_book_slope_sell_5m = dr.getData("fb_224_5min.book_slope_sell_5m").data
        fb_224_5min_f5_tox_5m = dr.getData("fb_224_5min.f5_tox_5m").data
        fb_224_5min_f9_eff_spread_5m = dr.getData("fb_224_5min.f9_eff_spread_5m").data
        fb_224_5min_large_buy_ratio_5m = dr.getData("fb_224_5min.large_buy_ratio_5m").data
        fb_224_5min_large_net_buy_5m = dr.getData("fb_224_5min.large_net_buy_5m").data
        fb_224_5min_large_sell_ratio_5m = dr.getData("fb_224_5min.large_sell_ratio_5m").data
        fb_224_5min_side_switch_5m = dr.getData("fb_224_5min.side_switch_5m").data
        fb_224_5min_vw_imb_l1_5m = dr.getData("fb_224_5min.vw_imb_l1_5m").data
        yq_212_5min_order_big_count_based_on_order_money = dr.getData("yq_212_5min.order_big_count_based_on_order_money").data
        yq_212_5min_order_big_total_money_based_on_order_money = dr.getData("yq_212_5min.order_big_total_money_based_on_order_money").data
        yq_212_5min_order_buy_count = dr.getData("yq_212_5min.order_buy_count").data
        yq_212_5min_order_buy_volume = dr.getData("yq_212_5min.order_buy_volume").data
        yq_212_5min_order_sell_count = dr.getData("yq_212_5min.order_sell_count").data
        yq_212_5min_order_sell_volume = dr.getData("yq_212_5min.order_sell_volume").data
        yq_212_5min_order_small_count_based_on_order_money = dr.getData("yq_212_5min.order_small_count_based_on_order_money").data

        with warnings.catch_warnings(), np.errstate(all="ignore"):
            warnings.simplefilter("ignore", category=RuntimeWarning)
            for di in range(di_start, len(uv.Dates)):
                self.cube5m_Interval5m_pctchange_tail_mean_minus_full_mean[di] = (
                    np.nanmean(interval5m_pctchange[di, 43:49, :], axis=0)
                    - np.nanmean(interval5m_pctchange[di, 1:49, :], axis=0)
                )
                self.cube5m_Interval5m_ret_tail_mean_minus_full_mean[di] = (
                    np.nanmean(interval5m_ret[di, 43:49, :], axis=0)
                    - np.nanmean(interval5m_ret[di, 1:49, :], axis=0)
                )
                self.cube5m_Interval5m_ret_upper_lower_tail_imbalance[di] = (
                    np.nanmean(interval5m_ret[di, 37:49, :], axis=0)
                    - np.nanmean(interval5m_ret[di, 1:13, :], axis=0)
                )
                self.cube5m_Interval5m_vwap_close_open_diff[di] = interval5m_vwap[di, 48, :] - interval5m_vwap[di, 1, :]
                self.cube5m_fb224_avg_imb_d10_5m_mean[di] = np.nanmean(fb_224_5min_avg_imb_d10_5m[di, 1:49, :], axis=0)
                self.cube5m_fb224_avg_imb_l1_5m_mean[di] = np.nanmean(fb_224_5min_avg_imb_l1_5m[di, 1:49, :], axis=0)
                self.cube5m_fb224_avg_imb_l1_5m_std[di] = np.nanstd(fb_224_5min_avg_imb_l1_5m[di, 1:49, :], axis=0)
                self.cube5m_fb224_avg_spread_rel_5m_mean[di] = np.nanmean(fb_224_5min_avg_spread_rel_5m[di, 1:49, :], axis=0)
                self.cube5m_fb224_book_slope_buy_5m_am_pm_diff[di] = (
                    np.nanmean(fb_224_5min_book_slope_buy_5m[di, 25:49, :], axis=0)
                    - np.nanmean(fb_224_5min_book_slope_buy_5m[di, 1:25, :], axis=0)
                )
                self.cube5m_fb224_book_slope_buy_5m_mean[di] = np.nanmean(fb_224_5min_book_slope_buy_5m[di, 1:49, :], axis=0)
                self.cube5m_fb224_book_slope_buy_5m_std[di] = np.nanstd(fb_224_5min_book_slope_buy_5m[di, 1:49, :], axis=0)
                self.cube5m_fb224_book_slope_sell_5m_am_pm_diff[di] = (
                    np.nanmean(fb_224_5min_book_slope_sell_5m[di, 25:49, :], axis=0)
                    - np.nanmean(fb_224_5min_book_slope_sell_5m[di, 1:25, :], axis=0)
                )
                self.cube5m_fb224_f5_tox_5m_mean[di] = np.nanmean(fb_224_5min_f5_tox_5m[di, 1:49, :], axis=0)
                self.cube5m_fb224_f5_tox_5m_tail_mean_minus_full_mean[di] = (
                    np.nanmean(fb_224_5min_f5_tox_5m[di, 43:49, :], axis=0)
                    - np.nanmean(fb_224_5min_f5_tox_5m[di, 1:49, :], axis=0)
                )
                self.cube5m_fb224_f9_eff_spread_5m_mean[di] = np.nanmean(fb_224_5min_f9_eff_spread_5m[di, 1:49, :], axis=0)
                self.cube5m_fb224_large_buy_ratio_5m_am_pm_diff[di] = (
                    np.nanmean(fb_224_5min_large_buy_ratio_5m[di, 25:49, :], axis=0)
                    - np.nanmean(fb_224_5min_large_buy_ratio_5m[di, 1:25, :], axis=0)
                )
                self.cube5m_fb224_large_buy_ratio_5m_mean[di] = np.nanmean(fb_224_5min_large_buy_ratio_5m[di, 1:49, :], axis=0)
                self.cube5m_fb224_large_net_buy_5m_am_pm_diff[di] = (
                    np.nanmean(fb_224_5min_large_net_buy_5m[di, 25:49, :], axis=0)
                    - np.nanmean(fb_224_5min_large_net_buy_5m[di, 1:25, :], axis=0)
                )
                self.cube5m_fb224_large_net_buy_5m_mean[di] = np.nanmean(fb_224_5min_large_net_buy_5m[di, 1:49, :], axis=0)
                self.cube5m_fb224_large_net_buy_5m_tail_mean_minus_full_mean[di] = (
                    np.nanmean(fb_224_5min_large_net_buy_5m[di, 43:49, :], axis=0)
                    - np.nanmean(fb_224_5min_large_net_buy_5m[di, 1:49, :], axis=0)
                )
                self.cube5m_fb224_large_sell_ratio_5m_am_pm_diff[di] = (
                    np.nanmean(fb_224_5min_large_sell_ratio_5m[di, 25:49, :], axis=0)
                    - np.nanmean(fb_224_5min_large_sell_ratio_5m[di, 1:25, :], axis=0)
                )
                self.cube5m_fb224_large_sell_ratio_5m_mean[di] = np.nanmean(fb_224_5min_large_sell_ratio_5m[di, 1:49, :], axis=0)
                self.cube5m_fb224_side_switch_5m_mean[di] = np.nanmean(fb_224_5min_side_switch_5m[di, 1:49, :], axis=0)
                self.cube5m_fb224_vw_imb_l1_5m_std[di] = np.nanstd(fb_224_5min_vw_imb_l1_5m[di, 1:49, :], axis=0)
                self.cube5m_yq212_order_big_count_based_on_order_money_am_pm_diff[di] = (
                    np.nanmean(yq_212_5min_order_big_count_based_on_order_money[di, 25:49, :], axis=0)
                    - np.nanmean(yq_212_5min_order_big_count_based_on_order_money[di, 1:25, :], axis=0)
                )
                self.cube5m_yq212_order_big_total_money_based_on_order_money_am_pm_diff[di] = (
                    np.nanmean(yq_212_5min_order_big_total_money_based_on_order_money[di, 25:49, :], axis=0)
                    - np.nanmean(yq_212_5min_order_big_total_money_based_on_order_money[di, 1:25, :], axis=0)
                )
                self.cube5m_yq212_order_big_total_money_based_on_order_money_last[di] = yq_212_5min_order_big_total_money_based_on_order_money[di, 48, :]
                self.cube5m_yq212_order_big_total_money_based_on_order_money_mean[di] = np.nanmean(yq_212_5min_order_big_total_money_based_on_order_money[di, 1:49, :], axis=0)
                self.cube5m_yq212_order_buy_count_last[di] = yq_212_5min_order_buy_count[di, 48, :]
                self.cube5m_yq212_order_buy_count_std[di] = np.nanstd(yq_212_5min_order_buy_count[di, 1:49, :], axis=0)
                self.cube5m_yq212_order_buy_volume_am_pm_diff[di] = (
                    np.nanmean(yq_212_5min_order_buy_volume[di, 25:49, :], axis=0)
                    - np.nanmean(yq_212_5min_order_buy_volume[di, 1:25, :], axis=0)
                )
                self.cube5m_yq212_order_buy_volume_last[di] = yq_212_5min_order_buy_volume[di, 48, :]
                self.cube5m_yq212_order_sell_count_last[di] = yq_212_5min_order_sell_count[di, 48, :]
                self.cube5m_yq212_order_sell_volume_std[di] = np.nanstd(yq_212_5min_order_sell_volume[di, 1:49, :], axis=0)
                self.cube5m_yq212_order_small_count_based_on_order_money_last[di] = yq_212_5min_order_small_count_based_on_order_money[di, 48, :]

                print(f"[{self.tag}] Updated on day {uv.Dates[di]}")
