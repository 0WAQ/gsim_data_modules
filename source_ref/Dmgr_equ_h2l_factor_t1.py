
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrequ_h2l_factor_t1(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.BCVP_5MIN = NIO_MATRIX()
        self.BCVP_15MIN = NIO_MATRIX()
        self.MOVP = NIO_MATRIX()
        self.NCV = NIO_MATRIX()
        self.OC_BCVP = NIO_MATRIX()
        self.OCVP = NIO_MATRIX()
        self.PCV = NIO_MATRIX()
        self.TCV = NIO_MATRIX()
        self.AOVP_5MIN_10D = NIO_MATRIX()
        self.APD_STD = NIO_MATRIX()
        self.MIN_VOL_KURT_AVE = NIO_MATRIX()
        self.MIN_VOL_KURT_STD = NIO_MATRIX()
        self.MIN_VOL_SKEW_AVE = NIO_MATRIX()
        self.MIN_VOL_SKEW_STD = NIO_MATRIX()
        self.MIN_VOL_STD_AVE = NIO_MATRIX()
        self.MIN_VOL_STD_STD = NIO_MATRIX()
        self.VAR_RATIO = NIO_MATRIX()
        self.VPC_STD = NIO_MATRIX()
        self.CORR_VPL = NIO_MATRIX()
        self.AR_V_CORR = NIO_MATRIX()
        self.CDPDP = NIO_MATRIX()
        self.CDPP = NIO_MATRIX()
        self.CDVDP_V = NIO_MATRIX()
        self.CDVDV = NIO_MATRIX()
        self.CDVV = NIO_MATRIX()
        self.DPN_DPN_CORR = NIO_MATRIX()
        self.DPN_P_CORR = NIO_MATRIX()
        self.DPP_DPP_CORR = NIO_MATRIX()
        self.DPP_P_CORR = NIO_MATRIX()
        self.DVN_DPN_CORR = NIO_MATRIX()
        self.DVN_DPP_CORR = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.BCVP_5MIN,self.tag + '.BCVP_5MIN')
        self.addDailyData(self.BCVP_15MIN,self.tag + '.BCVP_15MIN')
        self.addDailyData(self.MOVP,self.tag + '.MOVP')
        self.addDailyData(self.NCV,self.tag + '.NCV')
        self.addDailyData(self.OC_BCVP,self.tag + '.OC_BCVP')
        self.addDailyData(self.OCVP,self.tag + '.OCVP')
        self.addDailyData(self.PCV,self.tag + '.PCV')
        self.addDailyData(self.TCV,self.tag + '.TCV')
        self.addDailyData(self.AOVP_5MIN_10D,self.tag + '.AOVP_5MIN_10D')
        self.addDailyData(self.APD_STD,self.tag + '.APD_STD')
        self.addDailyData(self.MIN_VOL_KURT_AVE,self.tag + '.MIN_VOL_KURT_AVE')
        self.addDailyData(self.MIN_VOL_KURT_STD,self.tag + '.MIN_VOL_KURT_STD')
        self.addDailyData(self.MIN_VOL_SKEW_AVE,self.tag + '.MIN_VOL_SKEW_AVE')
        self.addDailyData(self.MIN_VOL_SKEW_STD,self.tag + '.MIN_VOL_SKEW_STD')
        self.addDailyData(self.MIN_VOL_STD_AVE,self.tag + '.MIN_VOL_STD_AVE')
        self.addDailyData(self.MIN_VOL_STD_STD,self.tag + '.MIN_VOL_STD_STD')
        self.addDailyData(self.VAR_RATIO,self.tag + '.VAR_RATIO')
        self.addDailyData(self.VPC_STD,self.tag + '.VPC_STD')
        self.addDailyData(self.CORR_VPL,self.tag + '.CORR_VPL')
        self.addDailyData(self.AR_V_CORR,self.tag + '.AR_V_CORR')
        self.addDailyData(self.CDPDP,self.tag + '.CDPDP')
        self.addDailyData(self.CDPP,self.tag + '.CDPP')
        self.addDailyData(self.CDVDP_V,self.tag + '.CDVDP_V')
        self.addDailyData(self.CDVDV,self.tag + '.CDVDV')
        self.addDailyData(self.CDVV,self.tag + '.CDVV')
        self.addDailyData(self.DPN_DPN_CORR,self.tag + '.DPN_DPN_CORR')
        self.addDailyData(self.DPN_P_CORR,self.tag + '.DPN_P_CORR')
        self.addDailyData(self.DPP_DPP_CORR,self.tag + '.DPP_DPP_CORR')
        self.addDailyData(self.DPP_P_CORR,self.tag + '.DPP_P_CORR')
        self.addDailyData(self.DVN_DPN_CORR,self.tag + '.DVN_DPN_CORR')
        self.addDailyData(self.DVN_DPP_CORR,self.tag + '.DVN_DPP_CORR')
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
            self.BCVP_5MIN[di, ii]  = float(linespt[3])
            self.BCVP_15MIN[di, ii]  = float(linespt[4])
            self.MOVP[di, ii]  = float(linespt[5])
            self.NCV[di, ii]  = float(linespt[6])
            self.OC_BCVP[di, ii]  = float(linespt[7])
            self.OCVP[di, ii]  = float(linespt[8])
            self.PCV[di, ii]  = float(linespt[9])
            self.TCV[di, ii]  = float(linespt[10])
            self.AOVP_5MIN_10D[di, ii]  = float(linespt[11])
            self.APD_STD[di, ii]  = float(linespt[12])
            self.MIN_VOL_KURT_AVE[di, ii]  = float(linespt[13])
            self.MIN_VOL_KURT_STD[di, ii]  = float(linespt[14])
            self.MIN_VOL_SKEW_AVE[di, ii]  = float(linespt[15])
            self.MIN_VOL_SKEW_STD[di, ii]  = float(linespt[16])
            self.MIN_VOL_STD_AVE[di, ii]  = float(linespt[17])
            self.MIN_VOL_STD_STD[di, ii]  = float(linespt[18])
            self.VAR_RATIO[di, ii]  = float(linespt[19])
            self.VPC_STD[di, ii]  = float(linespt[20])
            self.CORR_VPL[di, ii]  = float(linespt[21])
            self.AR_V_CORR[di, ii]  = float(linespt[22])
            self.CDPDP[di, ii]  = float(linespt[23])
            self.CDPP[di, ii]  = float(linespt[24])
            self.CDVDP_V[di, ii]  = float(linespt[25])
            self.CDVDV[di, ii]  = float(linespt[26])
            self.CDVV[di, ii]  = float(linespt[27])
            self.DPN_DPN_CORR[di, ii]  = float(linespt[28])
            self.DPN_P_CORR[di, ii]  = float(linespt[29])
            self.DPP_DPP_CORR[di, ii]  = float(linespt[30])
            self.DPP_P_CORR[di, ii]  = float(linespt[31])
            self.DVN_DPN_CORR[di, ii]  = float(linespt[32])
            self.DVN_DPP_CORR[di, ii]  = float(linespt[33])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.BCVP_5MIN[di] = self.BCVP_5MIN[di - 1]
        self.BCVP_15MIN[di] = self.BCVP_15MIN[di - 1]
        self.MOVP[di] = self.MOVP[di - 1]
        self.NCV[di] = self.NCV[di - 1]
        self.OC_BCVP[di] = self.OC_BCVP[di - 1]
        self.OCVP[di] = self.OCVP[di - 1]
        self.PCV[di] = self.PCV[di - 1]
        self.TCV[di] = self.TCV[di - 1]
        self.AOVP_5MIN_10D[di] = self.AOVP_5MIN_10D[di - 1]
        self.APD_STD[di] = self.APD_STD[di - 1]
        self.MIN_VOL_KURT_AVE[di] = self.MIN_VOL_KURT_AVE[di - 1]
        self.MIN_VOL_KURT_STD[di] = self.MIN_VOL_KURT_STD[di - 1]
        self.MIN_VOL_SKEW_AVE[di] = self.MIN_VOL_SKEW_AVE[di - 1]
        self.MIN_VOL_SKEW_STD[di] = self.MIN_VOL_SKEW_STD[di - 1]
        self.MIN_VOL_STD_AVE[di] = self.MIN_VOL_STD_AVE[di - 1]
        self.MIN_VOL_STD_STD[di] = self.MIN_VOL_STD_STD[di - 1]
        self.VAR_RATIO[di] = self.VAR_RATIO[di - 1]
        self.VPC_STD[di] = self.VPC_STD[di - 1]
        self.CORR_VPL[di] = self.CORR_VPL[di - 1]
        self.AR_V_CORR[di] = self.AR_V_CORR[di - 1]
        self.CDPDP[di] = self.CDPDP[di - 1]
        self.CDPP[di] = self.CDPP[di - 1]
        self.CDVDP_V[di] = self.CDVDP_V[di - 1]
        self.CDVDV[di] = self.CDVDV[di - 1]
        self.CDVV[di] = self.CDVV[di - 1]
        self.DPN_DPN_CORR[di] = self.DPN_DPN_CORR[di - 1]
        self.DPN_P_CORR[di] = self.DPN_P_CORR[di - 1]
        self.DPP_DPP_CORR[di] = self.DPP_DPP_CORR[di - 1]
        self.DPP_P_CORR[di] = self.DPP_P_CORR[di - 1]
        self.DVN_DPN_CORR[di] = self.DVN_DPN_CORR[di - 1]
        self.DVN_DPP_CORR[di] = self.DVN_DPP_CORR[di - 1]