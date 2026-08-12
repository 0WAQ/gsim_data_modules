from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Oputil
import numpy as np


class DmgrDpvb(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.days = None
        self.me = None
        self.dpvb1 = NIO_MATRIX()
        self.dpvb2 = NIO_MATRIX()
        self.dpvb3 = NIO_MATRIX()
        self.dpvb4 = NIO_MATRIX()
        self.dpvb5 = NIO_MATRIX()
        self.dpvb6 = NIO_MATRIX()
        self.dpvb7 = NIO_MATRIX()
        self.dpvb8 = NIO_MATRIX()
        self.dpvb9 = NIO_MATRIX()
        self.dpvb10 = NIO_MATRIX()
        self.dpvb11 = NIO_MATRIX()
        self.dpvb12 = NIO_MATRIX()
        self.dpvb13 = NIO_MATRIX()
        self.dpvb14 = NIO_MATRIX()
        self.dpvb15 = NIO_MATRIX()
        self.dpvb16 = NIO_MATRIX()
        self.dpvb17 = NIO_MATRIX()
        self.dpvb18 = NIO_MATRIX()
        self.dpvb19 = NIO_MATRIX()
        self.dpvb20 = NIO_MATRIX()

        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.days = cfg.getAttributeDefault('days', 20)
        self.addParamMetaData(self.days, 'days')
        self.me = cfg.getAttributeDefault('me', 5)
        self.addParamMetaData(self.me, 'me')
        self.addDailyData(self.dpvb1, self.tag+ ".dpvb1")
        self.addDailyData(self.dpvb2, self.tag+ ".dpvb2")
        self.addDailyData(self.dpvb3, self.tag+ ".dpvb3")
        self.addDailyData(self.dpvb4, self.tag+ ".dpvb4")
        self.addDailyData(self.dpvb5, self.tag+ ".dpvb5")
        self.addDailyData(self.dpvb6, self.tag+ ".dpvb6")
        self.addDailyData(self.dpvb7, self.tag+ ".dpvb7")
        self.addDailyData(self.dpvb8, self.tag+ ".dpvb8")
        self.addDailyData(self.dpvb9, self.tag+ ".dpvb9")
        self.addDailyData(self.dpvb10, self.tag+ ".dpvb10")
        self.addDailyData(self.dpvb11, self.tag+ ".dpvb11")
        self.addDailyData(self.dpvb12, self.tag+ ".dpvb12")
        self.addDailyData(self.dpvb13, self.tag+ ".dpvb13")
        self.addDailyData(self.dpvb14, self.tag+ ".dpvb14")
        self.addDailyData(self.dpvb15, self.tag+ ".dpvb15")
        self.addDailyData(self.dpvb16, self.tag+ ".dpvb16")
        self.addDailyData(self.dpvb17, self.tag+ ".dpvb17")
        self.addDailyData(self.dpvb18, self.tag+ ".dpvb18")
        self.addDailyData(self.dpvb19, self.tag+ ".dpvb19")
        self.addDailyData(self.dpvb20, self.tag+ ".dpvb20")



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
            self.dpvb1[di] = Oputil.mean(amt[di-4:di+1])
            #print ("self.dpvb1[di]:",self.dpvb1[di])
            #print (self.dpvb1[di].shape)
            self.dpvb2[di] = Oputil.mean(amt[di-20:di+1]) 
            self.dpvb3[di] = Oputil.mean(amt[di-40:di+1]) 
            self.dpvb4[di] = Oputil.mean(amt[di-60:di+1])
            self.dpvb5[di] = Oputil.mean(amt[di-120:di+1])
            self.dpvb6[di] = Oputil.mean(amt[di-242:di+1])
            self.dpvb7[di] = Oputil.mean(amt[di-242:di-20])
            self.dpvb8[di] = Oputil.mean(amt[di-242:di-60])
            self.dpvb9[di] = Oputil.mean(amt[di-242:di-120])
            self.dpvb10[di] = Oputil.mean(amt[di-242:di-180])
            self.dpvb11[di] = Oputil.mean(amt[di-242:di-220])
            self.dpvb12[di] = Oputil.mean(amt[di-262:di-242]) 
            self.dpvb13[di] = Oputil.mean(amt[di-485:di+1])
            self.dpvb14[di] = Oputil.mean(amt[di-485:di-242])
            self.dpvb15[di] = Oputil.mean(amt[di-485:di-21])
            self.dpvb16[di] = Oputil.mean(amt[di-180:di+1])
            self.dpvb17[di] = Oputil.mean(amt[di-3:di+1])
            self.dpvb18[di] = Oputil.mean(amt[di-2:di+1])
            self.dpvb19[di] = Oputil.mean(amt[di-1:di+1])
            self.dpvb20[di] = Oputil.mean(amt[di-10:di+1]) 

            #print ("dpvb1:",self.dpvb1[di])
            #print ("dpvb2:",self.dpvb2[di])
            #print ("dpvb3:",self.dpvb3[di])
        return

