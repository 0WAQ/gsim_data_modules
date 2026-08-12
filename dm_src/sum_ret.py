from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Oputil
import numpy as np


class DmgrSumret(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.days = None
        self.me = None
        self.sumret = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.days = cfg.getAttributeDefault('days', 10)
        self.addParamMetaData(self.days, 'days')
        self.me = cfg.getAttributeDefault('me', 5)
        self.addParamMetaData(self.me, 'me')
        self.addDailyData(self.sumret, self.tag)
        return

    def dependencies(self, ):
        DataManagerMapped.dependencies(self, )
        dr.registerDependency(self.mid, 'ashareeodprices.s_dq_pctchange')
        return

    def loadData(self, di_start):
        self.fillnan(di_start, len(uv.Dates))  # set default value
        ret = dr.getData('ashareeodprices.s_dq_pctchange')
        for di in range(di_start, len(uv.Dates)):
            print('[%s] Updating on day %d' % (self.tag, uv.Dates[di]))
            if di < self.days:
                continue
            self.sumret[di] = Oputil.sum(ret[di - self.days + 1:di + 1], self.me)
            print ("ret_di:",ret[di])
            print (di, self.sumret[di])
        return

