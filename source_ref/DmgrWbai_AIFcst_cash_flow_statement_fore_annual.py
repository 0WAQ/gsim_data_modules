from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import pandas as pd
from pathlib import Path

class DmgrWbai_AIFcst_cash_flow_statement_fore_annual(DataManagerMapped):
    def __init__(self):
        DataManagerMapped.__init__(self)

        self.CF01 = NIO_CUBE()
        self.CF02 = NIO_CUBE()
        self.CF03 = NIO_CUBE()
        self.CF04 = NIO_CUBE()
        self.CF05 = NIO_CUBE()
        self.CF06 = NIO_CUBE()
        self.CF07 = NIO_CUBE()
        self.CF08 = NIO_CUBE()
        self.CF09 = NIO_CUBE()
        self.CF10 = NIO_CUBE()
        self.CF11 = NIO_CUBE()
        self.CF12 = NIO_CUBE()
        self.CF13 = NIO_CUBE()
        self.CF14 = NIO_CUBE()
        self.CF15 = NIO_CUBE()
        self.CF16 = NIO_CUBE()
        self.CF17 = NIO_CUBE()
        self.CF18 = NIO_CUBE()
        self.CF19 = NIO_CUBE()
        self.CF20 = NIO_CUBE()
        self.CF21 = NIO_CUBE()
        self.CF22 = NIO_CUBE()
        self.forecast_year = NIO_CUBE()
        self.noy = 3                # num of years
        self.noq = 12 * self.noy    # num of quaters
    
    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = Path(cfg.getAttributeString('dataPath'))
        
        self.addData(self.CF01, self.tag + ".CF01", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.CF02, self.tag + ".CF02", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.CF03, self.tag + ".CF03", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.CF04, self.tag + ".CF04", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.CF05, self.tag + ".CF05", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.CF06, self.tag + ".CF06", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.CF07, self.tag + ".CF07", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.CF08, self.tag + ".CF08", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.CF09, self.tag + ".CF09", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.CF10, self.tag + ".CF10", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.CF11, self.tag + ".CF11", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.CF12, self.tag + ".CF12", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.CF13, self.tag + ".CF13", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.CF14, self.tag + ".CF14", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.CF15, self.tag + ".CF15", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.CF16, self.tag + ".CF16", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.CF17, self.tag + ".CF17", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.CF18, self.tag + ".CF18", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.CF19, self.tag + ".CF19", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.CF20, self.tag + ".CF20", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.CF21, self.tag + ".CF21", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.CF22, self.tag + ".CF22", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.forecast_year, self.tag + ".forecast_year", len(uv.Dates), len(uv.Instruments), self.noy)


    def loadDay(self, di):
        self.fillnan(di)
        date_str = str(uv.Dates[di])
        file = self.dataPath / date_str
        if not file.exists():
            print(f"cash_flow_statement_fore_annual {date_str} empty")
            return
        
        try:
            df = pd.read_csv(file, dtype={"TICKER": str})
            for ticker, subdf in df.groupby("TICKER"):
                ii = uv.Instruments.lookup(ticker)
                if ii < 0:
                    continue

                subdf = subdf.sort_values("END_DATE")
                for yi, (_, row) in enumerate(subdf.iterrows()):
                    if yi >= self.noy:
                        break
                    end_date = row["END_DATE"]

                    self.CF01[di, yi, ii] = row["CF01"]
                    self.CF02[di, yi, ii] = row["CF02"]
                    self.CF03[di, yi, ii] = row["CF03"]
                    self.CF04[di, yi, ii] = row["CF04"]
                    self.CF05[di, yi, ii] = row["CF05"]
                    self.CF06[di, yi, ii] = row["CF06"]
                    self.CF07[di, yi, ii] = row["CF07"]
                    self.CF08[di, yi, ii] = row["CF08"]
                    self.CF09[di, yi, ii] = row["CF09"]
                    self.CF10[di, yi, ii] = row["CF10"]
                    self.CF11[di, yi, ii] = row["CF11"]
                    self.CF12[di, yi, ii] = row["CF12"]
                    self.CF13[di, yi, ii] = row["CF13"]
                    self.CF14[di, yi, ii] = row["CF14"]
                    self.CF15[di, yi, ii] = row["CF15"]
                    self.CF16[di, yi, ii] = row["CF16"]
                    self.CF17[di, yi, ii] = row["CF17"]
                    self.CF18[di, yi, ii] = row["CF18"]
                    self.CF19[di, yi, ii] = row["CF19"]
                    self.CF20[di, yi, ii] = row["CF20"]
                    self.CF21[di, yi, ii] = row["CF21"]
                    self.CF22[di, yi, ii] = row["CF22"]
                    self.forecast_year[di, yi, ii] = int(end_date[0:4] + end_date[5:7] + end_date[8:])
            
            print(f"cash_flow_statement_fore_annual finished on [{date_str}]")
        
        except Exception:
            print(f"Error: {di}-{uv.Dates[di]} {yi} {ii}-{uv.Instruments[ii]}")
