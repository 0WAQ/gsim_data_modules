from gsim.utils.NioData import *
from gsim.data import DataManagerMapped
from gsim.data import DataRegistry as dr
from gsim.data import Universe as uv
from gsim.utils import Calendar
import numpy as np
import pandas as pd
from pathlib import Path

class DmgrWbai_AIFcst_income_statement_fore_quarter(DataManagerMapped):
    def __init__(self):
        DataManagerMapped.__init__(self)

        self.IS01_q = NIO_CUBE()
        self.IS02_q = NIO_CUBE()
        self.IS03_q = NIO_CUBE()
        self.IS04_q = NIO_CUBE()
        self.IS05_q = NIO_CUBE()
        self.IS06_q = NIO_CUBE()
        self.IS07_q = NIO_CUBE()
        self.IS08_q = NIO_CUBE()
        self.IS09_q = NIO_CUBE()
        self.IS11_q = NIO_CUBE()
        self.IS12_q = NIO_CUBE()
        self.IS13_q = NIO_CUBE()
        self.IS14_q = NIO_CUBE()
        self.IS15_q = NIO_CUBE()
        self.IS16_q = NIO_CUBE()
        self.IS17_q = NIO_CUBE()
        self.IS18_q = NIO_CUBE()
        self.IS19_q = NIO_CUBE()
        self.IS30_q = NIO_CUBE()
        self.IS31_q = NIO_CUBE()
        self.IS32_q = NIO_CUBE()
        self.IS33_q = NIO_CUBE()
        self.IS34_q = NIO_CUBE()
        self.IS35_q = NIO_CUBE()
        self.IS36_q = NIO_CUBE()
        self.IS37_q = NIO_CUBE()
        self.IS38_q = NIO_CUBE()
        self.IS39_q = NIO_CUBE()
        self.IS40_q = NIO_CUBE()
        self.IS41_q = NIO_CUBE()
        self.IS42_q = NIO_CUBE()
        self.forecast_quarter = NIO_CUBE()
        self.noy = 3                # num of years
        self.noq = 4 * self.noy    # num of quaters
    
    def initialize(self, id, path, cfg):
        DataManagerMapped.initialize(self, id, path, cfg)
        self.dataPath = Path(cfg.getAttributeString('dataPath'))
        
        self.addData(self.IS01_q, self.tag + ".IS01_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS02_q, self.tag + ".IS02_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS03_q, self.tag + ".IS03_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS04_q, self.tag + ".IS04_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS05_q, self.tag + ".IS05_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS06_q, self.tag + ".IS06_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS07_q, self.tag + ".IS07_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS08_q, self.tag + ".IS08_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS09_q, self.tag + ".IS09_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS11_q, self.tag + ".IS11_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS12_q, self.tag + ".IS12_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS13_q, self.tag + ".IS13_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS14_q, self.tag + ".IS14_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS15_q, self.tag + ".IS15_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS16_q, self.tag + ".IS16_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS17_q, self.tag + ".IS17_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS18_q, self.tag + ".IS18_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS19_q, self.tag + ".IS19_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS30_q, self.tag + ".IS30_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS31_q, self.tag + ".IS31_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS32_q, self.tag + ".IS32_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS33_q, self.tag + ".IS33_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS34_q, self.tag + ".IS34_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS35_q, self.tag + ".IS35_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS36_q, self.tag + ".IS36_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS37_q, self.tag + ".IS37_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS38_q, self.tag + ".IS38_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS39_q, self.tag + ".IS39_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS40_q, self.tag + ".IS40_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS41_q, self.tag + ".IS41_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.IS42_q, self.tag + ".IS42_q", len(uv.Dates), len(uv.Instruments), self.noq)
        self.addData(self.forecast_quarter, self.tag + ".forecast_quarter", len(uv.Dates), len(uv.Instruments), self.noq)


    def loadDay(self, di):
        self.fillnan(di)
        date_str = str(uv.Dates[di])
        file = self.dataPath / date_str
        if not file.exists():
            print(f"income_statement_fore_quarter {date_str} empty")
            return
        
        try:
            df = pd.read_csv(file, dtype={"TICKER": str})
            for ticker, subdf in df.groupby("TICKER"):
                ii = uv.Instruments.lookup(ticker)
                if ii < 0:
                    continue

                subdf: pd.DataFrame = subdf.sort_values("END_DATE")
                for qi, (_, row) in enumerate(subdf.iterrows()):
                    if qi >= self.noq:
                        break
                    end_date = row["END_DATE"]

                    self.IS01_q[di, qi, ii] = row["IS01_q"]
                    self.IS02_q[di, qi, ii] = row["IS02_q"]
                    self.IS03_q[di, qi, ii] = row["IS03_q"]
                    self.IS04_q[di, qi, ii] = row["IS04_q"]
                    self.IS05_q[di, qi, ii] = row["IS05_q"]
                    self.IS06_q[di, qi, ii] = row["IS06_q"]
                    self.IS07_q[di, qi, ii] = row["IS07_q"]
                    self.IS08_q[di, qi, ii] = row["IS08_q"]
                    self.IS09_q[di, qi, ii] = row["IS09_q"]
                    self.IS11_q[di, qi, ii] = row["IS11_q"]
                    self.IS12_q[di, qi, ii] = row["IS12_q"]
                    self.IS13_q[di, qi, ii] = row["IS13_q"]
                    self.IS14_q[di, qi, ii] = row["IS14_q"]
                    self.IS15_q[di, qi, ii] = row["IS15_q"]
                    self.IS16_q[di, qi, ii] = row["IS16_q"]
                    self.IS17_q[di, qi, ii] = row["IS17_q"]
                    self.IS18_q[di, qi, ii] = row["IS18_q"]
                    self.IS19_q[di, qi, ii] = row["IS19_q"]
                    self.IS30_q[di, qi, ii] = row["IS30_q"]
                    self.IS31_q[di, qi, ii] = row["IS31_q"]
                    self.IS32_q[di, qi, ii] = row["IS32_q"]
                    self.IS33_q[di, qi, ii] = row["IS33_q"]
                    self.IS34_q[di, qi, ii] = row["IS34_q"]
                    self.IS35_q[di, qi, ii] = row["IS35_q"]
                    self.IS36_q[di, qi, ii] = row["IS36_q"]
                    self.IS37_q[di, qi, ii] = row["IS37_q"]
                    self.IS38_q[di, qi, ii] = row["IS38_q"]
                    self.IS39_q[di, qi, ii] = row["IS39_q"]
                    self.IS40_q[di, qi, ii] = row["IS40_q"]
                    self.IS41_q[di, qi, ii] = row["IS41_q"]
                    self.IS42_q[di, qi, ii] = row["IS42_q"]
                    self.forecast_quarter[di, qi, ii] = int(end_date[0:4] + end_date[5:7] + end_date[8:])
            
            print(f"income_statement_fore_quarter finished on [{date_str}]")
        
        except Exception as e:
            print(f"Error: {e} on {di} ({uv.Dates[di]}) {ii} ({uv.Instruments[ii]}) {qi}")
