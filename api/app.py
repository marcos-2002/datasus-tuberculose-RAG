import asyncio
from quart import Quart, jsonify
import database
from etl.etl import ETL
from rag.rag import RAG
from config import Config

app = Quart(__name__)
app.config.from_object(Config)

@app.before_serving
async def startup():
    await database.init()

@app.after_serving
async def shutdown():
    await Tortoise.close_connections()

@app.route('/', methods=['GET'])
def hello():
    return jsonify({"message": "Hello world!"})

@app.route('/etl', methods=['GET'])
async def etl():
    years = [str(i) for i in range(2023, 2024)]  

    months = [i for i in range(1, 13)]
    
    etl = ETL()
    
    for year in years:
        for month in months:
            try:
                print(f'Importando {month}/{year}')
                await etl.run(year, month)
            except Exception as e:
                print(f"Erro ao importar {month}/{year}: {e}")

    return jsonify({"message": "ETL completed"})

@app.route('/chat-message', methods=['POST'])
async def chat_message():
    data = request.get_json()

    if not data or "question" not in data:
        return jsonify({"error": "Missing 'question' field"}), 400

    question = data["question"]
    await database.init()
    
    rag = RAG(question)
    
    final_answer = await rag.execute_rag()

    return jsonify({"answer": final_answer})
