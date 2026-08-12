from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import Universe as uv
import numpy as np
import os


class UmgrIndex(DataManagerMapped):
    def __init__(self, ):
        DataManagerMapped.__init__(self, )
        self.dataPath = None
        self.univ = NIO_MATRIX(NIO_BOOL)
        return

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = cfg.getAttributeString('dataPath')
        self.addDailyData(self.univ, self.tag)
        return

    def loadDay(self, di):
        print ("load ", di, "...")
        self.fillnan(di)  # default value
        filepath = os.path.join(self.dataPath, '%d' % uv.Dates[di])
        if not os.path.isfile(filepath):  # use yesterday's value
            if di == 0:
                return
            self.univ[di, :] = self.univ[di - 1, :]
            return
        infile = open(filepath, 'r')
        infile.readline()  # skip title line
        updated = 0
        for line in infile:
            linespt = line.strip('\n').split(',')
            ticker = linespt[2].split('.')[0]
            ii = uv.Instruments.lookup(ticker)
            if ii < 0:
                continue
            self.univ[di, ii] = True
            updated += 1
        infile.close()
        print('[ %s ] Activated %d sotcks on day %d' % (self.tag, updated, uv.Dates[di]))
        return

