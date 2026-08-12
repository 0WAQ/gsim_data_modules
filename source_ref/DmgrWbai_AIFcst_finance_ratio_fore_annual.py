from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import pandas as pd
from pathlib import Path

class DmgrWbai_AIFcst_finance_ratio_fore_annual(DataManagerMapped):
    def __init__(self):
        DataManagerMapped.__init__(self)

        self.ID01 = NIO_CUBE()
        self.ID02 = NIO_CUBE()
        self.ID03 = NIO_CUBE()
        self.ID04 = NIO_CUBE()
        self.ID05 = NIO_CUBE()
        self.ID06 = NIO_CUBE()
        self.ID08 = NIO_CUBE()
        self.ID09 = NIO_CUBE()
        self.ID10 = NIO_CUBE()
        self.ID11 = NIO_CUBE()
        self.ID12 = NIO_CUBE()
        self.ID13 = NIO_CUBE()
        self.ID14 = NIO_CUBE()
        self.ID15 = NIO_CUBE()
        self.ID17 = NIO_CUBE()
        self.ID18 = NIO_CUBE()
        self.ID19 = NIO_CUBE()
        self.ID20 = NIO_CUBE()
        self.ID21 = NIO_CUBE()
        self.ID23 = NIO_CUBE()
        self.ID24 = NIO_CUBE()
        self.ID25 = NIO_CUBE()
        self.ID26 = NIO_CUBE()
        self.ID27 = NIO_CUBE()
        self.ID29 = NIO_CUBE()
        self.ID30 = NIO_CUBE()
        self.ID31 = NIO_CUBE()
        self.ID32 = NIO_CUBE()
        self.ID34 = NIO_CUBE()
        self.ID35 = NIO_CUBE()
        self.ID36 = NIO_CUBE()
        self.ID37 = NIO_CUBE()
        self.ID38 = NIO_CUBE()
        self.ID40 = NIO_CUBE()
        self.ID41 = NIO_CUBE()
        self.ID42 = NIO_CUBE()
        self.forecast_year = NIO_CUBE()
        self.noy = 3                # num of years
        self.noq = 12 * self.noy    # num of quaters
    
    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = Path(cfg.getAttributeString('dataPath'))
        
        self.addData(self.ID01, self.tag + ".ID01", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID02, self.tag + ".ID02", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID03, self.tag + ".ID03", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID04, self.tag + ".ID04", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID05, self.tag + ".ID05", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID06, self.tag + ".ID06", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID08, self.tag + ".ID08", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID09, self.tag + ".ID09", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID10, self.tag + ".ID10", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID11, self.tag + ".ID11", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID12, self.tag + ".ID12", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID13, self.tag + ".ID13", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID14, self.tag + ".ID14", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID15, self.tag + ".ID15", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID17, self.tag + ".ID17", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID18, self.tag + ".ID18", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID19, self.tag + ".ID19", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID20, self.tag + ".ID20", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID21, self.tag + ".ID21", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID23, self.tag + ".ID23", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID24, self.tag + ".ID24", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID25, self.tag + ".ID25", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID26, self.tag + ".ID26", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID27, self.tag + ".ID27", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID29, self.tag + ".ID29", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID30, self.tag + ".ID30", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID31, self.tag + ".ID31", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID32, self.tag + ".ID32", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID34, self.tag + ".ID34", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID35, self.tag + ".ID35", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID36, self.tag + ".ID36", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID37, self.tag + ".ID37", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID38, self.tag + ".ID38", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID40, self.tag + ".ID40", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID41, self.tag + ".ID41", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.ID42, self.tag + ".ID42", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.forecast_year, self.tag + ".forecast_year", len(uv.Dates), len(uv.Instruments), self.noy)


    def loadDay(self, di):
        self.fillnan(di)
        date_str = str(uv.Dates[di])
        file = self.dataPath / date_str
        if not file.exists():
            print(f"finance_ratio_fore_annual {date_str} empty")
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

                    self.ID01[di, yi, ii] = row["ID01"]
                    self.ID02[di, yi, ii] = row["ID02"]
                    self.ID03[di, yi, ii] = row["ID03"]
                    self.ID04[di, yi, ii] = row["ID04"]
                    self.ID05[di, yi, ii] = row["ID05"]
                    self.ID06[di, yi, ii] = row["ID06"]
                    self.ID08[di, yi, ii] = row["ID08"]
                    self.ID09[di, yi, ii] = row["ID09"]
                    self.ID10[di, yi, ii] = row["ID10"]
                    self.ID11[di, yi, ii] = row["ID11"]
                    self.ID12[di, yi, ii] = row["ID12"]
                    self.ID13[di, yi, ii] = row["ID13"]
                    self.ID14[di, yi, ii] = row["ID14"]
                    self.ID15[di, yi, ii] = row["ID15"]
                    self.ID17[di, yi, ii] = row["ID17"]
                    self.ID18[di, yi, ii] = row["ID18"]
                    self.ID19[di, yi, ii] = row["ID19"]
                    self.ID20[di, yi, ii] = row["ID20"]
                    self.ID21[di, yi, ii] = row["ID21"]
                    self.ID23[di, yi, ii] = row["ID23"]
                    self.ID24[di, yi, ii] = row["ID24"]
                    self.ID25[di, yi, ii] = row["ID25"]
                    self.ID26[di, yi, ii] = row["ID26"]
                    self.ID27[di, yi, ii] = row["ID27"]
                    self.ID29[di, yi, ii] = row["ID29"]
                    self.ID30[di, yi, ii] = row["ID30"]
                    self.ID31[di, yi, ii] = row["ID31"]
                    self.ID32[di, yi, ii] = row["ID32"]
                    self.ID34[di, yi, ii] = row["ID34"]
                    self.ID35[di, yi, ii] = row["ID35"]
                    self.ID36[di, yi, ii] = row["ID36"]
                    self.ID37[di, yi, ii] = row["ID37"]
                    self.ID38[di, yi, ii] = row["ID38"]
                    self.ID40[di, yi, ii] = row["ID40"]
                    self.ID41[di, yi, ii] = row["ID41"]
                    self.ID42[di, yi, ii] = row["ID42"]
                    self.forecast_year[di, yi, ii] = int(end_date[0:4] + end_date[5:7] + end_date[8:])
            
            print(f"finance_ratio_fore_annual finished on [{date_str}]")
        
        except Exception:
            print(f"Error: {di}-{uv.Dates[di]} {yi} {ii}-{uv.Instruments[ii]}")
