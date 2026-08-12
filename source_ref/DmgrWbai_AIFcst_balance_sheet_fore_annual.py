from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import pandas as pd
from pathlib import Path


class DmgrWbai_AIFcst_balance_sheet_fore_annual(DataManagerMapped):
    def __init__(self):
        DataManagerMapped.__init__(self)

        self.BS01 = NIO_CUBE()
        self.BS02 = NIO_CUBE()
        self.BS03 = NIO_CUBE()
        self.BS04 = NIO_CUBE()
        self.BS05 = NIO_CUBE()
        self.BS06 = NIO_CUBE()
        self.BS07 = NIO_CUBE()
        self.BS08 = NIO_CUBE()
        self.BS09 = NIO_CUBE()
        self.BS10 = NIO_CUBE()
        self.BS11 = NIO_CUBE()
        self.BS12 = NIO_CUBE()
        self.BS13 = NIO_CUBE()
        self.BS14 = NIO_CUBE()
        self.BS15 = NIO_CUBE()
        self.BS16 = NIO_CUBE()
        self.BS17 = NIO_CUBE()
        self.BS18 = NIO_CUBE()
        self.BS19 = NIO_CUBE()
        self.BS20 = NIO_CUBE()
        self.BS21 = NIO_CUBE()
        self.BS22 = NIO_CUBE()
        self.BS23 = NIO_CUBE()
        self.BS24 = NIO_CUBE()
        self.BS25 = NIO_CUBE()
        self.BS26 = NIO_CUBE()
        self.BS27 = NIO_CUBE()
        self.BS28 = NIO_CUBE()
        self.BS29 = NIO_CUBE()
        self.BS30 = NIO_CUBE()
        self.BS31 = NIO_CUBE()
        self.BS32 = NIO_CUBE()
        self.BS33 = NIO_CUBE()
        self.BS34 = NIO_CUBE()
        self.BS35 = NIO_CUBE()
        self.BS36 = NIO_CUBE()
        self.BS37 = NIO_CUBE()
        self.BS38 = NIO_CUBE()
        self.BS39 = NIO_CUBE()
        self.BS40 = NIO_CUBE()
        self.forecast_year = NIO_CUBE()
        self.noy = 3                # num of years
        self.noq = 12 * self.noy    # num of quaters
    
    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = Path(cfg.getAttributeString('dataPath'))
        
        self.addData(self.BS01, self.tag + ".BS01", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS02, self.tag + ".BS02", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS03, self.tag + ".BS03", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS04, self.tag + ".BS04", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS05, self.tag + ".BS05", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS06, self.tag + ".BS06", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS07, self.tag + ".BS07", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS08, self.tag + ".BS08", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS09, self.tag + ".BS09", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS10, self.tag + ".BS10", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS11, self.tag + ".BS11", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS12, self.tag + ".BS12", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS13, self.tag + ".BS13", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS14, self.tag + ".BS14", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS15, self.tag + ".BS15", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS16, self.tag + ".BS16", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS17, self.tag + ".BS17", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS18, self.tag + ".BS18", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS19, self.tag + ".BS19", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS20, self.tag + ".BS20", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS21, self.tag + ".BS21", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS22, self.tag + ".BS22", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS23, self.tag + ".BS23", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS24, self.tag + ".BS24", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS25, self.tag + ".BS25", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS26, self.tag + ".BS26", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS27, self.tag + ".BS27", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS28, self.tag + ".BS28", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS29, self.tag + ".BS29", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS30, self.tag + ".BS30", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS31, self.tag + ".BS31", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS32, self.tag + ".BS32", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS33, self.tag + ".BS33", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS34, self.tag + ".BS34", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS35, self.tag + ".BS35", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS36, self.tag + ".BS36", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS37, self.tag + ".BS37", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS38, self.tag + ".BS38", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS39, self.tag + ".BS39", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.BS40, self.tag + ".BS40", len(uv.Dates), len(uv.Instruments), self.noy)
        self.addData(self.forecast_year, self.tag + ".forecast_year", len(uv.Dates), len(uv.Instruments), self.noy)


    def loadDay(self, di):
        self.fillnan(di)
        date_str = str(uv.Dates[di])
        file = self.dataPath / date_str
        if not file.exists():
            print(f"balance_sheet_fore_annual {date_str} empty")
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

                    self.BS01[di, yi, ii] = row["BS01"]
                    self.BS02[di, yi, ii] = row["BS02"]
                    self.BS03[di, yi, ii] = row["BS03"]
                    self.BS04[di, yi, ii] = row["BS04"]
                    self.BS05[di, yi, ii] = row["BS05"]
                    self.BS06[di, yi, ii] = row["BS06"]
                    self.BS07[di, yi, ii] = row["BS07"]
                    self.BS08[di, yi, ii] = row["BS08"]
                    self.BS09[di, yi, ii] = row["BS09"]
                    self.BS10[di, yi, ii] = row["BS10"]
                    self.BS11[di, yi, ii] = row["BS11"]
                    self.BS12[di, yi, ii] = row["BS12"]
                    self.BS13[di, yi, ii] = row["BS13"]
                    self.BS14[di, yi, ii] = row["BS14"]
                    self.BS15[di, yi, ii] = row["BS15"]
                    self.BS16[di, yi, ii] = row["BS16"]
                    self.BS17[di, yi, ii] = row["BS17"]
                    self.BS18[di, yi, ii] = row["BS18"]
                    self.BS19[di, yi, ii] = row["BS19"]
                    self.BS20[di, yi, ii] = row["BS20"]
                    self.BS21[di, yi, ii] = row["BS21"]
                    self.BS22[di, yi, ii] = row["BS22"]
                    self.BS23[di, yi, ii] = row["BS23"]
                    self.BS24[di, yi, ii] = row["BS24"]
                    self.BS25[di, yi, ii] = row["BS25"]
                    self.BS26[di, yi, ii] = row["BS26"]
                    self.BS27[di, yi, ii] = row["BS27"]
                    self.BS28[di, yi, ii] = row["BS28"]
                    self.BS29[di, yi, ii] = row["BS29"]
                    self.BS30[di, yi, ii] = row["BS30"]
                    self.BS31[di, yi, ii] = row["BS31"]
                    self.BS32[di, yi, ii] = row["BS32"]
                    self.BS33[di, yi, ii] = row["BS33"]
                    self.BS34[di, yi, ii] = row["BS34"]
                    self.BS35[di, yi, ii] = row["BS35"]
                    self.BS36[di, yi, ii] = row["BS36"]
                    self.BS37[di, yi, ii] = row["BS37"]
                    self.BS38[di, yi, ii] = row["BS38"]
                    self.BS39[di, yi, ii] = row["BS39"]
                    self.BS40[di, yi, ii] = row["BS40"]
                    self.forecast_year[di, yi, ii] = int(end_date[0:4] + end_date[5:7] + end_date[8:])
            
            print(f"balance_sheet_fore_annual finished on [{date_str}]")
        
        except Exception:
            print(f"Error: {di}-{uv.Dates[di]} {yi} {ii}-{uv.Instruments[ii]}")
