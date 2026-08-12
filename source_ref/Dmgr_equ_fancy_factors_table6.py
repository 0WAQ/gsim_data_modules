
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrequ_fancy_factors_table6(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.FF3R2_20 = NIO_MATRIX()
        self.FF3SPMOM_20 = NIO_MATRIX()
        self.FF3SPVOL_20 = NIO_MATRIX()
        self.FF3SYSMOM_20 = NIO_MATRIX()
        self.FF3SYSVOL_20 = NIO_MATRIX()
        self.RMVOL_20 = NIO_MATRIX()
        self.RMVOL_60 = NIO_MATRIX()
        self.RMVOL_120 = NIO_MATRIX()
        self.TRVOL_20 = NIO_MATRIX()
        self.TRVOL_60 = NIO_MATRIX()
        self.TRVOL_120 = NIO_MATRIX()
        self.TRVOV = NIO_MATRIX()
        self.MINTVAL_QUA_20D = NIO_MATRIX()
        self.MINTVAL_SKEW_20D = NIO_MATRIX()
        self.MINTVAL_MTS_20D = NIO_MATRIX()
        self.MINTVAL_MTE_20D = NIO_MATRIX()
        self.SECTVAL_KURT_20D = NIO_MATRIX()
        self.OVAL_MBSR_20D = NIO_MATRIX()
        self.GMM_MEAN_1M_20D = NIO_MATRIX()
        self.GMM_DMEAN_1M_20D = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.FF3R2_20,self.tag + '.FF3R2_20')
        self.addDailyData(self.FF3SPMOM_20,self.tag + '.FF3SPMOM_20')
        self.addDailyData(self.FF3SPVOL_20,self.tag + '.FF3SPVOL_20')
        self.addDailyData(self.FF3SYSMOM_20,self.tag + '.FF3SYSMOM_20')
        self.addDailyData(self.FF3SYSVOL_20,self.tag + '.FF3SYSVOL_20')
        self.addDailyData(self.RMVOL_20,self.tag + '.RMVOL_20')
        self.addDailyData(self.RMVOL_60,self.tag + '.RMVOL_60')
        self.addDailyData(self.RMVOL_120,self.tag + '.RMVOL_120')
        self.addDailyData(self.TRVOL_20,self.tag + '.TRVOL_20')
        self.addDailyData(self.TRVOL_60,self.tag + '.TRVOL_60')
        self.addDailyData(self.TRVOL_120,self.tag + '.TRVOL_120')
        self.addDailyData(self.TRVOV,self.tag + '.TRVOV')
        self.addDailyData(self.MINTVAL_QUA_20D,self.tag + '.MINTVAL_QUA_20D')
        self.addDailyData(self.MINTVAL_SKEW_20D,self.tag + '.MINTVAL_SKEW_20D')
        self.addDailyData(self.MINTVAL_MTS_20D,self.tag + '.MINTVAL_MTS_20D')
        self.addDailyData(self.MINTVAL_MTE_20D,self.tag + '.MINTVAL_MTE_20D')
        self.addDailyData(self.SECTVAL_KURT_20D,self.tag + '.SECTVAL_KURT_20D')
        self.addDailyData(self.OVAL_MBSR_20D,self.tag + '.OVAL_MBSR_20D')
        self.addDailyData(self.GMM_MEAN_1M_20D,self.tag + '.GMM_MEAN_1M_20D')
        self.addDailyData(self.GMM_DMEAN_1M_20D,self.tag + '.GMM_DMEAN_1M_20D')
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
            ticker = linespt[1][0:6]
            ii = uv.Instruments.lookup(ticker)
            if ii < 0:
                continue
            self.FF3R2_20[di, ii]  = float(linespt[3])
            self.FF3SPMOM_20[di, ii]  = float(linespt[4])
            self.FF3SPVOL_20[di, ii]  = float(linespt[5])
            self.FF3SYSMOM_20[di, ii]  = float(linespt[6])
            self.FF3SYSVOL_20[di, ii]  = float(linespt[7])
            self.RMVOL_20[di, ii]  = float(linespt[8])
            self.RMVOL_60[di, ii]  = float(linespt[9])
            self.RMVOL_120[di, ii]  = float(linespt[10])
            self.TRVOL_20[di, ii]  = float(linespt[11])
            self.TRVOL_60[di, ii]  = float(linespt[12])
            self.TRVOL_120[di, ii]  = float(linespt[13])
            self.TRVOV[di, ii]  = float(linespt[14])
            self.MINTVAL_QUA_20D[di, ii]  = float(linespt[15])
            self.MINTVAL_SKEW_20D[di, ii]  = float(linespt[16])
            self.MINTVAL_MTS_20D[di, ii]  = float(linespt[17])
            self.MINTVAL_MTE_20D[di, ii]  = float(linespt[18])
            self.SECTVAL_KURT_20D[di, ii]  = float(linespt[19])
            self.OVAL_MBSR_20D[di, ii]  = float(linespt[20])
            self.GMM_MEAN_1M_20D[di, ii]  = float(linespt[21])
            self.GMM_DMEAN_1M_20D[di, ii]  = float(linespt[22])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.FF3R2_20[di] = self.FF3R2_20[di - 1]
        self.FF3SPMOM_20[di] = self.FF3SPMOM_20[di - 1]
        self.FF3SPVOL_20[di] = self.FF3SPVOL_20[di - 1]
        self.FF3SYSMOM_20[di] = self.FF3SYSMOM_20[di - 1]
        self.FF3SYSVOL_20[di] = self.FF3SYSVOL_20[di - 1]
        self.RMVOL_20[di] = self.RMVOL_20[di - 1]
        self.RMVOL_60[di] = self.RMVOL_60[di - 1]
        self.RMVOL_120[di] = self.RMVOL_120[di - 1]
        self.TRVOL_20[di] = self.TRVOL_20[di - 1]
        self.TRVOL_60[di] = self.TRVOL_60[di - 1]
        self.TRVOL_120[di] = self.TRVOL_120[di - 1]
        self.TRVOV[di] = self.TRVOV[di - 1]
        self.MINTVAL_QUA_20D[di] = self.MINTVAL_QUA_20D[di - 1]
        self.MINTVAL_SKEW_20D[di] = self.MINTVAL_SKEW_20D[di - 1]
        self.MINTVAL_MTS_20D[di] = self.MINTVAL_MTS_20D[di - 1]
        self.MINTVAL_MTE_20D[di] = self.MINTVAL_MTE_20D[di - 1]
        self.SECTVAL_KURT_20D[di] = self.SECTVAL_KURT_20D[di - 1]
        self.OVAL_MBSR_20D[di] = self.OVAL_MBSR_20D[di - 1]
        self.GMM_MEAN_1M_20D[di] = self.GMM_MEAN_1M_20D[di - 1]
        self.GMM_DMEAN_1M_20D[di] = self.GMM_DMEAN_1M_20D[di - 1]