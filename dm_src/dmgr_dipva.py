from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Oputil
import numpy as np

def fast_skew(data, me=3, axis=None):
    n = data.shape[axis] if axis is not None else len(data)
    mean = np.mean(data, axis=axis, keepdims=True)
    std_dev = np.std(data, axis=axis, ddof=0, keepdims=True)  # 使用 ddof=0 以匹配 scipy.stats.skew 的行为
    skewness = (n / ((n - 1) * (n - 2))) * np.sum((((data - mean) / std_dev) ** 3), axis=axis)
    return skewness


class DmgrDipva(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.days = None
        self.me = None
        self.dipva1 = NIO_MATRIX()
        self.dipva2 = NIO_MATRIX()
        self.dipva3 = NIO_MATRIX()
        self.dipva4 = NIO_MATRIX()
        self.dipva5 = NIO_MATRIX()
        self.dipva6 = NIO_MATRIX()
        self.dipva7 = NIO_MATRIX()
        self.dipva8 = NIO_MATRIX()
        self.dipva9 = NIO_MATRIX()
        self.dipva10 = NIO_MATRIX()
        self.dipva11 = NIO_MATRIX()
        self.dipva12 = NIO_MATRIX()
        self.dipva13 = NIO_MATRIX()
        self.dipva14 = NIO_MATRIX()
        self.dipva15 = NIO_MATRIX()
        self.dipva16 = NIO_MATRIX()
        self.dipva17 = NIO_MATRIX()
        self.dipva18 = NIO_MATRIX()
        self.dipva19 = NIO_MATRIX()
        self.dipva20 = NIO_MATRIX()

        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.days = cfg.getAttributeDefault('days', 10)
        self.addParamMetaData(self.days, 'days')
        self.me = cfg.getAttributeDefault('me', 5)
        self.addParamMetaData(self.me, 'me')
        self.addDailyData(self.dipva1, self.tag+ ".dipva1")
        self.addDailyData(self.dipva2, self.tag+ ".dipva2")
        self.addDailyData(self.dipva3, self.tag+ ".dipva3")
        self.addDailyData(self.dipva4, self.tag+ ".dipva4")
        self.addDailyData(self.dipva5, self.tag+ ".dipva5")
        self.addDailyData(self.dipva6, self.tag+ ".dipva6")
        self.addDailyData(self.dipva7, self.tag+ ".dipva7")
        self.addDailyData(self.dipva8, self.tag+ ".dipva8")
        self.addDailyData(self.dipva9, self.tag+ ".dipva9")
        self.addDailyData(self.dipva10, self.tag+ ".dipva10")
        self.addDailyData(self.dipva11, self.tag+ ".dipva11")
        self.addDailyData(self.dipva12, self.tag+ ".dipva12")
        self.addDailyData(self.dipva13, self.tag+ ".dipva13")
        self.addDailyData(self.dipva14, self.tag+ ".dipva14")
        self.addDailyData(self.dipva15, self.tag+ ".dipva15")
        self.addDailyData(self.dipva16, self.tag+ ".dipva16")
        self.addDailyData(self.dipva17, self.tag+ ".dipva17")
        self.addDailyData(self.dipva18, self.tag+ ".dipva18")
        self.addDailyData(self.dipva19, self.tag+ ".dipva19")
        self.addDailyData(self.dipva20, self.tag+ ".dipva20")



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
        #dr.registerDependency(self.mid, 'ashareeodprices.s_dq_volume')
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
            self.dipva1[di] = Oputil.mean(close_m5[di,1:] / ops_m5[di,1:]-1.0)
            #print ("self.dipva1[di]:",self.dipva1[di],"shape:",self.dipva1[di].shape)
            self.dipva2[di] = Oputil.std(close_m5[di,1:] / ops_m5[di,1:] -1.0)
            self.dipva3[di] = fast_skew(close_m5[di,1:] / ops_m5[di,1:] -1.0)
            self.dipva4[di] =  Oputil.std(close_m5[di,1:])/ Oputil.mean(close_m5[di,1:]) 
            self.dipva5[di] = Oputil.corr(close_m5[di,1:],vol_m5[di,1:])
            #print (self.dipva5[di].shape)
            self.dipva6[di] = Oputil.corr(close_m5[di,1:],high_m5[di,1:]-low_m5[di,1:]) 
            self.dipva7[di] = Oputil.corr(vol_m5[di,1:],high_m5[di,1:]-low_m5[di,1:]) 
            self.dipva8[di] = Oputil.corr(close_m5[di,1:48],vol_m5[di,2:49]) 
            self.dipva9[di] = Oputil.corr(close_m5[di,2:49],vol_m5[di,1:48])
            self.dipva10[di] = Oputil.corr(vol_m5[di,1:48],high_m5[di,2:49]-low_m5[di,2:49]) 
            self.dipva11[di] = Oputil.corr(vol_m5[di,2:49],high_m5[di,1:48]-low_m5[di,1:48])
            self.dipva12[di] = Oputil.corr(vol_m5[di,2:49]-vol_m5[di,1:48],high_m5[di,1:48]-low_m5[di,1:48]) 
            self.dipva13[di] = Oputil.corr(vol_m5[di,2:49]-vol_m5[di,1:48],high_m5[di,2:49]-low_m5[di,2:49]) 
            self.dipva14[di] = Oputil.corr(vol_m5[di,2:49]-vol_m5[di,1:48],close_m5[di,2:49]-ops_m5[di,2:49]) 
            self.dipva15[di] =  Oputil.corr(vol_m5[di,2:49]-vol_m5[di,1:48],close_m5[di,1:48]-ops_m5[di,1:48]) 
            self.dipva16[di] = Oputil.corr(amo_m5[di,1:49]/(vol_m5[di,1:49]+0.00001)/100.0,close_m5[di,1:49] ) 
            self.dipva17[di] =  Oputil.corr(close_m5[di,2:49],close_m5[di,2:49]-close_m5[di,1:48]) 
            self.dipva18[di] = Oputil.corr(vol_m5[di,2:49],close_m5[di,2:49]-close_m5[di,1:48])
            self.dipva19[di] = Oputil.corr(vol_m5[di,1:48],close_m5[di,2:49]-close_m5[di,1:48])
            self.dipva20[di] = Oputil.corr(vol_m5[di,2:49]-vol_m5[di,1:48],close_m5[di,2:49]-close_m5[di,1:48])

            #print ("dipv1:",self.dipv1[di])
            #print ("dipv2:",self.dipv2[di])
            #print ("dipv3:",self.dipv3[di])
        return

