
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgrequ_fancy_factors_table5(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.AI_DA_PE_60 = NIO_MATRIX()
        self.AI_DA_PE_90 = NIO_MATRIX()
        self.AI_DA_PS_30 = NIO_MATRIX()
        self.AI_DA_PS_60 = NIO_MATRIX()
        self.AI_DA_PS_90 = NIO_MATRIX()
        self.AST_RPT_SENTIMENT_W = NIO_MATRIX()
        self.AST_RPT_SENTIMENT_Z180 = NIO_MATRIX()
        self.AST_RPT_SENTIMENT_Z365 = NIO_MATRIX()
        self.AST_RPT_SENTIMENT_Z730 = NIO_MATRIX()
        self.FMZL_1Y_IPCNUM_SUM = NIO_MATRIX()
        self.FMZL_1Y_RELATEDNUM_SUM = NIO_MATRIX()
        self.FMZL_1Y_OWNPARENT_SUM = NIO_MATRIX()
        self.FMZL_1Y_REVIEWDAY_SUM = NIO_MATRIX()
        self.FMZL_1Y_RELATEDNUM_MAX = NIO_MATRIX()
        self.BCVP_05M_20D = NIO_MATRIX()
        self.OCVP_05M_20D = NIO_MATRIX()
        self.CORR_VPL_05M_20D = NIO_MATRIX()
        self.UPP_01M_20D = NIO_MATRIX()
        self.DDP_01M_20D = NIO_MATRIX()
        self.VOLL_01M_20D = NIO_MATRIX()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)
        self.addDailyData(self.AI_DA_PE_60,self.tag + '.AI_DA_PE_60')
        self.addDailyData(self.AI_DA_PE_90,self.tag + '.AI_DA_PE_90')
        self.addDailyData(self.AI_DA_PS_30,self.tag + '.AI_DA_PS_30')
        self.addDailyData(self.AI_DA_PS_60,self.tag + '.AI_DA_PS_60')
        self.addDailyData(self.AI_DA_PS_90,self.tag + '.AI_DA_PS_90')
        self.addDailyData(self.AST_RPT_SENTIMENT_W,self.tag + '.AST_RPT_SENTIMENT_W')
        self.addDailyData(self.AST_RPT_SENTIMENT_Z180,self.tag + '.AST_RPT_SENTIMENT_Z180')
        self.addDailyData(self.AST_RPT_SENTIMENT_Z365,self.tag + '.AST_RPT_SENTIMENT_Z365')
        self.addDailyData(self.AST_RPT_SENTIMENT_Z730,self.tag + '.AST_RPT_SENTIMENT_Z730')
        self.addDailyData(self.FMZL_1Y_IPCNUM_SUM,self.tag + '.FMZL_1Y_IPCNUM_SUM')
        self.addDailyData(self.FMZL_1Y_RELATEDNUM_SUM,self.tag + '.FMZL_1Y_RELATEDNUM_SUM')
        self.addDailyData(self.FMZL_1Y_OWNPARENT_SUM,self.tag + '.FMZL_1Y_OWNPARENT_SUM')
        self.addDailyData(self.FMZL_1Y_REVIEWDAY_SUM,self.tag + '.FMZL_1Y_REVIEWDAY_SUM')
        self.addDailyData(self.FMZL_1Y_RELATEDNUM_MAX,self.tag + '.FMZL_1Y_RELATEDNUM_MAX')
        self.addDailyData(self.BCVP_05M_20D,self.tag + '.BCVP_05M_20D')
        self.addDailyData(self.OCVP_05M_20D,self.tag + '.OCVP_05M_20D')
        self.addDailyData(self.CORR_VPL_05M_20D,self.tag + '.CORR_VPL_05M_20D')
        self.addDailyData(self.UPP_01M_20D,self.tag + '.UPP_01M_20D')
        self.addDailyData(self.DDP_01M_20D,self.tag + '.DDP_01M_20D')
        self.addDailyData(self.VOLL_01M_20D,self.tag + '.VOLL_01M_20D')
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
            self.AI_DA_PE_60[di, ii]  = float(linespt[3])
            self.AI_DA_PE_90[di, ii]  = float(linespt[4])
            self.AI_DA_PS_30[di, ii]  = float(linespt[5])
            self.AI_DA_PS_60[di, ii]  = float(linespt[6])
            self.AI_DA_PS_90[di, ii]  = float(linespt[7])
            self.AST_RPT_SENTIMENT_W[di, ii]  = float(linespt[8])
            self.AST_RPT_SENTIMENT_Z180[di, ii]  = float(linespt[9])
            self.AST_RPT_SENTIMENT_Z365[di, ii]  = float(linespt[10])
            self.AST_RPT_SENTIMENT_Z730[di, ii]  = float(linespt[11])
            self.FMZL_1Y_IPCNUM_SUM[di, ii]  = float(linespt[12])
            self.FMZL_1Y_RELATEDNUM_SUM[di, ii]  = float(linespt[13])
            self.FMZL_1Y_OWNPARENT_SUM[di, ii]  = float(linespt[14])
            self.FMZL_1Y_REVIEWDAY_SUM[di, ii]  = float(linespt[15])
            self.FMZL_1Y_RELATEDNUM_MAX[di, ii]  = float(linespt[16])
            self.BCVP_05M_20D[di, ii]  = float(linespt[17])
            self.OCVP_05M_20D[di, ii]  = float(linespt[18])
            self.CORR_VPL_05M_20D[di, ii]  = float(linespt[19])
            self.UPP_01M_20D[di, ii]  = float(linespt[20])
            self.DDP_01M_20D[di, ii]  = float(linespt[21])
            self.VOLL_01M_20D[di, ii]  = float(linespt[22])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

    def doBackfill(self, di):

        self.AI_DA_PE_60[di] = self.AI_DA_PE_60[di - 1]
        self.AI_DA_PE_90[di] = self.AI_DA_PE_90[di - 1]
        self.AI_DA_PS_30[di] = self.AI_DA_PS_30[di - 1]
        self.AI_DA_PS_60[di] = self.AI_DA_PS_60[di - 1]
        self.AI_DA_PS_90[di] = self.AI_DA_PS_90[di - 1]
        self.AST_RPT_SENTIMENT_W[di] = self.AST_RPT_SENTIMENT_W[di - 1]
        self.AST_RPT_SENTIMENT_Z180[di] = self.AST_RPT_SENTIMENT_Z180[di - 1]
        self.AST_RPT_SENTIMENT_Z365[di] = self.AST_RPT_SENTIMENT_Z365[di - 1]
        self.AST_RPT_SENTIMENT_Z730[di] = self.AST_RPT_SENTIMENT_Z730[di - 1]
        self.FMZL_1Y_IPCNUM_SUM[di] = self.FMZL_1Y_IPCNUM_SUM[di - 1]
        self.FMZL_1Y_RELATEDNUM_SUM[di] = self.FMZL_1Y_RELATEDNUM_SUM[di - 1]
        self.FMZL_1Y_OWNPARENT_SUM[di] = self.FMZL_1Y_OWNPARENT_SUM[di - 1]
        self.FMZL_1Y_REVIEWDAY_SUM[di] = self.FMZL_1Y_REVIEWDAY_SUM[di - 1]
        self.FMZL_1Y_RELATEDNUM_MAX[di] = self.FMZL_1Y_RELATEDNUM_MAX[di - 1]
        self.BCVP_05M_20D[di] = self.BCVP_05M_20D[di - 1]
        self.OCVP_05M_20D[di] = self.OCVP_05M_20D[di - 1]
        self.CORR_VPL_05M_20D[di] = self.CORR_VPL_05M_20D[di - 1]
        self.UPP_01M_20D[di] = self.UPP_01M_20D[di - 1]
        self.DDP_01M_20D[di] = self.DDP_01M_20D[di - 1]
        self.VOLL_01M_20D[di] = self.VOLL_01M_20D[di - 1]