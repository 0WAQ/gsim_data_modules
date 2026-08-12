
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrequ_h2l_factor_t3(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.APT_OUTFLOW_RATIO = NIO_MATRIX()
        self.ARPP = NIO_MATRIX()
        self.NET_INFLOW_L_RATIO = NIO_MATRIX()
        self.DDP = NIO_MATRIX()
        self.AMP_STD = NIO_MATRIX()
        self.FUZZY_VOV = NIO_MATRIX()
        self.MIN_IRET_KURT_STD = NIO_MATRIX()
        self.MIN_IRET_SKEW_STD = NIO_MATRIX()
        self.MIN_IRET_STD_AVE = NIO_MATRIX()
        self.MIN_IRET_STD_STD = NIO_MATRIX()
        self.MIN_RET_KURT_STD = NIO_MATRIX()
        self.MIN_RET_SKEW_STD = NIO_MATRIX()
        self.MIN_RET_STD_AVE = NIO_MATRIX()
        self.MIN_RET_STD_STD = NIO_MATRIX()
        self.RSJ_RATIO = NIO_MATRIX()
        self.UP_VOL_RATIO = NIO_MATRIX()
        self.UPP = NIO_MATRIX()
        self.VOLL = NIO_MATRIX()
        self.INT_RET = NIO_MATRIX()
        self.INT_RET_1H = NIO_MATRIX()
        self.INT_RET_2H = NIO_MATRIX()
        self.INT_RET_3H = NIO_MATRIX()
        self.INT_RET_4H = NIO_MATRIX()
        self.INT_RET_DE1 = NIO_MATRIX()
        self.MILD_RET_1H = NIO_MATRIX()
        self.MOM_L = NIO_MATRIX()
        self.OVP = NIO_MATRIX()
        self.RET_APT_C = NIO_MATRIX()
        self.RET_HVOL_REV = NIO_MATRIX()
        self.RET_OV = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.APT_OUTFLOW_RATIO,self.tag + '.APT_OUTFLOW_RATIO')
        self.addDailyData(self.ARPP,self.tag + '.ARPP')
        self.addDailyData(self.NET_INFLOW_L_RATIO,self.tag + '.NET_INFLOW_L_RATIO')
        self.addDailyData(self.DDP,self.tag + '.DDP')
        self.addDailyData(self.AMP_STD,self.tag + '.AMP_STD')
        self.addDailyData(self.FUZZY_VOV,self.tag + '.FUZZY_VOV')
        self.addDailyData(self.MIN_IRET_KURT_STD,self.tag + '.MIN_IRET_KURT_STD')
        self.addDailyData(self.MIN_IRET_SKEW_STD,self.tag + '.MIN_IRET_SKEW_STD')
        self.addDailyData(self.MIN_IRET_STD_AVE,self.tag + '.MIN_IRET_STD_AVE')
        self.addDailyData(self.MIN_IRET_STD_STD,self.tag + '.MIN_IRET_STD_STD')
        self.addDailyData(self.MIN_RET_KURT_STD,self.tag + '.MIN_RET_KURT_STD')
        self.addDailyData(self.MIN_RET_SKEW_STD,self.tag + '.MIN_RET_SKEW_STD')
        self.addDailyData(self.MIN_RET_STD_AVE,self.tag + '.MIN_RET_STD_AVE')
        self.addDailyData(self.MIN_RET_STD_STD,self.tag + '.MIN_RET_STD_STD')
        self.addDailyData(self.RSJ_RATIO,self.tag + '.RSJ_RATIO')
        self.addDailyData(self.UP_VOL_RATIO,self.tag + '.UP_VOL_RATIO')
        self.addDailyData(self.UPP,self.tag + '.UPP')
        self.addDailyData(self.VOLL,self.tag + '.VOLL')
        self.addDailyData(self.INT_RET,self.tag + '.INT_RET')
        self.addDailyData(self.INT_RET_1H,self.tag + '.INT_RET_1H')
        self.addDailyData(self.INT_RET_2H,self.tag + '.INT_RET_2H')
        self.addDailyData(self.INT_RET_3H,self.tag + '.INT_RET_3H')
        self.addDailyData(self.INT_RET_4H,self.tag + '.INT_RET_4H')
        self.addDailyData(self.INT_RET_DE1,self.tag + '.INT_RET_DE1')
        self.addDailyData(self.MILD_RET_1H,self.tag + '.MILD_RET_1H')
        self.addDailyData(self.MOM_L,self.tag + '.MOM_L')
        self.addDailyData(self.OVP,self.tag + '.OVP')
        self.addDailyData(self.RET_APT_C,self.tag + '.RET_APT_C')
        self.addDailyData(self.RET_HVOL_REV,self.tag + '.RET_HVOL_REV')
        self.addDailyData(self.RET_OV,self.tag + '.RET_OV')
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
            self.APT_OUTFLOW_RATIO[di, ii]  = float(linespt[3])
            self.ARPP[di, ii]  = float(linespt[4])
            self.NET_INFLOW_L_RATIO[di, ii]  = float(linespt[5])
            self.DDP[di, ii]  = float(linespt[6])
            self.AMP_STD[di, ii]  = float(linespt[7])
            self.FUZZY_VOV[di, ii]  = float(linespt[8])
            self.MIN_IRET_KURT_STD[di, ii]  = float(linespt[9])
            self.MIN_IRET_SKEW_STD[di, ii]  = float(linespt[10])
            self.MIN_IRET_STD_AVE[di, ii]  = float(linespt[11])
            self.MIN_IRET_STD_STD[di, ii]  = float(linespt[12])
            self.MIN_RET_KURT_STD[di, ii]  = float(linespt[13])
            self.MIN_RET_SKEW_STD[di, ii]  = float(linespt[14])
            self.MIN_RET_STD_AVE[di, ii]  = float(linespt[15])
            self.MIN_RET_STD_STD[di, ii]  = float(linespt[16])
            self.RSJ_RATIO[di, ii]  = float(linespt[17])
            self.UP_VOL_RATIO[di, ii]  = float(linespt[18])
            self.UPP[di, ii]  = float(linespt[19])
            self.VOLL[di, ii]  = float(linespt[20])
            self.INT_RET[di, ii]  = float(linespt[21])
            self.INT_RET_1H[di, ii]  = float(linespt[22])
            self.INT_RET_2H[di, ii]  = float(linespt[23])
            self.INT_RET_3H[di, ii]  = float(linespt[24])
            self.INT_RET_4H[di, ii]  = float(linespt[25])
            self.INT_RET_DE1[di, ii]  = float(linespt[26])
            self.MILD_RET_1H[di, ii]  = float(linespt[27])
            self.MOM_L[di, ii]  = float(linespt[28])
            self.OVP[di, ii]  = float(linespt[29])
            self.RET_APT_C[di, ii]  = float(linespt[30])
            self.RET_HVOL_REV[di, ii]  = float(linespt[31])
            self.RET_OV[di, ii]  = float(linespt[32])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.APT_OUTFLOW_RATIO[di] = self.APT_OUTFLOW_RATIO[di - 1]
        self.ARPP[di] = self.ARPP[di - 1]
        self.NET_INFLOW_L_RATIO[di] = self.NET_INFLOW_L_RATIO[di - 1]
        self.DDP[di] = self.DDP[di - 1]
        self.AMP_STD[di] = self.AMP_STD[di - 1]
        self.FUZZY_VOV[di] = self.FUZZY_VOV[di - 1]
        self.MIN_IRET_KURT_STD[di] = self.MIN_IRET_KURT_STD[di - 1]
        self.MIN_IRET_SKEW_STD[di] = self.MIN_IRET_SKEW_STD[di - 1]
        self.MIN_IRET_STD_AVE[di] = self.MIN_IRET_STD_AVE[di - 1]
        self.MIN_IRET_STD_STD[di] = self.MIN_IRET_STD_STD[di - 1]
        self.MIN_RET_KURT_STD[di] = self.MIN_RET_KURT_STD[di - 1]
        self.MIN_RET_SKEW_STD[di] = self.MIN_RET_SKEW_STD[di - 1]
        self.MIN_RET_STD_AVE[di] = self.MIN_RET_STD_AVE[di - 1]
        self.MIN_RET_STD_STD[di] = self.MIN_RET_STD_STD[di - 1]
        self.RSJ_RATIO[di] = self.RSJ_RATIO[di - 1]
        self.UP_VOL_RATIO[di] = self.UP_VOL_RATIO[di - 1]
        self.UPP[di] = self.UPP[di - 1]
        self.VOLL[di] = self.VOLL[di - 1]
        self.INT_RET[di] = self.INT_RET[di - 1]
        self.INT_RET_1H[di] = self.INT_RET_1H[di - 1]
        self.INT_RET_2H[di] = self.INT_RET_2H[di - 1]
        self.INT_RET_3H[di] = self.INT_RET_3H[di - 1]
        self.INT_RET_4H[di] = self.INT_RET_4H[di - 1]
        self.INT_RET_DE1[di] = self.INT_RET_DE1[di - 1]
        self.MILD_RET_1H[di] = self.MILD_RET_1H[di - 1]
        self.MOM_L[di] = self.MOM_L[di - 1]
        self.OVP[di] = self.OVP[di - 1]
        self.RET_APT_C[di] = self.RET_APT_C[di - 1]
        self.RET_HVOL_REV[di] = self.RET_HVOL_REV[di - 1]
        self.RET_OV[di] = self.RET_OV[di - 1]