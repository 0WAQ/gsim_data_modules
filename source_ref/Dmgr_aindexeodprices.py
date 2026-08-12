
from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import os
import operator
import csv

class Dmgraindexeodprices(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.backfill = False
        self.s_dq_preclose_000016 = NIO_VECTOR()
        self.s_dq_open_000016 = NIO_VECTOR()
        self.s_dq_high_000016 = NIO_VECTOR()
        self.s_dq_low_000016 = NIO_VECTOR()
        self.s_dq_close_000016 = NIO_VECTOR()
        self.s_dq_change_000016 = NIO_VECTOR()
        self.s_dq_pctchange_000016 = NIO_VECTOR()
        self.s_dq_volume_000016 = NIO_VECTOR()
        self.s_dq_amount_000016 = NIO_VECTOR()
        self.s_dq_preclose_000300 = NIO_VECTOR()
        self.s_dq_open_000300 = NIO_VECTOR()
        self.s_dq_high_000300 = NIO_VECTOR()
        self.s_dq_low_000300 = NIO_VECTOR()
        self.s_dq_close_000300 = NIO_VECTOR()
        self.s_dq_change_000300 = NIO_VECTOR()
        self.s_dq_pctchange_000300 = NIO_VECTOR()
        self.s_dq_volume_000300 = NIO_VECTOR()
        self.s_dq_amount_000300 = NIO_VECTOR()
 
        self.s_dq_preclose_000905 = NIO_VECTOR()
        self.s_dq_open_000905 = NIO_VECTOR()
        self.s_dq_high_000905 = NIO_VECTOR()
        self.s_dq_low_000905 = NIO_VECTOR()
        self.s_dq_close_000905 = NIO_VECTOR()
        self.s_dq_change_000905 = NIO_VECTOR()
        self.s_dq_pctchange_000905 = NIO_VECTOR()
        self.s_dq_volume_000905 = NIO_VECTOR()
        self.s_dq_amount_000905 = NIO_VECTOR()

        self.s_dq_preclose_000906 = NIO_VECTOR()
        self.s_dq_open_000906 = NIO_VECTOR()
        self.s_dq_high_000906 = NIO_VECTOR()
        self.s_dq_low_000906 = NIO_VECTOR()
        self.s_dq_close_000906 = NIO_VECTOR()
        self.s_dq_change_000906 = NIO_VECTOR()
        self.s_dq_pctchange_000906 = NIO_VECTOR()
        self.s_dq_volume_000906 = NIO_VECTOR()
        self.s_dq_amount_000906 = NIO_VECTOR()


        self.s_dq_preclose_000852 = NIO_VECTOR()
        self.s_dq_open_000852 = NIO_VECTOR()
        self.s_dq_high_000852 = NIO_VECTOR()
        self.s_dq_low_000852 = NIO_VECTOR()
        self.s_dq_close_000852 = NIO_VECTOR()
        self.s_dq_change_000852 = NIO_VECTOR()
        self.s_dq_pctchange_000852 = NIO_VECTOR()
        self.s_dq_volume_000852 = NIO_VECTOR()
        self.s_dq_amount_000852 = NIO_VECTOR()
        self.s_dq_preclose_399001 = NIO_VECTOR()
        self.s_dq_open_399001 = NIO_VECTOR()
        self.s_dq_high_399001 = NIO_VECTOR()
        self.s_dq_low_399001 = NIO_VECTOR()
        self.s_dq_close_399001 = NIO_VECTOR()
        self.s_dq_change_399001 = NIO_VECTOR()
        self.s_dq_pctchange_399001 = NIO_VECTOR()
        self.s_dq_volume_399001 = NIO_VECTOR()
        self.s_dq_amount_399001 = NIO_VECTOR()
        self.s_dq_preclose_399005 = NIO_VECTOR()
        self.s_dq_open_399005 = NIO_VECTOR()
        self.s_dq_high_399005 = NIO_VECTOR()
        self.s_dq_low_399005 = NIO_VECTOR()
        self.s_dq_close_399005 = NIO_VECTOR()
        self.s_dq_change_399005 = NIO_VECTOR()
        self.s_dq_pctchange_399005 = NIO_VECTOR()
        self.s_dq_volume_399005 = NIO_VECTOR()
        self.s_dq_amount_399005 = NIO_VECTOR()
        self.s_dq_preclose_399006 = NIO_VECTOR()
        self.s_dq_open_399006 = NIO_VECTOR()
        self.s_dq_high_399006 = NIO_VECTOR()
        self.s_dq_low_399006 = NIO_VECTOR()
        self.s_dq_close_399006 = NIO_VECTOR()
        self.s_dq_change_399006 = NIO_VECTOR()
        self.s_dq_pctchange_399006 = NIO_VECTOR()
        self.s_dq_volume_399006 = NIO_VECTOR()
        self.s_dq_amount_399006 = NIO_VECTOR()
        self.s_dq_preclose_000001 = NIO_VECTOR()
        self.s_dq_open_000001 = NIO_VECTOR()
        self.s_dq_high_000001 = NIO_VECTOR()
        self.s_dq_low_000001 = NIO_VECTOR()
        self.s_dq_close_000001 = NIO_VECTOR()
        self.s_dq_change_000001 = NIO_VECTOR()
        self.s_dq_pctchange_000001 = NIO_VECTOR()
        self.s_dq_volume_000001 = NIO_VECTOR()
        self.s_dq_amount_000001 = NIO_VECTOR()

        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.backfill = cfg.getAttributeDefault('backfill', False)

        self.addDailyData(self.s_dq_preclose_000016, self.tag + '.s_dq_preclose_000016')
        self.addDailyData(self.s_dq_open_000016, self.tag + '.s_dq_open_000016')
        self.addDailyData(self.s_dq_high_000016, self.tag + '.s_dq_high_000016')
        self.addDailyData(self.s_dq_low_000016, self.tag + '.s_dq_low_000016')
        self.addDailyData(self.s_dq_close_000016, self.tag + '.s_dq_close_000016')
        self.addDailyData(self.s_dq_change_000016, self.tag + '.s_dq_change_000016')
        self.addDailyData(self.s_dq_pctchange_000016, self.tag + '.s_dq_pctchange_000016')
        self.addDailyData(self.s_dq_volume_000016, self.tag + '.s_dq_volume_000016')
        self.addDailyData(self.s_dq_amount_000016, self.tag + '.s_dq_amount_000016')

        self.addDailyData(self.s_dq_preclose_000300, self.tag + '.s_dq_preclose_000300')
        self.addDailyData(self.s_dq_open_000300, self.tag + '.s_dq_open_000300')
        self.addDailyData(self.s_dq_high_000300, self.tag + '.s_dq_high_000300')
        self.addDailyData(self.s_dq_low_000300, self.tag + '.s_dq_low_000300')
        self.addDailyData(self.s_dq_close_000300, self.tag + '.s_dq_close_000300')
        self.addDailyData(self.s_dq_change_000300, self.tag + '.s_dq_change_000300')
        self.addDailyData(self.s_dq_pctchange_000300, self.tag + '.s_dq_pctchange_000300')
        self.addDailyData(self.s_dq_volume_000300, self.tag + '.s_dq_volume_000300')
        self.addDailyData(self.s_dq_amount_000300, self.tag + '.s_dq_amount_000300')

        self.addDailyData(self.s_dq_preclose_000905, self.tag + '.s_dq_preclose_000905')
        self.addDailyData(self.s_dq_open_000905, self.tag + '.s_dq_open_000905')
        self.addDailyData(self.s_dq_high_000905, self.tag + '.s_dq_high_000905')
        self.addDailyData(self.s_dq_low_000905, self.tag + '.s_dq_low_000905')
        self.addDailyData(self.s_dq_close_000905, self.tag + '.s_dq_close_000905')
        self.addDailyData(self.s_dq_change_000905, self.tag + '.s_dq_change_000905')
        self.addDailyData(self.s_dq_pctchange_000905, self.tag + '.s_dq_pctchange_000905')
        self.addDailyData(self.s_dq_volume_000905, self.tag + '.s_dq_volume_000905')
        self.addDailyData(self.s_dq_amount_000905, self.tag + '.s_dq_amount_000905')

        self.addDailyData(self.s_dq_preclose_000906, self.tag + '.s_dq_preclose_000906')
        self.addDailyData(self.s_dq_open_000906, self.tag + '.s_dq_open_000906')
        self.addDailyData(self.s_dq_high_000906, self.tag + '.s_dq_high_000906')
        self.addDailyData(self.s_dq_low_000906, self.tag + '.s_dq_low_000906')
        self.addDailyData(self.s_dq_close_000906, self.tag + '.s_dq_close_000906')
        self.addDailyData(self.s_dq_change_000906, self.tag + '.s_dq_change_000906')
        self.addDailyData(self.s_dq_pctchange_000906, self.tag + '.s_dq_pctchange_000906')
        self.addDailyData(self.s_dq_volume_000906, self.tag + '.s_dq_volume_000906')
        self.addDailyData(self.s_dq_amount_000906, self.tag + '.s_dq_amount_000906')


        self.addDailyData(self.s_dq_preclose_000852, self.tag + '.s_dq_preclose_000852')
        self.addDailyData(self.s_dq_open_000852, self.tag + '.s_dq_open_000852')
        self.addDailyData(self.s_dq_high_000852, self.tag + '.s_dq_high_000852')
        self.addDailyData(self.s_dq_low_000852, self.tag + '.s_dq_low_000852')
        self.addDailyData(self.s_dq_close_000852, self.tag + '.s_dq_close_000852')
        self.addDailyData(self.s_dq_change_000852, self.tag + '.s_dq_change_000852')
        self.addDailyData(self.s_dq_pctchange_000852, self.tag + '.s_dq_pctchange_000852')
        self.addDailyData(self.s_dq_volume_000852, self.tag + '.s_dq_volume_000852')
        self.addDailyData(self.s_dq_amount_000852, self.tag + '.s_dq_amount_000852')
        
        self.addDailyData(self.s_dq_preclose_399001, self.tag + '.s_dq_preclose_399001')
        self.addDailyData(self.s_dq_open_399001, self.tag + '.s_dq_open_399001')
        self.addDailyData(self.s_dq_high_399001, self.tag + '.s_dq_high_399001')
        self.addDailyData(self.s_dq_low_399001, self.tag + '.s_dq_low_399001')
        self.addDailyData(self.s_dq_close_399001, self.tag + '.s_dq_close_399001')
        self.addDailyData(self.s_dq_change_399001, self.tag + '.s_dq_change_399001')
        self.addDailyData(self.s_dq_pctchange_399001, self.tag + '.s_dq_pctchange_399001')
        self.addDailyData(self.s_dq_volume_399001, self.tag + '.s_dq_volume_399001')
        self.addDailyData(self.s_dq_amount_399001, self.tag + '.s_dq_amount_399001')
        
        self.addDailyData(self.s_dq_preclose_399005, self.tag + '.s_dq_preclose_399005')
        self.addDailyData(self.s_dq_open_399005, self.tag + '.s_dq_open_399005')
        self.addDailyData(self.s_dq_high_399005, self.tag + '.s_dq_high_399005')
        self.addDailyData(self.s_dq_low_399005, self.tag + '.s_dq_low_399005')
        self.addDailyData(self.s_dq_close_399005, self.tag + '.s_dq_close_399005')
        self.addDailyData(self.s_dq_change_399005, self.tag + '.s_dq_change_399005')
        self.addDailyData(self.s_dq_pctchange_399005, self.tag + '.s_dq_pctchange_399005')
        self.addDailyData(self.s_dq_volume_399005, self.tag + '.s_dq_volume_399005')
        self.addDailyData(self.s_dq_amount_399005, self.tag + '.s_dq_amount_399005')
        
        self.addDailyData(self.s_dq_preclose_399006, self.tag + '.s_dq_preclose_399006')
        self.addDailyData(self.s_dq_open_399006, self.tag + '.s_dq_open_399006')
        self.addDailyData(self.s_dq_high_399006, self.tag + '.s_dq_high_399006')
        self.addDailyData(self.s_dq_low_399006, self.tag + '.s_dq_low_399006')
        self.addDailyData(self.s_dq_close_399006, self.tag + '.s_dq_close_399006')
        self.addDailyData(self.s_dq_change_399006, self.tag + '.s_dq_change_399006')
        self.addDailyData(self.s_dq_pctchange_399006, self.tag + '.s_dq_pctchange_399006')
        self.addDailyData(self.s_dq_volume_399006, self.tag + '.s_dq_volume_399006')
        self.addDailyData(self.s_dq_amount_399006, self.tag + '.s_dq_amount_399006')

        self.addDailyData(self.s_dq_preclose_000001, self.tag + '.s_dq_preclose_000001')
        self.addDailyData(self.s_dq_open_000001, self.tag + '.s_dq_open_000001')
        self.addDailyData(self.s_dq_high_000001, self.tag + '.s_dq_high_000001')
        self.addDailyData(self.s_dq_low_000001, self.tag + '.s_dq_low_000001')
        self.addDailyData(self.s_dq_close_000001, self.tag + '.s_dq_close_000001')
        self.addDailyData(self.s_dq_change_000001, self.tag + '.s_dq_change_000001')
        self.addDailyData(self.s_dq_pctchange_000001, self.tag + '.s_dq_pctchange_000001')
        self.addDailyData(self.s_dq_volume_000001, self.tag + '.s_dq_volume_000001')
        self.addDailyData(self.s_dq_amount_000001, self.tag + '.s_dq_amount_000001')
        return

    def loadDay(self, di):
        self.fillnan(di)  # set default value
        #if di == len(uv.Dates) - 1:
        #    return
        #if di > 1 and self.backfill:  # backfill
        #    self.doBackfill(di)
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

            #ii = uv.Instruments.lookup(ticker)
            #if ii < 0:
            #    continue
            #var_name = f's_dq_preclose_{ticker}'
            getattr(self, f's_dq_preclose_{ticker}')[di] = float(linespt[2])
            getattr(self, f's_dq_open_{ticker}')[di]  = float(linespt[3])
            getattr(self, f's_dq_high_{ticker}')[di]  = float(linespt[4])
            getattr(self, f's_dq_low_{ticker}')[di]  = float(linespt[5])
            getattr(self, f's_dq_close_{ticker}')[di]  = float(linespt[6])
            getattr(self, f's_dq_change_{ticker}')[di]  = float(linespt[7])
            getattr(self, f's_dq_pctchange_{ticker}')[di]  = float(linespt[8])/100.0
            getattr(self, f's_dq_volume_{ticker}')[di]  = float(linespt[9])
            getattr(self, f's_dq_amount_{ticker}')[di]  = float(linespt[10])
            updated += 1
        infile.close()
        print('[ %s ] Updated %d stocks on day %d' %  (self.tag, updated, uv.Dates[di]))
        return

