from flask import Flask, jsonify, request
from etl.extract import Extractor

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return jsonify({"message": "Hello world!"})

@app.route('/etl', methods=['GET'])
async def etl():
    extractor = Extractor()
    raw = await extractor.extract()
    # transformer = Transformer()
    # parsed = transformer.parse(raw)
    # loader = Loader()
    # loader.load(parsed)
    ...
    return jsonify({"message": "ETL realizado com sucesso!"})
    

if __name__ == '__main__':
    app.run(debug=True)
