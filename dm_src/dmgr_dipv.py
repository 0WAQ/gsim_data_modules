from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Oputil
import numpy as np


class DmgrDipv(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.days = None
        self.me = None
        self.dipv1 = NIO_MATRIX()
        self.dipv2 = NIO_MATRIX()
        self.dipv3 = NIO_MATRIX()
        self.dipv4 = NIO_MATRIX()
        self.dipv5 = NIO_MATRIX()
        self.dipv6 = NIO_MATRIX()
        self.dipv7 = NIO_MATRIX()
        self.dipv8 = NIO_MATRIX()
        self.dipv9 = NIO_MATRIX()
        self.dipv10 = NIO_MATRIX()
        self.dipv11 = NIO_MATRIX()
        self.dipv12 = NIO_MATRIX()
        self.dipv13 = NIO_MATRIX()
        self.dipv14 = NIO_MATRIX()
        self.dipv15 = NIO_MATRIX()
        self.dipv16 = NIO_MATRIX()
        self.dipv17 = NIO_MATRIX()
        self.dipv18 = NIO_MATRIX()
        self.dipv19 = NIO_MATRIX()
        self.dipv20 = NIO_MATRIX()

        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.days = cfg.getAttributeDefault('days', 10)
        self.addParamMetaData(self.days, 'days')
        self.me = cfg.getAttributeDefault('me', 5)
        self.addParamMetaData(self.me, 'me')
        self.addDailyData(self.dipv1, self.tag+ ".dipv1")
        self.addDailyData(self.dipv2, self.tag+ ".dipv2")
        self.addDailyData(self.dipv3, self.tag+ ".dipv3")
        self.addDailyData(self.dipv4, self.tag+ ".dipv4")
        self.addDailyData(self.dipv5, self.tag+ ".dipv5")
        self.addDailyData(self.dipv6, self.tag+ ".dipv6")
        self.addDailyData(self.dipv7, self.tag+ ".dipv7")
        self.addDailyData(self.dipv8, self.tag+ ".dipv8")
        self.addDailyData(self.dipv9, self.tag+ ".dipv9")
        self.addDailyData(self.dipv10, self.tag+ ".dipv10")
        self.addDailyData(self.dipv11, self.tag+ ".dipv11")
        self.addDailyData(self.dipv12, self.tag+ ".dipv12")
        self.addDailyData(self.dipv13, self.tag+ ".dipv13")
        self.addDailyData(self.dipv14, self.tag+ ".dipv14")
        self.addDailyData(self.dipv15, self.tag+ ".dipv15")
        self.addDailyData(self.dipv16, self.tag+ ".dipv16")
        self.addDailyData(self.dipv17, self.tag+ ".dipv17")
        self.addDailyData(self.dipv18, self.tag+ ".dipv18")
        self.addDailyData(self.dipv19, self.tag+ ".dipv19")
        self.addDailyData(self.dipv20, self.tag+ ".dipv20")



        return

#Interval5m.amo.npy
#Interval5m.close.npy
#Interval5m.high.npy
#Interval5m.low.npy
#Interval5m.open.npy
#Interval5m.vol.npy




    def dependencies(self, ):
        DataManagerMapped.dependencies(self, )

        dr.registerDependency(self.mid, 'Interval5m.high')
        dr.registerDependency(self.mid, 'Interval5m.low')
        dr.registerDependency(self.mid, 'Interval5m.open')
        dr.registerDependency(self.mid, 'Interval5m.close')
        dr.registerDependency(self.mid, 'Interval5m.vol')
        dr.registerDependency(self.mid, 'Interval5m.amo')



        #dr.registerDependency(self.mid, 'ashareeodprices.s_dq_adjhigh')
        #dr.registerDependency(self.mid, 'ashareeodprices.s_dq_adjlow')
        #dr.registerDependency(self.mid, 'ashareeodprices.s_dq_adjopen')
        #dr.registerDependency(self.mid, 'ashareeodprices.s_dq_adjclose')
        #dr.registerDependency(self.mid, 'ashareeodprices.s_dq_adjpreclose')

        #dr.registerDependency(self.mid, 'ashareeodprices.s_dq_avgprice')

        #dr.registerDependency(self.mid, 'ashareeodprices.s_dq_high')
        #dr.registerDependency(self.mid, 'ashareeodprices.s_dq_low')
        #dr.registerDependency(self.mid, 'ashareeodprices.s_dq_close')
        #dr.registerDependency(self.mid, 'ashareeodprices.s_dq_open')
        #dr.registerDependency(self.mid, 'ashareeodprices.s_dq_preclose')

        #dr.registerDependency(self.mid, 'ashareeodprices.s_dq_amount')
        dr.registerDependency(self.mid, 'ashareeodprices.s_dq_volume')
        #dr.registerDependency(self.mid, 'ashareeodprices.s_dq_pctchange')
        #dr.registerDependency(self.mid, 'AShareMoneyFlow.trades_count')




        return

    def loadData(self, di_start):
        self.fillnan(di_start, len(uv.Dates))  # set default value
        #ret = dr.getData('ashareeodprices.s_dq_pctchange')
        #adjhigh = dr.getData('ashareeodprices.s_dq_adjhigh')
        #adjlow = dr.getData('ashareeodprices.s_dq_adjlow')
        #adjclose = dr.getData('ashareeodprices.s_dq_adjclose')
        #adjopen = dr.getData('ashareeodprices.s_dq_adjopen')
        #adjpreclose == dr.getData('ashareeodprices.s_dq_adjpreclose')

        #vwap = dr.getData('ashareeodprices.s_dq_avgprice')

        #high = dr.getData('ashareeodprices.s_dq_high')
        #low = dr.getData('ashareeodprices.s_dq_low')
        #close = dr.getData('ashareeodprices.s_dq_close')
        #ops = dr.getData('ashareeodprices.s_dq_open')
        #preclose = dr.getData('ashareeodprices.s_dq_preclose')

 
        high_m5 = dr.getData('Interval5m.high')
        low_m5 = dr.getData('Interval5m.low')
        ops_m5 = dr.getData('Interval5m.open')
        close_m5 = dr.getData('Interval5m.close')
        vol_m5 = dr.getData('Interval5m.vol')
        amo_m5 = dr.getData('Interval5m.amo')


        #ret = dr.getData('ashareeodprices.s_dq_pctchange')
        vol = dr.getData('ashareeodprices.s_dq_volume')
        #amt = dr.getData('ashareeodprices.s_dq_amount')
        #tcnt = dr.getData('AShareMoneyFlow.trades_count')



        for di in range(di_start, len(uv.Dates)):
            print('[%s] Updating on day %d' % (self.tag, uv.Dates[di]))
            if di < self.days:
                continue
            self.dipv1[di] = close_m5[di,1] / ops_m5[di,1] -1.0
            self.dipv2[di] = close_m5[di,48] / ops_m5[di,48] -1.0
            self.dipv3[di] = close_m5[di,24] / ops_m5[di,24] -1.0
            self.dipv4[di] = close_m5[di,25] / ops_m5[di,25] -1.0
            self.dipv5[di] = close_m5[di,12] / ops_m5[di,1] -1.0
            self.dipv6[di] = close_m5[di,24] / close_m5[di,12] -1.0
            self.dipv7[di] = close_m5[di,36] / close_m5[di,24] -1.0
            self.dipv8[di] = close_m5[di,48] / close_m5[di,36] -1.0
            self.dipv9[di] = close_m5[di,24] / ops_m5[di,1] -1.0 
            self.dipv10[di] = close_m5[di,48] / close_m5[di,24] -1.0
            self.dipv11[di] = vol_m5[di,48]/(vol[di]+0.00001) 
            self.dipv12[di] = vol_m5[di,1]/(vol[di]+0.00001) 
            self.dipv13[di] = vol_m5[di,24]/(vol[di]+0.00001) 
            self.dipv14[di] = vol_m5[di,25]/(vol[di]+0.00001)
            self.dipv15[di] = amo_m5[di,48]/vol_m5[di,48]/100.0/close_m5[di,48]-1.0  
            self.dipv16[di] = amo_m5[di,1]/vol_m5[di,1]/100.0/close_m5[di,1]-1.0 
            self.dipv17[di] = amo_m5[di,48]/vol_m5[di,48]/100.0/(ops_m5[di,48]+close_m5[di,48])-1.0 
            self.dipv18[di] = amo_m5[di,1]/vol_m5[di,1]/100.0/(ops_m5[di,1]+close_m5[di,1])-1.0
            self.dipv19[di] = high_m5[di,1] / low_m5[di,1] -1.0 
            self.dipv20[di] = high_m5[di,48] / low_m5[di,48] -1.0  

            #print ("dipv1:",self.dipv1[di])
            #print ("dipv2:",self.dipv2[di])
            #print ("dipv3:",self.dipv3[di])
        return

