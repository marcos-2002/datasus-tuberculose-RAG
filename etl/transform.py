import pandas as pd
from database.enums import DimensionEnum

class Transformer():
    def parse(self, data):
        column_mapping = DimensionEnum.get_column_mapping()
    
        # filtra apenas as colunas que estão no Enum
        valid_columns = list(set(column_mapping.keys()) & set(data.columns))
        df_filtered = data[valid_columns].copy()

        # renomeia as colunas conforme o mapeamento
        df_renamed = df_filtered.rename(columns=column_mapping)

        #conversão dos tipos
        for col in df_renamed.columns:
            if col in ["data", "ano_nasc"]:
                df_renamed[col] = df_renamed[col].astype(str)
            else:
                df_renamed[col] = pd.to_numeric(df_renamed[col], errors="coerce").astype("Int64")

        result = df_renamed.to_dict(orient='records')
        return result