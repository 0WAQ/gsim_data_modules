from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Oputil
import numpy as np


class DmgrDpva(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.days = None
        self.me = None
        self.dpva1 = NIO_MATRIX()
        self.dpva2 = NIO_MATRIX()
        self.dpva3 = NIO_MATRIX()
        self.dpva4 = NIO_MATRIX()
        self.dpva5 = NIO_MATRIX()
        self.dpva6 = NIO_MATRIX()
        self.dpva7 = NIO_MATRIX()
        self.dpva8 = NIO_MATRIX()
        self.dpva9 = NIO_MATRIX()
        self.dpva10 = NIO_MATRIX()
        self.dpva11 = NIO_MATRIX()
        self.dpva12 = NIO_MATRIX()
        self.dpva13 = NIO_MATRIX()
        self.dpva14 = NIO_MATRIX()
        self.dpva15 = NIO_MATRIX()
        self.dpva16 = NIO_MATRIX()
        self.dpva17 = NIO_MATRIX()
        self.dpva18 = NIO_MATRIX()
        self.dpva19 = NIO_MATRIX()
        self.dpva20 = NIO_MATRIX()

        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.days = cfg.getAttributeDefault('days', 20)
        self.addParamMetaData(self.days, 'days')
        self.me = cfg.getAttributeDefault('me', 5)
        self.addParamMetaData(self.me, 'me')
        self.addDailyData(self.dpva1, self.tag+ ".dpva1")
        self.addDailyData(self.dpva2, self.tag+ ".dpva2")
        self.addDailyData(self.dpva3, self.tag+ ".dpva3")
        self.addDailyData(self.dpva4, self.tag+ ".dpva4")
        self.addDailyData(self.dpva5, self.tag+ ".dpva5")
        self.addDailyData(self.dpva6, self.tag+ ".dpva6")
        self.addDailyData(self.dpva7, self.tag+ ".dpva7")
        self.addDailyData(self.dpva8, self.tag+ ".dpva8")
        self.addDailyData(self.dpva9, self.tag+ ".dpva9")
        self.addDailyData(self.dpva10, self.tag+ ".dpva10")
        self.addDailyData(self.dpva11, self.tag+ ".dpva11")
        self.addDailyData(self.dpva12, self.tag+ ".dpva12")
        self.addDailyData(self.dpva13, self.tag+ ".dpva13")
        self.addDailyData(self.dpva14, self.tag+ ".dpva14")
        self.addDailyData(self.dpva15, self.tag+ ".dpva15")
        self.addDailyData(self.dpva16, self.tag+ ".dpva16")
        self.addDailyData(self.dpva17, self.tag+ ".dpva17")
        self.addDailyData(self.dpva18, self.tag+ ".dpva18")
        self.addDailyData(self.dpva19, self.tag+ ".dpva19")
        self.addDailyData(self.dpva20, self.tag+ ".dpva20")



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
            self.dpva1[di] = Oputil.mean(ret[di-4:di+1])
            #print ("self.dpva1[di]:",self.dpva1[di])
            #print (self.dpva1[di].shape)
            self.dpva2[di] = Oputil.mean(ret[di-20:di+1]) 
            self.dpva3[di] = Oputil.mean(ret[di-40:di+1]) 
            self.dpva4[di] = Oputil.mean(ret[di-60:di+1])
            self.dpva5[di] = Oputil.mean(ret[di-120:di+1])
            self.dpva6[di] = Oputil.mean(ret[di-242:di+1])
            self.dpva7[di] = Oputil.mean(ret[di-242:di-20])
            self.dpva8[di] = Oputil.mean(ret[di-242:di-60])
            self.dpva9[di] = Oputil.mean(ret[di-242:di-120])
            self.dpva10[di] = Oputil.mean(ret[di-242:di-180])
            self.dpva11[di] = Oputil.mean(ret[di-242:di-220])
            self.dpva12[di] = Oputil.mean(ret[di-262:di-242]) 
            self.dpva13[di] = Oputil.mean(ret[di-485:di+1])
            self.dpva14[di] = Oputil.mean(ret[di-485:di-242])
            self.dpva15[di] = Oputil.mean(ret[di-485:di-21])
            self.dpva16[di] = Oputil.mean(ret[di-180:di+1])
            self.dpva17[di] = Oputil.mean(ret[di-3:di+1])
            self.dpva18[di] = Oputil.mean(ret[di-2:di+1])
            self.dpva19[di] = Oputil.mean(ret[di-1:di+1])
            self.dpva20[di] = Oputil.mean(ret[di-10:di+1]) 

            #print ("dpva1:",self.dpva1[di])
            #print ("dpva2:",self.dpva2[di])
            #print ("dpva3:",self.dpva3[di])
        return

