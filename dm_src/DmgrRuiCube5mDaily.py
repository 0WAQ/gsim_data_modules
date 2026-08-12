"""Direct daily aggregates from the official Interval5m cube."""

import warnings

import numpy as np
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils.NioData import NIO_MATRIX


FEATURE_NAMES = (
    "cube5m_Interval5m_ret_upper_lower_tail_imbalance",
    "cube5m_Interval5m_pctchange_tail_mean_minus_full_mean",
    "cube5m_Interval5m_ret_tail_mean_minus_full_mean",
    "cube5m_Interval5m_vwap_close_open_diff",
)


def nanmean(values):
    with np.errstate(invalid="ignore", divide="ignore"), warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        return np.nanmean(values, axis=0)


class DmgrRuiCube5mDaily(DataManagerMapped):
    def __init__(self):
        DataManagerMapped.__init__(self)
        self.ret_upper_lower_tail_imbalance = NIO_MATRIX()
        self.pctchange_tail_mean_minus_full_mean = NIO_MATRIX()
        self.ret_tail_mean_minus_full_mean = NIO_MATRIX()
        self.vwap_close_open_diff = NIO_MATRIX()

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.addDailyData(
            self.ret_upper_lower_tail_imbalance,
            self.tag + ".cube5m_Interval5m_ret_upper_lower_tail_imbalance",
        )
        self.addDailyData(
            self.pctchange_tail_mean_minus_full_mean,
            self.tag + ".cube5m_Interval5m_pctchange_tail_mean_minus_full_mean",
        )
        self.addDailyData(
            self.ret_tail_mean_minus_full_mean,
            self.tag + ".cube5m_Interval5m_ret_tail_mean_minus_full_mean",
        )
        self.addDailyData(
            self.vwap_close_open_diff,
            self.tag + ".cube5m_Interval5m_vwap_close_open_diff",
        )

    def dependencies(self):
        DataManagerMapped.dependencies(self)
        dr.registerDependency(self.mid, "Interval5m.ret")
        dr.registerDependency(self.mid, "Interval5m.pctchange")
        dr.registerDependency(self.mid, "Interval5m.vwap")

    def loadData(self, di_start):
        self.fillnan(di_start, len(uv.Dates))
        ret = dr.getData("Interval5m.ret")
        pctchange = dr.getData("Interval5m.pctchange")
        vwap = dr.getData("Interval5m.vwap")

        for di in range(di_start, len(uv.Dates)):
            ret_5m = np.asarray(ret[di], dtype=np.float64)
            pctchange_5m = np.asarray(pctchange[di], dtype=np.float64)
            vwap_5m = np.asarray(vwap[di], dtype=np.float64)

            self.ret_upper_lower_tail_imbalance[di] = (
                nanmean(ret_5m[37:49]) - nanmean(ret_5m[1:13])
            )
            self.pctchange_tail_mean_minus_full_mean[di] = (
                nanmean(pctchange_5m[43:49]) - nanmean(pctchange_5m[1:49])
            )
            self.ret_tail_mean_minus_full_mean[di] = (
                nanmean(ret_5m[43:49]) - nanmean(ret_5m[1:49])
            )
            self.vwap_close_open_diff[di] = vwap_5m[48] - vwap_5m[1]

