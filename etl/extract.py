import pandas as pd
from pysus import SINAN

class Extractor:
    async def extract(self, year, month):
        sinan = SINAN().load()
        
        files = sinan.get_files(dis_code=["TUBE"], year=[year])
        file = files[0]
        parquet = sinan.download(file, local_dir="./parquets")
        df = parquet.to_dataframe()
        print(len(df))

        df["DT_NOTIFIC"] = pd.to_datetime(df["DT_NOTIFIC"], errors="coerce")
        valores_unicos = df["CS_SEXO"]
        #print(f'valores unicos: {len(valores_unicos)}')
        # quantidade_3 = (df["POP_SAUDE"] == '3').sum()
        # print(f'quantidade de 3: {quantidade_3}')
        # quantidade_1 = (df["POP_SAUDE"] == '1').sum()
        # print(f'quantidade de 1: {quantidade_1}')
        # quantidade_2 = (df["POP_SAUDE"] == '2').sum()
        # print(f'quantidade de 2: {quantidade_2}')
        # quantidade_9 = (df["POP_SAUDE"] == '9').sum()
        # print(f'quantidade de 9: {quantidade_9}')
     
        df_filtrado = df[df["DT_NOTIFIC"].dt.month == month]

        return df_filtrado
