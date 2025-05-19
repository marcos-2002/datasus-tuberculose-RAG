from etl.extract import Extractor
from etl.load import Loader
from etl.transform import Transformer

class ETL:
    async def run(self, year, month):
        extractor = Extractor()
        data = await extractor.extract(year, month)
     
        transformer = Transformer()
        parsed = transformer.parse(data)
    
        if(parsed):
            loader = Loader()
            await loader.insert(parsed)
    