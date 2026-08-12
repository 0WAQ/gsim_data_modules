from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import pandas as pd
from pathlib import Path

class DmgrWbai_AIFcst_financial_summary_fore_quarter(DataManagerMapped):
    def __init__(self):
        DataManagerMapped.__init__(self)


        self.IS01_q = NIO_CUBE()
        self.IS02_q = NIO_CUBE()
        self.IS36_q = NIO_CUBE()
        self.ID06_q = NIO_CUBE()
        self.IS42_q = NIO_CUBE()
        self.IS06_q = NIO_CUBE()
        self.IS35_q = NIO_CUBE()
        self.ID13_q = NIO_CUBE()
        self.ID15_q = NIO_CUBE()
        self.ID35_q = NIO_CUBE()
        self.ID36_q = NIO_CUBE()
        self.forecast_quarter = NIO_CUBE()
        self.noy = 3                # num of years
        self.noq = 4 * self.noy    # num of quaters
    
    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = Path(cfg.getAttributeString('dataPath'))
        

        self.addData(self.IS01_q, self.tag + ".IS01_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS02_q, self.tag + ".IS02_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS36_q, self.tag + ".IS36_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.ID06_q, self.tag + ".ID06_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS42_q, self.tag + ".IS42_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS06_q, self.tag + ".IS06_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS35_q, self.tag + ".IS35_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.ID13_q, self.tag + ".ID13_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.ID15_q, self.tag + ".ID15_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.ID35_q, self.tag + ".ID35_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.ID36_q, self.tag + ".ID36_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.forecast_quarter, self.tag + ".forecast_quarter", len(uv.Dates), len(uv.Instruments), self.noq)


    def loadDay(self, di):
        self.fillnan(di)
        date_str = str(uv.Dates[di])
        file = self.dataPath / date_str
        if not file.exists():
            print(f"financial_summary_fore_quarter {date_str} empty")
            return
        
        try:
            df = pd.read_csv(file, dtype={"TICKER": str})
            for ticker, subdf in df.groupby("TICKER"):
                ii = uv.Instruments.lookup(ticker)
                if ii < 0:
                    continue

                subdf = subdf.sort_values("END_DATE")
                for yi, (_, row) in enumerate(subdf.iterrows()):
                    if yi >= self.noq:
                        break
                    end_date = row["END_DATE"]

                    self.IS01_q[di, yi, ii] = row["IS01_q"]
                    self.IS02_q[di, yi, ii] = row["IS02_q"]
                    self.IS36_q[di, yi, ii] = row["IS36_q"]
                    self.ID06_q[di, yi, ii] = row["ID06_q"]
                    self.IS42_q[di, yi, ii] = row["IS42_q"]
                    self.IS06_q[di, yi, ii] = row["IS06_q"]
                    self.IS35_q[di, yi, ii] = row["IS35_q"]
                    self.ID13_q[di, yi, ii] = row["ID13_q"]
                    self.ID15_q[di, yi, ii] = row["ID15_q"]
                    self.ID35_q[di, yi, ii] = row["ID35_q"]
                    self.ID36_q[di, yi, ii] = row["ID36_q"]
                    self.forecast_quarter[di, yi, ii] = int(end_date[0:4] + end_date[5:7] + end_date[8:])
            
            print(f"financial_summary_fore_quarter finished on [{date_str}]")
        
        except Exception:
            print(f"Error: {di}-{uv.Dates[di]} {yi} {ii}-{uv.Instruments[ii]}")
