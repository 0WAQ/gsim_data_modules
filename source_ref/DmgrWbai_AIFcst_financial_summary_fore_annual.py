from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import pandas as pd
from pathlib import Path

class DmgrWbai_AIFcst_financial_summary_fore_annual(DataManagerMapped):
    def __init__(self):
        DataManagerMapped.__init__(self)

        self.IS01 = NIO_CUBE()
        self.IS02 = NIO_CUBE()
        self.IS23 = NIO_CUBE()
        self.ID05 = NIO_CUBE()
        self.IS20 = NIO_CUBE()
        self.ID04 = NIO_CUBE()
        self.IS36 = NIO_CUBE()
        self.ID06 = NIO_CUBE()
        self.IS42 = NIO_CUBE()
        self.ID31 = NIO_CUBE()
        self.ID32 = NIO_CUBE()
        self.IS06 = NIO_CUBE()
        self.IS24 = NIO_CUBE()
        self.IS21 = NIO_CUBE()
        self.IS35 = NIO_CUBE()
        self.ID13 = NIO_CUBE()
        self.ID15 = NIO_CUBE()
        self.ID35 = NIO_CUBE()
        self.ID36 = NIO_CUBE()
        self.ID38 = NIO_CUBE()
        self.ID42 = NIO_CUBE()
        self.forecast_year = NIO_CUBE()
        self.noy = 3                # num of years
        self.noq = 12 * self.noy    # num of quaters
    
    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = Path(cfg.getAttributeString('dataPath'))
        
        self.addData(self.IS01, self.tag + ".IS01", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS02, self.tag + ".IS02", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS23, self.tag + ".IS23", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID05, self.tag + ".ID05", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS20, self.tag + ".IS20", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID04, self.tag + ".ID04", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS36, self.tag + ".IS36", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID06, self.tag + ".ID06", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS42, self.tag + ".IS42", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID31, self.tag + ".ID31", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID32, self.tag + ".ID32", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS06, self.tag + ".IS06", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS24, self.tag + ".IS24", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS21, self.tag + ".IS21", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS35, self.tag + ".IS35", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID13, self.tag + ".ID13", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID15, self.tag + ".ID15", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID35, self.tag + ".ID35", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID36, self.tag + ".ID36", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID38, self.tag + ".ID38", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID42, self.tag + ".ID42", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.forecast_year, self.tag + ".forecast_year", len(uv.Dates), len(uv.Instruments), self.noy)


    def loadDay(self, di):
        self.fillnan(di)
        date_str = str(uv.Dates[di])
        file = self.dataPath / date_str
        if not file.exists():
            print(f"financial_summary_fore_annual {date_str} empty")
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

                    self.IS01[di, yi, ii] = row["IS01"]
                    self.IS02[di, yi, ii] = row["IS02"]
                    self.IS23[di, yi, ii] = row["IS23"]
                    self.ID05[di, yi, ii] = row["ID05"]
                    self.IS20[di, yi, ii] = row["IS20"]
                    self.ID04[di, yi, ii] = row["ID04"]
                    self.IS36[di, yi, ii] = row["IS36"]
                    self.ID06[di, yi, ii] = row["ID06"]
                    self.IS42[di, yi, ii] = row["IS42"]
                    self.ID31[di, yi, ii] = row["ID31"]
                    self.ID32[di, yi, ii] = row["ID32"]
                    self.IS06[di, yi, ii] = row["IS06"]
                    self.IS24[di, yi, ii] = row["IS24"]
                    self.IS21[di, yi, ii] = row["IS21"]
                    self.IS35[di, yi, ii] = row["IS35"]
                    self.ID13[di, yi, ii] = row["ID13"]
                    self.ID15[di, yi, ii] = row["ID15"]
                    self.ID35[di, yi, ii] = row["ID35"]
                    self.ID36[di, yi, ii] = row["ID36"]
                    self.ID38[di, yi, ii] = row["ID38"]
                    self.ID42[di, yi, ii] = row["ID42"]
                    self.forecast_year[di, yi, ii] = int(end_date[0:4] + end_date[5:7] + end_date[8:])
            
            print(f"financial_summary_fore_annual finished on [{date_str}]")
        
        except Exception:
            print(f"Error: {di}-{uv.Dates[di]} {yi} {ii}-{uv.Instruments[ii]}")
