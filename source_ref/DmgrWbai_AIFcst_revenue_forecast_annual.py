from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import pandas as pd
from pathlib import Path

class DmgrWbai_AIFcst_revenue_forecast_annual(DataManagerMapped):
    def __init__(self):
        DataManagerMapped.__init__(self)

        self.revenue = NIO_CUBE()
        self.forecast_year = NIO_CUBE()
        self.noy = 3                # num of years
        self.noq = 12 * self.noy    # num of quaters
    
    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = Path(cfg.getAttributeString('dataPath'))
        
        self.addData(self.revenue, self.tag + ".revenue", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.forecast_year, self.tag + ".forecast_year", len(uv.Dates), len(uv.Instruments), self.noy)


    def loadDay(self, di):
        self.fillnan(di)
        date_str = str(uv.Dates[di])
        file = self.dataPath / date_str
        if not file.exists():
            print(f"revenue_forecast_annual {date_str} empty")
            return
        
        try:
            df = pd.read_csv(file, dtype={"TICKER": str, "REVENUE": np.float64})
            for ticker, subdf in df.groupby("TICKER"):
                ii = uv.Instruments.lookup(ticker)
                if ii < 0:
                    continue

                subdf = subdf.sort_values("END_DATE")
                for yi, (_, row) in enumerate(subdf.iterrows()):
                    if yi >= self.noy:
                        break
                    revenue = row["REVENUE"]
                    end_date = row["END_DATE"]

                    self.revenue[di, yi, ii] = revenue
                    self.forecast_year[di, yi, ii] = int(end_date[0:4] + end_date[5:7] + end_date[8:])
            
            print(f"revenue_forecast_annual finished on [{date_str}]")
        
        except Exception:
            print(f"Error: {di}-{uv.Dates[di]} {yi} {ii}-{uv.Instruments[ii]}")
