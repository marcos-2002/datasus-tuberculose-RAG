import pandas as pd
from pysus import SINAN
import numpy as np

class Extractor:
    async def extract(self, year, month):
        sinan = SINAN().load()
        
        files = sinan.get_files(dis_code=["TUBE"], year=[year])
        file = files[0]
        parquet = sinan.download(file, local_dir="./parquets")
        df = parquet.to_dataframe()

        df["DT_NOTIFIC"] = pd.to_datetime(df["DT_NOTIFIC"], errors="coerce") 
        df_filtrado = df[df["DT_NOTIFIC"].dt.month == month]

        return df_filtrado
