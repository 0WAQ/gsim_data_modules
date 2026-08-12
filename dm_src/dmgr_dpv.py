from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Oputil
import numpy as np


class DmgrDpv(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.days = None
        self.me = None
        self.dpv1 = NIO_MATRIX()
        self.dpv2 = NIO_MATRIX()
        self.dpv3 = NIO_MATRIX()
        self.dpv4 = NIO_MATRIX()
        self.dpv5 = NIO_MATRIX()
        self.dpv6 = NIO_MATRIX()
        self.dpv7 = NIO_MATRIX()
        self.dpv8 = NIO_MATRIX()
        self.dpv9 = NIO_MATRIX()
        self.dpv10 = NIO_MATRIX()
        self.dpv11 = NIO_MATRIX()
        self.dpv12 = NIO_MATRIX()
        self.dpv13 = NIO_MATRIX()
        self.dpv14 = NIO_MATRIX()
        self.dpv15 = NIO_MATRIX()
        self.dpv16 = NIO_MATRIX()
        self.dpv17 = NIO_MATRIX()
        self.dpv18 = NIO_MATRIX()
        self.dpv19 = NIO_MATRIX()
        self.dpv20 = NIO_MATRIX()

        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.days = cfg.getAttributeDefault('days', 10)
        self.addParamMetaData(self.days, 'days')
        self.me = cfg.getAttributeDefault('me', 5)
        self.addParamMetaData(self.me, 'me')
        self.addDailyData(self.dpv1, self.tag+ ".dpv1")
        self.addDailyData(self.dpv2, self.tag+ ".dpv2")
        self.addDailyData(self.dpv3, self.tag+ ".dpv3")
        self.addDailyData(self.dpv4, self.tag+ ".dpv4")
        self.addDailyData(self.dpv5, self.tag+ ".dpv5")
        self.addDailyData(self.dpv6, self.tag+ ".dpv6")
        self.addDailyData(self.dpv7, self.tag+ ".dpv7")
        self.addDailyData(self.dpv8, self.tag+ ".dpv8")
        self.addDailyData(self.dpv9, self.tag+ ".dpv9")
        self.addDailyData(self.dpv10, self.tag+ ".dpv10")
        self.addDailyData(self.dpv11, self.tag+ ".dpv11")
        self.addDailyData(self.dpv12, self.tag+ ".dpv12")
        self.addDailyData(self.dpv13, self.tag+ ".dpv13")
        self.addDailyData(self.dpv14, self.tag+ ".dpv14")
        self.addDailyData(self.dpv15, self.tag+ ".dpv15")
        self.addDailyData(self.dpv16, self.tag+ ".dpv16")
        self.addDailyData(self.dpv17, self.tag+ ".dpv17")
        self.addDailyData(self.dpv18, self.tag+ ".dpv18")
        self.addDailyData(self.dpv19, self.tag+ ".dpv19")
        self.addDailyData(self.dpv20, self.tag+ ".dpv20")



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
            self.dpv1[di] = adjclose[di] - adjopen[di] 
            self.dpv2[di] = adjhigh[di] - adjlow[di] 
            self.dpv3[di] = adjopen[di] - adjpreclose[di]
            self.dpv4[di] = adjlow[di] - adjpreclose[di]
            self.dpv5[di] = adjclose[di] - adjlow[di]
            self.dpv6[di] = adjhigh[di] - adjclose[di]
            self.dpv7[di] = adjclose[di] - adjpreclose[di]
            self.dpv8[di] = (adjhigh[di] + adjlow[di])/2-adjclose[di]
            self.dpv9[di] = (adjhigh[di] + adjlow[di])/2-adjopen[di]
            self.dpv10[di] = (adjhigh[di] + adjlow[di])/2-adjpreclose[di]
            self.dpv11[di] = abs(adjopen[di] - adjpreclose[di])
            self.dpv12[di] = (vwap[di] / close[di] -1.0)
            self.dpv13[di] = abs(vwap[di] / close[di] -1.0)
            self.dpv14[di] = (2*vwap[di] / (close[di]+ops[di]) -1.0)
            self.dpv15[di] = abs(2*vwap[di] / (close[di]+ops[di]) -1.0)
            self.dpv16[di] = (tcnt[di] / vol[di] -1.0)
            self.dpv17[di] = (tcnt[di] / amt[di] -1.0)
            self.dpv18[di] = (2*vwap[di] /(high[di]+low[di]) -1.0)
            self.dpv19[di] = abs(2*vwap[di] /(high[di]+low[di]) -1.0)
            self.dpv20[di] = (adjhigh[di] - adjlow[di])/adjclose[di]  

            #print ("dpv1:",self.dpv1[di])
            #print ("dpv2:",self.dpv2[di])
            #print ("dpv3:",self.dpv3[di])
        return

