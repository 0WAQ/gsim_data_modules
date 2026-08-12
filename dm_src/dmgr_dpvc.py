from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Oputil
import numpy as np


class DmgrDpvc(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.days = None
        self.me = None
        self.dpvc1 = NIO_MATRIX()
        self.dpvc2 = NIO_MATRIX()
        self.dpvc3 = NIO_MATRIX()
        self.dpvc4 = NIO_MATRIX()
        self.dpvc5 = NIO_MATRIX()
        self.dpvc6 = NIO_MATRIX()
        self.dpvc7 = NIO_MATRIX()
        self.dpvc8 = NIO_MATRIX()
        self.dpvc9 = NIO_MATRIX()
        self.dpvc10 = NIO_MATRIX()
        self.dpvc11 = NIO_MATRIX()
        self.dpvc12 = NIO_MATRIX()
        self.dpvc13 = NIO_MATRIX()
        self.dpvc14 = NIO_MATRIX()
        self.dpvc15 = NIO_MATRIX()
        self.dpvc16 = NIO_MATRIX()
        self.dpvc17 = NIO_MATRIX()
        self.dpvc18 = NIO_MATRIX()
        self.dpvc19 = NIO_MATRIX()
        self.dpvc20 = NIO_MATRIX()

        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.days = cfg.getAttributeDefault('days', 250)
        self.addParamMetaData(self.days, 'days')
        self.me = cfg.getAttributeDefault('me', 5)
        self.addParamMetaData(self.me, 'me')
        self.addDailyData(self.dpvc1, self.tag+ ".dpvc1")
        self.addDailyData(self.dpvc2, self.tag+ ".dpvc2")
        self.addDailyData(self.dpvc3, self.tag+ ".dpvc3")
        self.addDailyData(self.dpvc4, self.tag+ ".dpvc4")
        self.addDailyData(self.dpvc5, self.tag+ ".dpvc5")
        self.addDailyData(self.dpvc6, self.tag+ ".dpvc6")
        self.addDailyData(self.dpvc7, self.tag+ ".dpvc7")
        self.addDailyData(self.dpvc8, self.tag+ ".dpvc8")
        self.addDailyData(self.dpvc9, self.tag+ ".dpvc9")
        self.addDailyData(self.dpvc10, self.tag+ ".dpvc10")
        self.addDailyData(self.dpvc11, self.tag+ ".dpvc11")
        self.addDailyData(self.dpvc12, self.tag+ ".dpvc12")
        self.addDailyData(self.dpvc13, self.tag+ ".dpvc13")
        self.addDailyData(self.dpvc14, self.tag+ ".dpvc14")
        self.addDailyData(self.dpvc15, self.tag+ ".dpvc15")
        self.addDailyData(self.dpvc16, self.tag+ ".dpvc16")
        self.addDailyData(self.dpvc17, self.tag+ ".dpvc17")
        self.addDailyData(self.dpvc18, self.tag+ ".dpvc18")
        self.addDailyData(self.dpvc19, self.tag+ ".dpvc19")
        self.addDailyData(self.dpvc20, self.tag+ ".dpvc20")



        return

    def dependencies(self, ):
        DataManagerMapped.dependencies(self, )
        dr.registerDependency(self.mid, 'ashareeodprices.s_dq_adjhigh')
        dr.registerDependency(self.mid, 'ashareeodprices.s_dq_adjlow')
        dr.registerDependency(self.mid, 'ashareeodprices.s_dq_adjopen')
        dr.registerDependency(self.mid, 'ashareeodprices.s_dq_adjclose')
        dr.registerDependency(self.mid, 'ashareeodprices.s_dq_adjpreclose')

        dr.registerDependency(self.mid, 'ashareeodprices.s_dq_avgprice')

        dr.registerDependency(self.mid, 'ashareeodprices.s_dq_high')
        dr.registerDependency(self.mid, 'ashareeodprices.s_dq_low')
        dr.registerDependency(self.mid, 'ashareeodprices.s_dq_close')
        dr.registerDependency(self.mid, 'ashareeodprices.s_dq_open')
        dr.registerDependency(self.mid, 'ashareeodprices.s_dq_preclose')

        dr.registerDependency(self.mid, 'ashareeodprices.s_dq_amount')
        dr.registerDependency(self.mid, 'ashareeodprices.s_dq_volume')
        dr.registerDependency(self.mid, 'ashareeodprices.s_dq_pctchange')
        dr.registerDependency(self.mid, 'AShareMoneyFlow.trades_count')




        return

    def loadData(self, di_start):
        self.fillnan(di_start, len(uv.Dates))  # set default value
        #ret = dr.getData('ashareeodprices.s_dq_pctchange')
        adjhigh = dr.getData('ashareeodprices.s_dq_adjhigh')
        adjlow = dr.getData('ashareeodprices.s_dq_adjlow')
        adjclose = dr.getData('ashareeodprices.s_dq_adjclose')
        adjopen = dr.getData('ashareeodprices.s_dq_adjopen')
        adjpreclose = dr.getData('ashareeodprices.s_dq_adjpreclose')

        vwap = dr.getData('ashareeodprices.s_dq_avgprice')

        high = dr.getData('ashareeodprices.s_dq_high')
        low = dr.getData('ashareeodprices.s_dq_low')
        close = dr.getData('ashareeodprices.s_dq_close')
        ops = dr.getData('ashareeodprices.s_dq_open')
        preclose = dr.getData('ashareeodprices.s_dq_preclose')

        ret = dr.getData('ashareeodprices.s_dq_pctchange')
        vol = dr.getData('ashareeodprices.s_dq_volume')
        amt = dr.getData('ashareeodprices.s_dq_amount')
        tcnt = dr.getData('AShareMoneyFlow.trades_count')



        for di in range(di_start, len(uv.Dates)):
            print('[%s] Updating on day %d' % (self.tag, uv.Dates[di]))
            if di < self.days:
                continue
            self.dpvc1[di] = np.max(amt[di-5:di+1],axis=0)
            #print (self.dpvc1[di])
            #print (self.dpvc1[di].shape)
            self.dpvc2[di] = np.max(amt[di-20:di+1],axis=0) 
            self.dpvc3[di] = np.max(amt[di-60:di+1],axis=0)
            #print (self.dpvc3[di])
            #print (self.dpvc3[di].shape)

            self.dpvc4[di] = np.max(amt[di-120:di+1],axis=0)
            self.dpvc5[di] = np.max(amt[di-242:di+1],axis=0)
            self.dpvc6[di] = np.argmax(amt[di-5:di+1],axis=0)
            self.dpvc7[di] = np.argmax(amt[di-20:di+1],axis=0)
            self.dpvc8[di] = np.argmax(amt[di-60:di+1],axis=0) 
            self.dpvc9[di] = np.argmax(amt[di-120:di+1],axis=0)
            self.dpvc10[di] = np.argmax(amt[di-242:di+1],axis=0)
            self.dpvc11[di] = np.min(amt[di-5:di+1],axis=0)
            self.dpvc12[di] = np.min(amt[di-20:di+1],axis=0) 
            self.dpvc13[di] = np.min(amt[di-60:di+1],axis=0)
            self.dpvc14[di] = np.min(amt[di-120:di+1],axis=0)
            self.dpvc15[di] = np.min(amt[di-240:di+1],axis=0)
            self.dpvc16[di] = np.argmin(amt[di-5:di+1],axis=0) 
            self.dpvc17[di] = np.argmin(amt[di-20:di+1],axis=0)
            self.dpvc18[di] = np.argmin(amt[di-60:di+1],axis=0)
            self.dpvc19[di] = np.argmin(amt[di-120:di+1],axis=0)
            self.dpvc20[di] = np.argmin(amt[di-242:di+1],axis=0)

            #print ("dpvc1:",self.dpvc1[di])
            #print ("dpvc2:",self.dpvc2[di])
            #print ("dpvc3:",self.dpvc3[di])
        return

