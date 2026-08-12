"""
DmgrWangpy_FancyIndustry.py

行业因子聚合数据模块 —— 将 81 个筛选后的通联 equ_fancy_factors 因子，
按 Wind industry(64) 分类 + log1p(cap) 加权聚合 + 截面 z-score，
输出 81 个独立的行业因子 NIO 矩阵 + 1 个等权平均 combo 信号。

使用方式 (XML):
    <Data id="DmgrWangpy_FancyIndustry"
          module="/path/to/DmgrWangpy_FancyIndustry.py"
          niodatapath="/path/to/cache/" niomapprivate="true"/>

调用方式 (Alpha 或其他模块):
    # 单因子
    signal = dr.getData('DmgrWangpy_FancyIndustry.t5_ast_rpt_sentiment_w')
    # combo
    combo  = dr.getData('DmgrWangpy_FancyIndustry.combo')

输出: 82 个 NIO_MATRIX (dates × stocks), z-scored + clip [-3, 3]
作者: wangpy
"""
from gsim.utils.NioData import NIO_MATRIX
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
import numpy as np


# ── 81 个筛选因子 (mode2 Sharpe > 0.7, mode1 Sharpe >= 0) ──────────────────
SELECTED_FACTORS = [
    (5, 'AST_RPT_SENTIMENT_W'), (4, 'P_REPORT_DIFF'),
    (3, 'HK_HOLDRATIO_C'), (3, 'HK_HOLDRATIO_B'),
    (1, 'CORR_VP'), (9, 'GTRA_SELL_PCT_VOL'),
    (3, 'HK_HOLDRATIO_ALL'), (4, 'HK_HOLDVOL_CHG_ALL120'),
    (5, 'AST_RPT_SENTIMENT_Z365'), (6, 'FF3R2_20'),
    (1, 'SUDE'), (7, 'GB_POST_NUM_DA30'),
    (9, 'GTRA_BUY_PCT_VOL'), (4, 'HK_HOLDVOL_CHG_B120'),
    (5, 'AST_RPT_SENTIMENT_Z730'), (3, 'FUND_TOP10_NEGVALUE_PCT'),
    (8, 'CON_DTOP_DA90'), (1, 'SUDREV'),
    (8, 'GROWTH_QQC'), (7, 'FUND_TRACTION_20'),
    (3, 'AST_DA12_ETOP'), (4, 'HK_HOLDVOL_CHG_C60'),
    (7, 'GB_POST_NUM_60'), (1, 'OCFA'),
    (4, 'P_REPORT_DATE'), (7, 'REV_Q_ACC'),
    (7, 'PROFIT_TREND'), (4, 'HK_HOLDVOL_CHG_ALL60'),
    (5, 'FMZL_1Y_OWNPARENT_SUM'), (7, 'GB_POST_NUM_90'),
    (9, 'GPOST_POS_PCT_VOL'), (2, 'CON_REV_YOY'),
    (6, 'FF3SPMOM_20'), (2, 'D_Q_STOP'),
    (3, 'AST_PROFIT_UPPCT'), (1, 'NP_TTM_QOQ'),
    (5, 'AST_RPT_SENTIMENT_Z180'), (8, 'GOVERNANCE'),
    (5, 'AI_DA_PS_90'), (5, 'FMZL_1Y_REVIEWDAY_SUM'),
    (7, 'GB_POST_NUM_30'), (8, 'CON_DTOP_DA30'),
    (5, 'AI_DA_PS_60'), (9, 'NEWS_NUM_VOL_30'),
    (9, 'NEWS_NUM_POS_VOL_30'), (2, 'CON_SUDREV'),
    (3, 'FUND_TOP10_WEIGHT_MAX'), (7, 'FUND_TRACTION_60'),
    (1, 'TA_ENTROPY'), (3, 'CON_DA_PE_60'),
    (6, 'OVAL_MBSR_20D'), (8, 'AI_DTOP_DA90'),
    (9, 'XTRA_SELL_PCT'), (2, 'AI_NP_YOY'),
    (6, 'FF3SYSVOL_20'), (9, 'NEWS_NUM_30'),
    (10, 'ART_Q_YOYD'), (10, 'OPER_L_QOQ'),
    (7, 'NP_Q_ACC'), (6, 'MINTVAL_MTE_20D'),
    (9, 'GPOST_HOT'), (2, 'CON_SUDE'),
    (4, 'HK_HOLDVOL_CHG_B60'), (3, 'FUND_TOP10_WEIGHT_MEAN'),
    (9, 'GPOST_NEG_PCT_VOL'), (10, 'GR_PCF_TTM'),
    (10, 'GR_PCF_Q'), (10, 'STATIC_NOTE_RATIO'),
    (8, 'CON_DTOP_Z180'), (3, 'CON_DA_PS_40'),
    (5, 'AI_DA_PE_90'), (8, 'CFP_TTM_STD'),
    (10, 'GR_PE_Q'), (1, 'UDSL_UCL'),
    (2, 'CON_NP_YOY'), (3, 'NAIVE_WEIGHT_CHANGE_ASYM'),
    (10, 'FAT_Q_YOYD'), (2, 'ROE_TTM_YOYD'),
    (2, 'AI_SUDE'), (5, 'FMZL_1Y_RELATEDNUM_SUM'),
    (7, 'SUR_EVENT'),
]


def _factor_tag(tid, fname):
    """t5_AST_RPT_SENTIMENT_W → t5_ast_rpt_sentiment_w"""
    return f't{tid}_{fname}'.lower()


class DmgrPwang_industry_equ_fancy_factors(DataManagerMapped):

    def __init__(self):
        DataManagerMapped.__init__(self)

        # 81 个独立因子输出
        self.factor_matrices = {}
        for tid, fname in SELECTED_FACTORS:
            tag = _factor_tag(tid, fname)
            mat = NIO_MATRIX()
            setattr(self, tag, mat)
            self.factor_matrices[tag] = mat

        # combo 输出
        self.combo = NIO_MATRIX()

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)

        # 注册 81 个独立因子
        for tag, mat in self.factor_matrices.items():
            self.addDailyData(mat, f'{self.tag}.{tag}')

        # 注册 combo
        self.addDailyData(self.combo, f'{self.tag}.combo')

        print(f"[{self.tag}] DmgrWangpy_FancyIndustry: "
              f"{len(SELECTED_FACTORS)} factors + combo, "
              f"industry × log1p(cap) aggregation")

    def dependencies(self):
        DataManagerMapped.dependencies(self)
        dr.registerDependency(self.mid, 'industry')
        dr.registerDependency(self.mid, 'cap')
        dr.registerDependency(self.mid, 'ALL_TRD')
        for tid, fname in SELECTED_FACTORS:
            dr.registerDependency(self.mid, f'equ_fancy_factors_table{tid}.{fname}')

    def loadData(self, di_start):
        self.fillnan(di_start, len(uv.Dates))

        d_industry = dr.getData('industry').data
        d_cap = dr.getData('cap').data
        d_trd = dr.getData('ALL_TRD').data

        # 预加载因子数据引用 + 输出矩阵引用
        factor_mats = []
        out_matrices = []
        for tid, fname in SELECTED_FACTORS:
            factor_mats.append(dr.getData(f'equ_fancy_factors_table{tid}.{fname}').data)
            out_matrices.append(self.factor_matrices[_factor_tag(tid, fname)])

        n_factors = len(factor_mats)
        L = len(uv.Instruments)

        print(f"[{self.tag}] 开始计算: {n_factors} factors + combo", flush=True)

        for di in range(di_start, len(uv.Dates)):
            if di < 256:
                continue
            if di % 500 == 0:
                print(f"[{self.tag}] di={di}, date={uv.Dates[di]}", flush=True)

            industry = d_industry[di]
            caps_raw = d_cap[di - 1]
            trd = d_trd[di]

            signals = np.full((n_factors, L), np.nan)

            for fi, fmat in enumerate(factor_mats):
                agg = self._industry_agg(fmat[di], industry, caps_raw, trd, L)
                signals[fi] = agg
                # 写入该因子的独立 NIO
                out_matrices[fi][di] = agg

            # combo = 等权平均 + z-score
            with np.errstate(all='ignore'):
                combo_val = np.nanmean(signals, axis=0)
            self.combo[di] = self._zscore(combo_val)

            print(f"{self.tag} finished on {uv.Dates[di]}")

    # ── 单因子行业聚合 ──────────────────────────────────────────────────

    def _industry_agg(self, feat, industry, caps_raw, trd, L):
        out = np.full(L, np.nan)

        ok = (~np.isnan(feat)) & (trd != 0) & (industry > 0)
        ok_idx = np.where(ok)[0]
        if len(ok_idx) == 0:
            return out

        caps_ok = caps_raw[ok_idx]
        global_cap_mean = np.nanmean(caps_ok) if not np.all(np.isnan(caps_ok)) else 0.0

        ind_vals = industry[ok_idx]
        for ind in np.unique(ind_vals[ind_vals > 0]):
            mask = (ind_vals == ind)
            g_idx = ok_idx[mask]
            g_feat = feat[g_idx]
            g_caps = caps_raw[g_idx].copy()

            nan_c = np.isnan(g_caps)
            if np.any(nan_c):
                fill = np.nanmean(g_caps) if not np.all(nan_c) else global_cap_mean
                if np.isnan(fill):
                    continue
                g_caps[nan_c] = fill

            g_caps = np.maximum(g_caps, 0.0)
            if g_caps.sum() <= 0:
                continue

            w = np.log1p(g_caps)
            if w.sum() <= 0:
                continue
            w /= w.sum()

            out[g_idx] = np.sum(g_feat * w)

        return self._zscore(out)

    @staticmethod
    def _zscore(vals):
        valid = ~np.isnan(vals)
        if valid.sum() < 2:
            return vals
        mu, sigma = vals[valid].mean(), vals[valid].std()
        if sigma > 1e-8:
            vals[valid] = np.clip((vals[valid] - mu) / sigma, -3.0, 3.0)
        else:
            vals[valid] = 0.0
        return vals
