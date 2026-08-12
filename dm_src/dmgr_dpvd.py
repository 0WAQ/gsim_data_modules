from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Oputil
import numpy as np


class DmgrDpvd(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.days = None
        self.me = None
        self.dpvd1 = NIO_MATRIX()
        self.dpvd2 = NIO_MATRIX()
        self.dpvd3 = NIO_MATRIX()
        self.dpvd4 = NIO_MATRIX()
        self.dpvd5 = NIO_MATRIX()
        self.dpvd6 = NIO_MATRIX()
        self.dpvd7 = NIO_MATRIX()
        self.dpvd8 = NIO_MATRIX()
        self.dpvd9 = NIO_MATRIX()
        self.dpvd10 = NIO_MATRIX()
        self.dpvd11 = NIO_MATRIX()
        self.dpvd12 = NIO_MATRIX()
        self.dpvd13 = NIO_MATRIX()
        self.dpvd14 = NIO_MATRIX()
        self.dpvd15 = NIO_MATRIX()
        self.dpvd16 = NIO_MATRIX()
        self.dpvd17 = NIO_MATRIX()
        self.dpvd18 = NIO_MATRIX()
        self.dpvd19 = NIO_MATRIX()
        self.dpvd20 = NIO_MATRIX()

        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.days = cfg.getAttributeDefault('days', 20)
        self.addParamMetaData(self.days, 'days')
        self.me = cfg.getAttributeDefault('me', 5)
        self.addParamMetaData(self.me, 'me')
        self.addDailyData(self.dpvd1, self.tag+ ".dpvd1")
        self.addDailyData(self.dpvd2, self.tag+ ".dpvd2")
        self.addDailyData(self.dpvd3, self.tag+ ".dpvd3")
        self.addDailyData(self.dpvd4, self.tag+ ".dpvd4")
        self.addDailyData(self.dpvd5, self.tag+ ".dpvd5")
        self.addDailyData(self.dpvd6, self.tag+ ".dpvd6")
        self.addDailyData(self.dpvd7, self.tag+ ".dpvd7")
        self.addDailyData(self.dpvd8, self.tag+ ".dpvd8")
        self.addDailyData(self.dpvd9, self.tag+ ".dpvd9")
        self.addDailyData(self.dpvd10, self.tag+ ".dpvd10")
        self.addDailyData(self.dpvd11, self.tag+ ".dpvd11")
        self.addDailyData(self.dpvd12, self.tag+ ".dpvd12")
        self.addDailyData(self.dpvd13, self.tag+ ".dpvd13")
        self.addDailyData(self.dpvd14, self.tag+ ".dpvd14")
        self.addDailyData(self.dpvd15, self.tag+ ".dpvd15")
        self.addDailyData(self.dpvd16, self.tag+ ".dpvd16")
        self.addDailyData(self.dpvd17, self.tag+ ".dpvd17")
        self.addDailyData(self.dpvd18, self.tag+ ".dpvd18")
        self.addDailyData(self.dpvd19, self.tag+ ".dpvd19")
        self.addDailyData(self.dpvd20, self.tag+ ".dpvd20")



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
        dr.registerDependency(self.mid, 'ashareeodprices.s_dq_pctchange')




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

        ret1000 = dr.getData('aindexeodprices.s_dq_pctchange_000852')
        ret500 = dr.getData('aindexeodprices.s_dq_pctchange_000905')
        ret300 = dr.getData('aindexeodprices.s_dq_pctchange_000300')


        close1000 = dr.getData('aindexeodprices.s_dq_close_000852')
        close500 = dr.getData('aindexeodprices.s_dq_close_000905')
        close300 = dr.getData('aindexeodprices.s_dq_close_000300')


        open500 = dr.getData('aindexeodprices.s_dq_open_000905')
        preclose500 = dr.getData('aindexeodprices.s_dq_preclose_000905')


        amt1000 = dr.getData('aindexeodprices.s_dq_amount_000852')
        amt500 = dr.getData('aindexeodprices.s_dq_amount_000905')
        amt300 = dr.getData('aindexeodprices.s_dq_amount_000300')

        for di in range(di_start, len(uv.Dates)):
            print('[%s] Updating on day %d' % (self.tag, uv.Dates[di]))
            if di < self.days:
                continue
            self.dpvd1[di] = ret[di]-ret[di-1]
            self.dpvd2[di] = ret[di]-ret1000[di] 
            self.dpvd3[di] =  ret[di]-ret500[di]
            self.dpvd4[di] = ret[di]-ret300[di]
            self.dpvd5[di] = ret300[di]-ret500[di]
            self.dpvd6[di] = Oputil.mean(ret[di-20:di+1]-ret1000[di-20:di+1].reshape(-1,1)) 
            self.dpvd7[di] = Oputil.mean(ret[di-20:di+1]-ret300[di-20:di+1].reshape(-1,1))
            self.dpvd8[di] = Oputil.std(ret[di-20:di+1]-ret1000[di-20:di+1].reshape(-1,1)) 
            self.dpvd9[di] = Oputil.std(ret[di-20:di+1]-ret300[di-20:di+1].reshape(-1,1))
            self.dpvd10[di] = ret500[di]*2-ret300[di]-ret1000[di]
            self.dpvd11[di] = amt[di] / amt1000[di] 
            self.dpvd12[di] = amt[di] / amt500[di] 
            self.dpvd13[di] = amt[di] / amt300[di]
            self.dpvd14[di] = amt1000[di] / amt300[di]
            self.dpvd15[di] = adjclose[di]/ close1000[di]
            self.dpvd16[di] = close300[di]/close1000[di]
            self.dpvd17[di] = adjclose[di]/close300[di] 
            self.dpvd18[di] = adjopen[di]/adjpreclose[di] - open500[di].reshape(-1,1)/preclose500[di].reshape(-1,1) 
            self.dpvd19[di] = adjclose[di]/adjopen[di] - close500[di].reshape(-1,1)/open500[di].reshape(-1,1)
            self.dpvd20[di] = ret500[di]

            #print ("dpvd1:",self.dpvd1[di])
            #print ("dpvd2:",self.dpvd2[di])
            #print ("dpvd3:",self.dpvd3[di])
        return

