from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Oputil
import numpy as np
import os

class DmgrAdv(DataManagerMapped):
    def __init__(self,):
        DataManagerMapped.__init__(self, )
        self.ndays = None
        self.adv   = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.ndays = cfg.getAttribute('ndays')
        self.addParamMetaData(self.ndays, 'ndays')
        self.addDailyData(self.adv, self.tag)
        return

    def dependencies(self,):
        dr.registerDependency(self.mid, 'amount')
        return
    
    def loadData(self, di_start):
        self.fillnan(di_start, len(uv.Dates)) # set default value
        amt = dr.getData('amount')
        for di in range(di_start, len(uv.Dates)):
            print('[%s] Updating on day %d' % (self.tag, uv.Dates[di]))
            di_work = max(di - self.ndays+1, 0) 
            bm = amt[di_work:di+1] > 0
            a = np.copy(amt[di_work:di+1])
            a[ ~bm ] = np.nan
            self.adv[di] = Oputil.mean(a)
        return
