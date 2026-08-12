from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import Universe as uv
import numpy as np, pandas as pd
import os, sys
from datetime import datetime
from gsim.data import DataRegistry as dr

'''
load interval data

Note: 
1) Instruments.lookup() is slow, reduce usage.
2) [di][ti][ii] much slower than [di,ti,ii]
'''


class DmgrGfl5m(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.open = NIO_CUBE()
        self.close = NIO_CUBE()
        self.high = NIO_CUBE()
        self.low = NIO_CUBE()
        self.vol = NIO_CUBE()
        self.amo = NIO_CUBE()
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.addData(self.open, self.tag + '.open', len(uv.Dates), len(uv.Instruments), uv.INTRADAY_STEPS_5M)
        self.addData(self.high, self.tag + '.high', len(uv.Dates), len(uv.Instruments), uv.INTRADAY_STEPS_5M)
        self.addData(self.low, self.tag + '.low', len(uv.Dates), len(uv.Instruments), uv.INTRADAY_STEPS_5M)
        self.addData(self.close, self.tag + '.close', len(uv.Dates), len(uv.Instruments), uv.INTRADAY_STEPS_5M)
        self.addData(self.vol, self.tag + '.vol', len(uv.Dates), len(uv.Instruments), uv.INTRADAY_STEPS_5M)
        self.addData(self.amo, self.tag + '.amo', len(uv.Dates), len(uv.Instruments), uv.INTRADAY_STEPS_5M)

    def registration(self, ):
        dr.registerData(self.mid, self.open, self.tag + '.open')
        dr.registerData(self.mid, self.high, self.tag + '.high')
        dr.registerData(self.mid, self.low, self.tag + '.low')
        dr.registerData(self.mid, self.close, self.tag + '.close')
        dr.registerData(self.mid, self.vol, self.tag + '.vol')
        dr.registerData(self.mid, self.amo, self.tag + '.amo')
        return

    def loadDay(self, di):
        self.fillnan(di)  # set default value
        filepath = os.path.join(self.dataPath, '%d' % uv.Dates[di]+".csv")
        print ("filepath:",filepath)
        if not os.path.isfile(filepath):
            print('[ %s ] missing file on day %d' % (self.tag, uv.Dates[di]))
            return
        infile = open(filepath, 'r')
        header = infile.readline().strip().split(',')  # skip title line
        #print ("header...", header)
        dayStr = str(uv.Dates[di])[0:4]+'-'+str(uv.Dates[di])[4:6]+'-'+str(uv.Dates[di])[6:8]
        print ("dayStr",dayStr)
        morning = pd.date_range(start=f'{dayStr} 9:30:00', end=f'{dayStr} 11:30:00', freq='5min')
        afternoon = pd.date_range(start=f'{dayStr} 13:05:00', end=f'{dayStr} 15:00:00', freq='5min')
        timeIdx = {j.strftime('%H:%M'):i for i, j in enumerate(morning.append(afternoon))}
        count = np.zeros(len(uv.Instruments))  ############
        #print ("uv.Instruments:",uv.Instruments[0])
        for line in infile:
            linespt = line.strip('\n').split(',')
            raw_code  = linespt[header.index('stock_symbol')]
            code = raw_code[2:]#+'.'+raw_code[0:2]
            ii = uv.Instruments.lookup(code)
            #print (code, "ii=",ii)
            if ii < 0:
                continue
            #count[ii] += 1  ##############
            # ti = np.searchsorted(timePoints, datetime.strptime(f"{uv.Dates[di]} {linespt[header.index('time')]}", '%Y%m%d %H:%M:%S.%f0'), side='right') - 1
            timeStr = linespt[header.index('window_end')][11:16]
            #print ("timeStr:",timeStr)
            #print ("timeIdx:",timeIdx)
            if timeStr not in timeIdx:
                continue
            ti = timeIdx[timeStr]
            count[ii] += 1  ##############
            #print ("ti=",ti)
            openStr = linespt[header.index('open')]
            highStr = linespt[header.index('high')]
            lowStr = linespt[header.index('low')]
            closeStr = linespt[header.index('close')]
            volStr = linespt[header.index('volume')]
            amoStr = linespt[header.index('trade_total_money')]
            self.open[di, ti, ii] = float(openStr) if openStr != '' else np.nan
            self.high[di, ti, ii] = float(highStr) if highStr != '' else np.nan
            self.low[di, ti, ii] = float(lowStr) if lowStr != '' else np.nan
            self.close[di, ti, ii] = float(closeStr) if closeStr != '' else np.nan
            self.vol[di, ti, ii] = float(volStr) if volStr != '' else np.nan
            self.amo[di, ti, ii] = float(amoStr) if amoStr != '' else np.nan
            #print (di,ti,ii,self.open[di, ti, ii],self.close[di, ti, ii],self.vol[di, ti, ii],self.amo[di, ti, ii])
        infile.close()
        print ("=====count:",count)
        if np.sum(count > 49) > 0:  ###################
            print('**** warning ****: ticker overlap')
            print(uv.Instruments[count > 49])
        print('[ %s ] Updated %d stocks on day %d' % (self.tag, np.sum(count)/49, uv.Dates[di]))

