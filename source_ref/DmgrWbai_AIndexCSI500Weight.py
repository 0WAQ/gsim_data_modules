from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
import numpy as np
import pandas as pd
from pathlib import Path

class DmgrWbai_AIndexCSI500Weight(DataManagerMapped):
    def __init__(self):
        DataManagerMapped.__init__(self)
        self.weight = NIO_MATRIX()

        self.rawdata_dir = None # Path("/production/bak/datasvc/rawdata_wind/AIndexCSI500Weight/")

    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.rawdata_dir = Path(cfg.getAttributeStringDefault('dataPath', '/production/bak/datasvc/rawdata_wind/AIndexCSI500Weight/'))
        self.addDailyData(self.weight, "AIndexCSI500Weight.weight")

    def loadData(self, di_start):
        self.fillnan(di_start, len(uv.Dates))

        target_cols = ["WEIGHT", "S_CON_WINDCODE"]
        for di in range(di_start, len(uv.Dates)):
            if di % 10 == 0:
                print(f'[{self.tag}] Processing {uv.Dates[di]}')
            csv_path: Path = self.rawdata_dir / str(uv.Dates[di])
            if not csv_path.exists():
                continue
            df = pd.read_csv(csv_path, usecols=lambda x: x.upper() in target_cols)
            df.columns = df.columns.str.upper()
            for _, row in df.iterrows():
                ticker = row["S_CON_WINDCODE"].split('.')[0]
                ii = uv.Instruments.lookup(ticker)
                self.weight[di, ii] = row["WEIGHT"]
 
        arr = self.weight.data
        print(np.count_nonzero(np.isnan(arr)) / len(arr))
