from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import Universe as uv
import numpy as np
import os
#code,open,high,low,close,volume,amount,status

class DmgrBasedata(DataManagerMapped):
    """基础数据

    Parameters
    ------------
    open:
    high:
    low:
    close:
    volume:
    amount:
    tradecnt:
    cap:
    negcap:
    vwap:
    status:
    st:
    country:
    exchange:
    sector:
    industry:
    subindustry:
    """

    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.rawpricePath = None
        self.industryPath = None
        self.stPath = None
        self.openp = NIO_MATRIX()
        self.high = NIO_MATRIX()
        self.low = NIO_MATRIX()
        self.close = NIO_MATRIX()
        self.volume = NIO_MATRIX()
        self.amount = NIO_MATRIX()
        self.tradecnt = NIO_MATRIX()
        self.cap = NIO_MATRIX()
        self.capfree = NIO_MATRIX()
        self.vwap = NIO_MATRIX()
        self.status = NIO_MATRIX(NIO_INT)
        self.st = NIO_MATRIX(NIO_BOOL)

        self.country = NIO_MATRIX(NIO_INT)
        self.exchange = NIO_MATRIX(NIO_INT)
        self.sector = NIO_MATRIX(NIO_INT)
        self.subsector = NIO_MATRIX(NIO_INT)
        self.industry = NIO_MATRIX(NIO_INT)
        self.subindustry = NIO_MATRIX(NIO_INT)

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.rawpricePath = cfg.getAttributeString('rawpricePath')
        self.industryPath = cfg.getAttributeString('industryPath')
        self.stPath = cfg.getAttributeString('ST')
        #
        self.addDailyData(self.openp, 'open')
        self.addDailyData(self.high, 'high')
        self.addDailyData(self.low, 'low')
        self.addDailyData(self.close, 'close')
        self.addDailyData(self.volume, 'volume')
        self.addDailyData(self.amount, 'amount')
        self.addDailyData(self.tradecnt, 'tradecnt')
        self.addDailyData(self.cap, 'cap')
        self.addDailyData(self.capfree, 'capfree')
        self.addDailyData(self.vwap, 'vwap')
        self.addDailyData(self.status, 'status')
        self.addDailyData(self.st, 'st')

        self.addDailyData(self.country, 'country')
        self.addDailyData(self.exchange, 'exchange')
        self.addDailyData(self.sector, 'sector')
        self.addDailyData(self.subsector, 'subsector')
        self.addDailyData(self.industry, 'industry')
        self.addDailyData(self.subindustry, 'subindustry')

    def loadDay(self, di):
        # daily quote
        self.fillnan(di)  # set default value
        self.status[di] = 0
        if di > 0:  # for non-trading days
            self.close[di] = self.close[di - 1]
            self.volume[di] = 0
        filepath = os.path.join(self.rawpricePath, '%d' % uv.Dates[di])
        if not os.path.isfile(filepath):
            print('[ %s ] %s missing on day %d' % (self.tag, filepath, uv.Dates[di]))
            return
        infile = open(filepath, 'r')
        #print ("Open..",filepath)#<<std::endl;
        infile.readline()  # skip title line
        updated = 0
        #code,name,trade_date,open,high,low,close,volume,amount,trades,cap,negcap,status
        for line in infile:
	    #std::cout<<"line:"<<line<<std::endl;	
            #print ("line:",line)
            linespt = line.strip('\n').split(',')
            # a field could be blank if its value is missing
            linespt = [np.nan if x == '' else x for x in linespt]
            ticker = linespt[0].split('.')[0]
            ii = uv.Instruments.lookup(ticker)
            if ii < 0:
                continue
            self.openp[di, ii] = float(linespt[3])
            self.high[di, ii] = float(linespt[4])
            self.low[di, ii] = float(linespt[5])
            self.close[di, ii] = float(linespt[6])
            self.volume[di, ii] = float(linespt[7])
            self.amount[di, ii] = float(linespt[8])
            self.tradecnt[di, ii] = float(linespt[9])
            self.cap[di, ii] = float(linespt[10])
            self.capfree[di, ii] = float(linespt[11])
            self.vwap[di, ii] = self.amount[di, ii] / self.volume[di, ii] if self.volume[di, ii] > 0 else np.nan
            self.status[di, ii] = int(linespt[12])
            updated += 1
        infile.close()
        print('[%s] Cached %d stocks on day %d' % (self.tag, updated, uv.Dates[di]))

        # st
        filepath = os.path.join(self.stPath, '%d' % uv.Dates[di])
        if not os.path.isfile(filepath) and di == len(uv.Dates) - 1:
            print('Warning--[%s.st] %s missing on day %d' % (self.tag, filepath, uv.Dates[di]))
            return
        infile = open(filepath, 'r')
        infile.readline()  # skip title line
        _lines =0
        _cnt =0
        _cnt_T =0
        _cnt_R =0
        for line in infile:
            _lines += 1
            linespt = line.strip('\n').split(',')
            ticker = linespt[0].split('.')[0]
            type_st = linespt[2]
            ii = uv.Instruments.lookup(ticker)
            if ii < 0:
                print ("Warning: ii<0",ii,ticker)
                continue
            if type_st=='R':
                _cnt_R += 1
                #print ("[Info YSim] type_st=","R")
                continue
            self.st[di, ii] = True
            _cnt += 1
            if type_st=='T':
                _cnt_T += 1
        infile.close()
        print (di, uv.Dates[di], "# of lines:", _lines)
        print (di, uv.Dates[di], "# of st:", _cnt)
        print (di, uv.Dates[di], "# of T:", _cnt_T)
        print (di, uv.Dates[di], "# of R:", _cnt_R)

        # industry
        #S_INFO_WINDCODE,WIND_IND_CODE,ENTRY_DT,REMOVE_DT
        self.country[di] = 1
        self.industry[di] = 0
        filepath = os.path.join(self.industryPath, '%d' % uv.Dates[di])
        if not os.path.isfile(filepath):
            print('Warning--[%s] %s missing on day %d' % (self.tag, filepath, uv.Dates[di]))
            return
        infile = open(filepath, 'r')
        infile.readline()  # skip title line
        for line in infile:
            linespt = line.strip('\n').split(',')
            linespt = [-1 if x == '' else x for x in linespt]
            ticker = linespt[0].split('.')[0]
            ii = uv.Instruments.lookup(ticker)
            if ii < 0:
                continue

            if ticker[0] == '6':
                self.exchange[di, ii] = 0
            elif ticker[0] == '0' or ticker[0] == '3':
                self.exchange[di, ii] = 1
            elif ticker[0] == '9':
                self.exchange[di, ii] = 2
            else:
                self.exchange[di, ii] = 3
                print ("[YSim:Warning-Exchange] Ticker", ticker)

            #self.exchange[di, ii] = 0 if ticker[0] == '6' else 1
            ind_code = str(linespt[1])
            self.sector[di, ii] = int(ind_code[-10:-6])
            self.subsector[di, ii] = int(ind_code[-10:-4])
            self.industry[di, ii] = int(ind_code[-10:-2])
            self.subindustry[di, ii] = int(ind_code[-10:])
        infile.close()
        return
