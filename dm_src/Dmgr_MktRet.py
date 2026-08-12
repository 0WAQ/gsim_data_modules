from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
import numpy as np

class Dmgr_MktRet(DataManagerMapped):
    """
    全市场平均收益率统计
    逻辑：
    1. 使用 ALL_TRD 确定当日交易股票
    2. 使用 ashareeodprices.s_dq_pctchange 计算收益
    3. 剔除异常值：仅保留 [-20%, 20%] 之间的收益率数据 (interpret: kick out outliers outside +/- 20%)
    4. 计算全市场等权平均
    """

    def __init__(self):
        DataManagerMapped.__init__(self)
        self.market_avg_ret = NIO_VECTOR()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        # 按照新要求注册名称：模块名.数据名
        self.addDailyData(self.market_avg_ret, "Dmgr_MktRet.mkt_avg_ret")
        return

    def dependencies(self):
        DataManagerMapped.dependencies(self)

        # 涨跌幅
        dr.registerDependency(self.mid, 'ashareeodprices.s_dq_pctchange')

        # 全市场交易状态 (ALL_TRD 文件夹下的 ALL_TRD.npy)
        dr.registerDependency(self.mid, 'ALL_TRD')
        return

    def loadData(self, di_start):
        self.fillnan(di_start, len(uv.Dates))

        # 获取数据句柄
        d_pct = dr.getData('ashareeodprices.s_dq_pctchange')
        d_trd = dr.getData('ALL_TRD')

        print(f'[{self.tag}] Calculating Market Average Return...')

        for di in range(di_start, len(uv.Dates)):
            if di % 100 == 0:
                print(f'[{self.tag}] Processing {uv.Dates[di]}')

            # 获取当日数据 (1D numpy array)
            daily_pct = d_pct[di]
            #print (daily_pct)
            daily_trd = d_trd[di]

            # 构建有效性掩码
            # 1. 必须在 ALL_TRD 中 (假设 > 0 为真)
            # 2. 收益率必须在 [-20, 20] 之间 (剔除异常值)
            # 3. 收益率非 NaN
            with np.errstate(invalid='ignore'):
                mask_valid = (daily_trd > 0) & \
                             (daily_pct >= -0.2) & \
                             (daily_pct <= 0.2) & \
                             (~np.isnan(daily_pct))

            # 计算平均值
            if np.any(mask_valid):
                avg_ret = np.mean(daily_pct[mask_valid])
            else:
                avg_ret = np.nan

            # 将标量广播到当日所有股票 (Market Factor)
            # 即使个股当日无交易，也填充市场当天的平均收益作为参考
            # 或者仅填充 mask_valid 的部分？通常市场因子会对全截面赋值
            #res_arr = np.full_like(daily_pct, avg_ret)

            self.market_avg_ret[di] = avg_ret#res_arr

        return
