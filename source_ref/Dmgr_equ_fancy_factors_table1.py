
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrequ_fancy_factors_table1(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.UDSL_DWL = NIO_MATRIX()
        self.UDSL_UCL = NIO_MATRIX()
        self.UDSL = NIO_MATRIX()
        self.ASHAREHOLDER_Z = NIO_MATRIX()
        self.TA_ENTROPY = NIO_MATRIX()
        self.CORR_VP = NIO_MATRIX()
        self.APB_SKEW = NIO_MATRIX()
        self.SUDE = NIO_MATRIX()
        self.SUDREV = NIO_MATRIX()
        self.LPNP_Q = NIO_MATRIX()
        self.NP_Q_YOY = NIO_MATRIX()
        self.NP_YTD_YOY = NIO_MATRIX()
        self.NP_TTM_QOQ = NIO_MATRIX()
        self.NP_TTM_YOY = NIO_MATRIX()
        self.REV_Q_YOY = NIO_MATRIX()
        self.REV_YTD_YOY = NIO_MATRIX()
        self.REV_TTM_QOQ = NIO_MATRIX()
        self.REV_TTM_YOY = NIO_MATRIX()
        self.RROC_Q = NIO_MATRIX()
        self.OCFA = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.UDSL_DWL,self.tag + '.UDSL_DWL')
        self.addDailyData(self.UDSL_UCL,self.tag + '.UDSL_UCL')
        self.addDailyData(self.UDSL,self.tag + '.UDSL')
        self.addDailyData(self.ASHAREHOLDER_Z,self.tag + '.ASHAREHOLDER_Z')
        self.addDailyData(self.TA_ENTROPY,self.tag + '.TA_ENTROPY')
        self.addDailyData(self.CORR_VP,self.tag + '.CORR_VP')
        self.addDailyData(self.APB_SKEW,self.tag + '.APB_SKEW')
        self.addDailyData(self.SUDE,self.tag + '.SUDE')
        self.addDailyData(self.SUDREV,self.tag + '.SUDREV')
        self.addDailyData(self.LPNP_Q,self.tag + '.LPNP_Q')
        self.addDailyData(self.NP_Q_YOY,self.tag + '.NP_Q_YOY')
        self.addDailyData(self.NP_YTD_YOY,self.tag + '.NP_YTD_YOY')
        self.addDailyData(self.NP_TTM_QOQ,self.tag + '.NP_TTM_QOQ')
        self.addDailyData(self.NP_TTM_YOY,self.tag + '.NP_TTM_YOY')
        self.addDailyData(self.REV_Q_YOY,self.tag + '.REV_Q_YOY')
        self.addDailyData(self.REV_YTD_YOY,self.tag + '.REV_YTD_YOY')
        self.addDailyData(self.REV_TTM_QOQ,self.tag + '.REV_TTM_QOQ')
        self.addDailyData(self.REV_TTM_YOY,self.tag + '.REV_TTM_YOY')
        self.addDailyData(self.RROC_Q,self.tag + '.RROC_Q')
        self.addDailyData(self.OCFA,self.tag + '.OCFA')
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
            self.UDSL_DWL[di, ii]  = float(linespt[3])
            self.UDSL_UCL[di, ii]  = float(linespt[4])
            self.UDSL[di, ii]  = float(linespt[5])
            self.ASHAREHOLDER_Z[di, ii]  = float(linespt[6])
            self.TA_ENTROPY[di, ii]  = float(linespt[7])
            self.CORR_VP[di, ii]  = float(linespt[8])
            self.APB_SKEW[di, ii]  = float(linespt[9])
            self.SUDE[di, ii]  = float(linespt[10])
            self.SUDREV[di, ii]  = float(linespt[11])
            self.LPNP_Q[di, ii]  = float(linespt[12])
            self.NP_Q_YOY[di, ii]  = float(linespt[13])
            self.NP_YTD_YOY[di, ii]  = float(linespt[14])
            self.NP_TTM_QOQ[di, ii]  = float(linespt[15])
            self.NP_TTM_YOY[di, ii]  = float(linespt[16])
            self.REV_Q_YOY[di, ii]  = float(linespt[17])
            self.REV_YTD_YOY[di, ii]  = float(linespt[18])
            self.REV_TTM_QOQ[di, ii]  = float(linespt[19])
            self.REV_TTM_YOY[di, ii]  = float(linespt[20])
            self.RROC_Q[di, ii]  = float(linespt[21])
            self.OCFA[di, ii]  = float(linespt[22])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.UDSL_DWL[di] = self.UDSL_DWL[di - 1]
        self.UDSL_UCL[di] = self.UDSL_UCL[di - 1]
        self.UDSL[di] = self.UDSL[di - 1]
        self.ASHAREHOLDER_Z[di] = self.ASHAREHOLDER_Z[di - 1]
        self.TA_ENTROPY[di] = self.TA_ENTROPY[di - 1]
        self.CORR_VP[di] = self.CORR_VP[di - 1]
        self.APB_SKEW[di] = self.APB_SKEW[di - 1]
        self.SUDE[di] = self.SUDE[di - 1]
        self.SUDREV[di] = self.SUDREV[di - 1]
        self.LPNP_Q[di] = self.LPNP_Q[di - 1]
        self.NP_Q_YOY[di] = self.NP_Q_YOY[di - 1]
        self.NP_YTD_YOY[di] = self.NP_YTD_YOY[di - 1]
        self.NP_TTM_QOQ[di] = self.NP_TTM_QOQ[di - 1]
        self.NP_TTM_YOY[di] = self.NP_TTM_YOY[di - 1]
        self.REV_Q_YOY[di] = self.REV_Q_YOY[di - 1]
        self.REV_YTD_YOY[di] = self.REV_YTD_YOY[di - 1]
        self.REV_TTM_QOQ[di] = self.REV_TTM_QOQ[di - 1]
        self.REV_TTM_YOY[di] = self.REV_TTM_YOY[di - 1]
        self.RROC_Q[di] = self.RROC_Q[di - 1]
        self.OCFA[di] = self.OCFA[di - 1]