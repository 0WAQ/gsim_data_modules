from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import pandas as pd
from pathlib import Path

class DmgrWbai_AIFcst_income_statement_fore_annual(DataManagerMapped):
    def __init__(self):
        DataManagerMapped.__init__(self)

        self.IS01 = NIO_CUBE()
        self.IS02 = NIO_CUBE()
        self.IS03 = NIO_CUBE()
        self.IS04 = NIO_CUBE()
        self.IS05 = NIO_CUBE()
        self.IS06 = NIO_CUBE()
        self.IS07 = NIO_CUBE()
        self.IS08 = NIO_CUBE()
        self.IS09 = NIO_CUBE()
        self.IS11 = NIO_CUBE()
        self.IS12 = NIO_CUBE()
        self.IS13 = NIO_CUBE()
        self.IS14 = NIO_CUBE()
        self.IS15 = NIO_CUBE()
        self.IS16 = NIO_CUBE()
        self.IS17 = NIO_CUBE()
        self.IS18 = NIO_CUBE()
        self.IS19 = NIO_CUBE()
        self.IS20 = NIO_CUBE()
        self.IS21 = NIO_CUBE()
        self.IS22 = NIO_CUBE()
        self.IS23 = NIO_CUBE()
        self.IS24 = NIO_CUBE()
        self.IS25 = NIO_CUBE()
        self.IS26 = NIO_CUBE()
        self.IS27 = NIO_CUBE()
        self.IS28 = NIO_CUBE()
        self.IS29 = NIO_CUBE()
        self.IS30 = NIO_CUBE()
        self.IS31 = NIO_CUBE()
        self.IS32 = NIO_CUBE()
        self.IS33 = NIO_CUBE()
        self.IS34 = NIO_CUBE()
        self.IS35 = NIO_CUBE()
        self.IS36 = NIO_CUBE()
        self.IS37 = NIO_CUBE()
        self.IS38 = NIO_CUBE()
        self.IS39 = NIO_CUBE()
        self.IS40 = NIO_CUBE()
        self.IS41 = NIO_CUBE()
        self.IS42 = NIO_CUBE()
        self.forecast_year = NIO_CUBE()
        self.noy = 3                # num of years
        self.noq = 12 * self.noy    # num of quaters
    
    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = Path(cfg.getAttributeString('dataPath'))
        
        self.addData(self.IS01, self.tag + ".IS01", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS02, self.tag + ".IS02", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS03, self.tag + ".IS03", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS04, self.tag + ".IS04", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS05, self.tag + ".IS05", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS06, self.tag + ".IS06", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS07, self.tag + ".IS07", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS08, self.tag + ".IS08", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS09, self.tag + ".IS09", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS11, self.tag + ".IS11", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS12, self.tag + ".IS12", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS13, self.tag + ".IS13", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS14, self.tag + ".IS14", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS15, self.tag + ".IS15", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS16, self.tag + ".IS16", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS17, self.tag + ".IS17", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS18, self.tag + ".IS18", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS19, self.tag + ".IS19", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS20, self.tag + ".IS20", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS21, self.tag + ".IS21", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS22, self.tag + ".IS22", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS23, self.tag + ".IS23", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS24, self.tag + ".IS24", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS25, self.tag + ".IS25", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS26, self.tag + ".IS26", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS27, self.tag + ".IS27", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS28, self.tag + ".IS28", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS29, self.tag + ".IS29", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS30, self.tag + ".IS30", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS31, self.tag + ".IS31", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS32, self.tag + ".IS32", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS33, self.tag + ".IS33", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS34, self.tag + ".IS34", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS35, self.tag + ".IS35", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS36, self.tag + ".IS36", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS37, self.tag + ".IS37", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS38, self.tag + ".IS38", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS39, self.tag + ".IS39", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS40, self.tag + ".IS40", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS41, self.tag + ".IS41", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.IS42, self.tag + ".IS42", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.forecast_year, self.tag + ".forecast_year", len(uv.Dates), len(uv.Instruments), self.noy)


    def loadDay(self, di):
        self.fillnan(di)
        date_str = str(uv.Dates[di])
        file = self.dataPath / date_str
        if not file.exists():
            print(f"income_statement_fore_annual {date_str} empty")
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
                    self.IS03[di, yi, ii] = row["IS03"]
                    self.IS04[di, yi, ii] = row["IS04"]
                    self.IS05[di, yi, ii] = row["IS05"]
                    self.IS06[di, yi, ii] = row["IS06"]
                    self.IS07[di, yi, ii] = row["IS07"]
                    self.IS08[di, yi, ii] = row["IS08"]
                    self.IS09[di, yi, ii] = row["IS09"]
                    self.IS11[di, yi, ii] = row["IS11"]
                    self.IS12[di, yi, ii] = row["IS12"]
                    self.IS13[di, yi, ii] = row["IS13"]
                    self.IS14[di, yi, ii] = row["IS14"]
                    self.IS15[di, yi, ii] = row["IS15"]
                    self.IS16[di, yi, ii] = row["IS16"]
                    self.IS17[di, yi, ii] = row["IS17"]
                    self.IS18[di, yi, ii] = row["IS18"]
                    self.IS19[di, yi, ii] = row["IS19"]
                    self.IS20[di, yi, ii] = row["IS20"]
                    self.IS21[di, yi, ii] = row["IS21"]
                    self.IS22[di, yi, ii] = row["IS22"]
                    self.IS23[di, yi, ii] = row["IS23"]
                    self.IS24[di, yi, ii] = row["IS24"]
                    self.IS25[di, yi, ii] = row["IS25"]
                    self.IS26[di, yi, ii] = row["IS26"]
                    self.IS27[di, yi, ii] = row["IS27"]
                    self.IS28[di, yi, ii] = row["IS28"]
                    self.IS29[di, yi, ii] = row["IS29"]
                    self.IS30[di, yi, ii] = row["IS30"]
                    self.IS31[di, yi, ii] = row["IS31"]
                    self.IS32[di, yi, ii] = row["IS32"]
                    self.IS33[di, yi, ii] = row["IS33"]
                    self.IS34[di, yi, ii] = row["IS34"]
                    self.IS35[di, yi, ii] = row["IS35"]
                    self.IS36[di, yi, ii] = row["IS36"]
                    self.IS37[di, yi, ii] = row["IS37"]
                    self.IS38[di, yi, ii] = row["IS38"]
                    self.IS39[di, yi, ii] = row["IS39"]
                    self.IS40[di, yi, ii] = row["IS40"]
                    self.IS41[di, yi, ii] = row["IS41"]
                    self.IS42[di, yi, ii] = row["IS42"]
                    self.forecast_year[di, yi, ii] = int(end_date[0:4] + end_date[5:7] + end_date[8:])
            
            print(f"income_statement_fore_annual finished on [{date_str}]")
        
        except Exception:
            print(f"Error: {di}-{uv.Dates[di]} {yi} {ii}-{uv.Instruments[ii]}")
