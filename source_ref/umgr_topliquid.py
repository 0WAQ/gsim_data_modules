from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import Universe as uv
from gsim.data import DataRegistry as dr
from gsim.utils import Config, Oputil
import numpy as np
import sys
import pandas as pd


class UmgrTopliquid(DataManagerMapped):
    def __init__(self, ):
        super().__init__()
        self.backdays = None
        self.univsize = None
        self.volwindow = None
        self.minprice = None
        self.maxprice = None
        self.minvol = None
        self.mincap = None
        self.minlive = None
        self.delay = None
        self.exst = None
        self.postipo = None
        self.ex300x = None
        self.exkcb = None
        self.valid = NIO_MATRIX(NIO_BOOL)

        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.backdays = Config(cfg.getConfig().getroottree().find('Constants')).getAttribute('backdays')
        self.univsize = cfg.getAttributeDefault('univsize', 500)
        self.volwindow = cfg.getAttributeDefault('volwindow', 63)
        self.minprice = cfg.getAttributeDefault('minprice', 1.0)
        self.maxprice = cfg.getAttributeDefault('maxprice', 1000.0)
        self.minvol = cfg.getAttributeDefault('minvol', 0.)
        self.mincap = cfg.getAttributeDefault('mincap', 0.)
        self.minlive = cfg.getAttributeDefault('minlive', 1)
        self.delay = cfg.getAttributeDefault('delay', 1)
        self.exst = cfg.getAttributeDefault('exst', True)
        self.postipo = cfg.getAttributeDefault('postipo', 200)
        self.ex300x = cfg.getAttributeDefault('ex300x', False)
        self.exkcb = cfg.getAttributeDefault('exkcb', False)
        self.addParamMetaData(self.univsize, 'univsize')
        self.addParamMetaData(self.volwindow, 'volwindow')
        self.addParamMetaData(self.maxprice, 'maxprice')
        self.addParamMetaData(self.minprice, 'minprice')
        self.addParamMetaData(self.minvol, 'minvol')
        self.addParamMetaData(self.mincap, 'mincap')
        self.addParamMetaData(self.minlive, 'minlive')
        self.addParamMetaData(self.delay, 'delay')
        self.addParamMetaData(self.exst, 'exst')
        self.addParamMetaData(self.postipo, 'postipo')
        self.addParamMetaData(self.ex300x, 'ex300x')
        self.addParamMetaData(self.exkcb, 'exkcb')

        self.addDailyData(self.valid, self.tag)
        return

    def dependencies(self, ):
        dr.registerDependency(self.mid, 'amount')
        dr.registerDependency(self.mid, 'capfree')
        dr.registerDependency(self.mid, 'st')
        # dr.registerDependency(self.mid, 'adj_close')
        dr.registerDependency(self.mid, 'close')  # do not use adj price in dmgr
        dr.registerDependency(self.mid, 'adjfactor')
        dr.registerDependency(self.mid, 'ipodate')
        dr.registerDependency(self.mid, 'ZZ500')
        dr.registerDependency(self.mid, 'HS300')
        return

    def loadData(self, di_start):
        if self.backdays < self.volwindow:
            print('UmgrTopliquid: backdays < volwindow')
            sys.exit(1)
        self.fillnan(di_start, len(uv.Dates))  # set default value
        amo = dr.getData('amount')
        cap = dr.getData('capfree')
        st = dr.getData('st')
        # cps = dr.getData('adj_close')
        rawcps = dr.getData('close')
        adj = dr.getData('adjfactor')
        ipd = dr.getData('ipodate')
        zz500 = dr.getData('ZZ500')
        hs300 = dr.getData('HS300')
        di_work = max(di_start, self.volwindow + self.delay - 1)
        for di in range(di_work, len(uv.Dates)):
            bm = amo[di - self.delay - self.volwindow + 1:di - self.delay + 1] > 0
            a = np.copy(amo[di - self.delay - self.volwindow + 1:di - self.delay + 1])
            # c  = np.copy(cps[di-self.delay-self.volwindow+1:di-self.delay+1])
            cumAdj = np.full((self.volwindow, len(uv.Instruments)), 1.0)
            for bd in range(self.volwindow-1): # 20210228
                cumAdj[self.volwindow - bd - 2, :] *= adj[di - bd - 1, :]
            c = rawcps[di - self.delay - self.volwindow + 1:di - self.delay + 1, :] * cumAdj[:, :]
            ca = np.copy(cap[di - self.delay - self.volwindow + 1:di - self.delay + 1])
            a[~bm] = np.nan
            c[~bm] = np.nan
            ca[~bm] = np.nan
            avg_vol = Oputil.mean(a)
            avg_cps = Oputil.mean(c)
            avg_cap = Oputil.mean(ca)
            avg_vol[avg_cps < self.minprice] = np.nan
            avg_vol[avg_cps > self.maxprice] = np.nan
            avg_vol[avg_vol < self.minvol] = np.nan
            avg_vol[avg_cap < self.mincap] = np.nan
            cnt = np.sum(bm, axis=0)
            avg_vol[cnt < self.minlive] = np.nan  # filter halted stocks
            if self.exst:
                avg_vol[st[di - self.delay]] = np.nan  # ST yesterday
            avg_vol[~(amo[di - self.delay] > 0)] = np.nan  # halted yesterday
            nd = np.full(len(uv.Instruments), 0, dtype=np.int32)
            is300x = np.full(len(uv.Instruments), False, dtype=np.bool)
            iskcb = np.full(len(uv.Instruments), False, dtype=np.bool)
            for ii in range(len(uv.Instruments)):
                # start = ipd[ii]
                # end = uv.Dates[di]
                start = '%04d-%02d-%02d' % (ipd[ii] // 10000, (ipd[ii] % 10000) // 100, ipd[ii] % 100)
                end = '%04d-%02d-%02d' % (uv.Dates[di] // 10000, (uv.Dates[di] % 10000) // 100, uv.Dates[di] % 100)
                d = np.busday_count(np.datetime64(start), np.datetime64(end))
                nd[ii] = d
                if uv.Instruments[ii][0:2] == '30':
                    is300x[ii] = True
                if uv.Instruments[ii][0:2] == '68':
                    iskcb[ii] = True
            avg_vol[ nd < self.postipo ] = np.nan # new stocks
            if self.ex300x:
                avg_vol[is300x & ~hs300[di] & ~zz500[di]] = np.nan  # exclude 300xxx
            if self.exkcb:
                avg_vol[iskcb & ~hs300[di] & ~zz500[di]] = np.nan  # exclude kcb

            # sort
            idx_sort = np.argsort(-1 * avg_vol)
            activated = 0
            for ii in range(self.univsize):
                if np.isnan(avg_vol[idx_sort[ii]]):
                    continue
                self.valid[di, idx_sort[ii]] = True
                activated += 1
            add = np.sum(self.valid[di] & ~self.valid[di - 1])
            remove = np.sum(~self.valid[di] & self.valid[di - 1])
            print('[%s] Activated %d sotcks on day %d (+%d -%d)' % (self.tag, activated, uv.Dates[di], add, remove))

        return

