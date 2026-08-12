"""Cross-sectional transforms built directly from official five-minute cubes."""

import warnings

import numpy as np
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils.NioData import NIO_MATRIX


FEATURE_NAMES = (
    "r05_active_small_big_buy_spread_z",
    "r09_micro_close_replenish_p01_c0_ratio_z",
)


def nanmean(values):
    with np.errstate(invalid="ignore", divide="ignore"), warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        return np.nanmean(values, axis=0)


def zscore(row):
    values = np.asarray(row, dtype=np.float64)
    finite = np.isfinite(values)
    if int(finite.sum()) < 25:
        return np.full(values.shape, np.nan, dtype=np.float64)
    sigma = float(np.std(values[finite]))
    if not np.isfinite(sigma) or sigma <= 1e-12:
        return np.full(values.shape, np.nan, dtype=np.float64)
    result = (values - float(np.mean(values[finite]))) / sigma
    result[~finite] = np.nan
    return np.clip(result, -10.0, 10.0)


def stabilized_ratio(numerator, denominator):
    numerator_z = zscore(numerator)
    denominator_z = zscore(denominator)
    sign = np.where(denominator_z >= 0.0, 1.0, -1.0)
    denominator_floor = sign * np.maximum(np.abs(denominator_z), 0.25)
    return zscore(numerator_z / denominator_floor)


class DmgrRuiCrossSection5m(DataManagerMapped):
    def __init__(self):
        DataManagerMapped.__init__(self)
        self.active_small_big_buy_spread_z = NIO_MATRIX()
        self.micro_close_replenish_ratio_z = NIO_MATRIX()

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.addDailyData(
            self.active_small_big_buy_spread_z,
            self.tag + ".r05_active_small_big_buy_spread_z",
        )
        self.addDailyData(
            self.micro_close_replenish_ratio_z,
            self.tag + ".r09_micro_close_replenish_p01_c0_ratio_z",
        )

    def dependencies(self):
        DataManagerMapped.dependencies(self)
        dr.registerDependency(self.mid, "dw_57_5min.activebuy_small_order_amount_5")
        dr.registerDependency(self.mid, "dw_57_5min.activebuy_big_order_amount_20")
        dr.registerDependency(self.mid, "Interval5m.vwap")
        dr.registerDependency(self.mid, "fb_224_5min.mx_liq_score_5m")

    def loadData(self, di_start):
        self.fillnan(di_start, len(uv.Dates))
        activebuy_small = dr.getData("dw_57_5min.activebuy_small_order_amount_5")
        activebuy_big = dr.getData("dw_57_5min.activebuy_big_order_amount_20")
        vwap = dr.getData("Interval5m.vwap")
        liquidity_score = dr.getData("fb_224_5min.mx_liq_score_5m")

        for di in range(di_start, len(uv.Dates)):
            activebuy_small_mean = nanmean(
                np.asarray(activebuy_small[di], dtype=np.float64)[1:49]
            )
            activebuy_big_mean = nanmean(
                np.asarray(activebuy_big[di], dtype=np.float64)[1:49]
            )
            vwap_5m = np.asarray(vwap[di], dtype=np.float64)
            liquidity_score_5m = np.asarray(liquidity_score[di], dtype=np.float64)

            self.active_small_big_buy_spread_z[di] = zscore(
                zscore(activebuy_small_mean) - zscore(activebuy_big_mean)
            )
            self.micro_close_replenish_ratio_z[di] = stabilized_ratio(
                vwap_5m[48] - vwap_5m[1],
                liquidity_score_5m[48],
            )

