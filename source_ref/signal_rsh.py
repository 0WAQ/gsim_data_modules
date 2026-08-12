from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import pandas as pd
from pathlib import Path

class signal_rsh(DataManagerMapped):
    def __init__(self):
        DataManagerMapped.__init__(self)

        self.value = NIO_MATRIX()

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = Path(cfg.getAttributeString('dataPath'))
        
        self.addData(self.value, self.tag + ".value", len(uv.Dates), len(uv.Instruments))


    def loadData(self, di_start):
        self.fillnan(di_start, len(uv.Dates))

        for di in range(di_start, len(uv.Dates)):
            if di % 10 == 0:
                print(f'[{self.tag}] Processing {uv.Dates[di]}')
            csv_path: Path = self.dataPath / str(uv.Dates[di])
            if not csv_path.exists():
                continue
            df = pd.read_csv(csv_path)
            for _, row in df.iterrows():
                ticker = row["stock_code"].split('.')[0]
                ii = uv.Instruments.lookup(ticker)
                self.value[di, ii] = row["value"]

        arr = self.value.data
        print(np.count_nonzero(np.isnan(arr)) / len(arr))
