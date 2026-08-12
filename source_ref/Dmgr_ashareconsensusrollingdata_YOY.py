
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrashareconsensusrollingdata_YOY(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.net_profit = NIO_MATRIX()
        self.est_eps = NIO_MATRIX()
        self.est_pe = NIO_MATRIX()
        self.est_peg = NIO_MATRIX()
        self.est_pb = NIO_MATRIX()
        self.est_roe = NIO_MATRIX()
        self.est_oper_revenue = NIO_MATRIX()
        self.est_cfps = NIO_MATRIX()
        self.est_dps = NIO_MATRIX()
        self.est_bps = NIO_MATRIX()
        self.est_ebit = NIO_MATRIX()
        self.est_ebitda = NIO_MATRIX()
        self.est_total_profit = NIO_MATRIX()
        self.est_oper_profit = NIO_MATRIX()
        self.est_oper_cost = NIO_MATRIX()
        self.benchmark_yr = NIO_MATRIX()
        self.est_baseshare = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.net_profit,self.tag + '.net_profit')
        self.addDailyData(self.est_eps,self.tag + '.est_eps')
        self.addDailyData(self.est_pe,self.tag + '.est_pe')
        self.addDailyData(self.est_peg,self.tag + '.est_peg')
        self.addDailyData(self.est_pb,self.tag + '.est_pb')
        self.addDailyData(self.est_roe,self.tag + '.est_roe')
        self.addDailyData(self.est_oper_revenue,self.tag + '.est_oper_revenue')
        self.addDailyData(self.est_cfps,self.tag + '.est_cfps')
        self.addDailyData(self.est_dps,self.tag + '.est_dps')
        self.addDailyData(self.est_bps,self.tag + '.est_bps')
        self.addDailyData(self.est_ebit,self.tag + '.est_ebit')
        self.addDailyData(self.est_ebitda,self.tag + '.est_ebitda')
        self.addDailyData(self.est_total_profit,self.tag + '.est_total_profit')
        self.addDailyData(self.est_oper_profit,self.tag + '.est_oper_profit')
        self.addDailyData(self.est_oper_cost,self.tag + '.est_oper_cost')
        self.addDailyData(self.benchmark_yr,self.tag + '.benchmark_yr')
        self.addDailyData(self.est_baseshare,self.tag + '.est_baseshare')
        return

    def loadDay(self, di):
        self.fillnan(di)  # set default value
        if di == len(uv.Dates) - 1:
            return
        if di > 1 and self.backfill:  # backfill
            self.doBackfill(di)
        filepath = os.path.join(self.dataPath, '%d' % uv.Dates[di])
        if not os.path.isfile(filepath):
            print('[ %s ] %s missing on day %d' %  (self.tag, filepath, uv.Dates[di]))
            return
        infile = open(filepath, 'r')
        infile.readline() # skip title line
        updated = 0
        for line in infile:
            linespt = line.strip('\n').split(',')
            # a field could be blank if its value is missing
            linespt = [np.nan if x == '' else x for x in linespt]
            ticker = linespt[0][0:6]
            ii = uv.Instruments.lookup(ticker)
            if ii < 0:
                continue
            self.net_profit[di, ii]  = float(linespt[3])
            self.est_eps[di, ii]  = float(linespt[4])
            self.est_pe[di, ii]  = float(linespt[5])
            self.est_peg[di, ii]  = float(linespt[6])
            self.est_pb[di, ii]  = float(linespt[7])
            self.est_roe[di, ii]  = float(linespt[8])
            self.est_oper_revenue[di, ii]  = float(linespt[9])
            self.est_cfps[di, ii]  = float(linespt[10])
            self.est_dps[di, ii]  = float(linespt[11])
            self.est_bps[di, ii]  = float(linespt[12])
            self.est_ebit[di, ii]  = float(linespt[13])
            self.est_ebitda[di, ii]  = float(linespt[14])
            self.est_total_profit[di, ii]  = float(linespt[15])
            self.est_oper_profit[di, ii]  = float(linespt[16])
            self.est_oper_cost[di, ii]  = float(linespt[17])
            self.benchmark_yr[di, ii]  = float(linespt[18])
            self.est_baseshare[di, ii]  = float(linespt[19])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.net_profit[di] = self.net_profit[di - 1]
        self.est_eps[di] = self.est_eps[di - 1]
        self.est_pe[di] = self.est_pe[di - 1]
        self.est_peg[di] = self.est_peg[di - 1]
        self.est_pb[di] = self.est_pb[di - 1]
        self.est_roe[di] = self.est_roe[di - 1]
        self.est_oper_revenue[di] = self.est_oper_revenue[di - 1]
        self.est_cfps[di] = self.est_cfps[di - 1]
        self.est_dps[di] = self.est_dps[di - 1]
        self.est_bps[di] = self.est_bps[di - 1]
        self.est_ebit[di] = self.est_ebit[di - 1]
        self.est_ebitda[di] = self.est_ebitda[di - 1]
        self.est_total_profit[di] = self.est_total_profit[di - 1]
        self.est_oper_profit[di] = self.est_oper_profit[di - 1]
        self.est_oper_cost[di] = self.est_oper_cost[di - 1]
        self.benchmark_yr[di] = self.benchmark_yr[di - 1]
        self.est_baseshare[di] = self.est_baseshare[di - 1]