import asyncio
from quart import Quart, json, jsonify, request
import database
from etl.etl import ETL
from rag.rag import RAG
from config import Config
from tortoise import Tortoise
from quart_cors import cors
from database.models.general import MensagensChat

app = Quart(__name__)
app = cors(Quart(__name__), allow_origin="*")
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
    years = [str(i) for i in range(2020, 2024)]  
    months = [i for i in range(1, 13)]
    
    etl = ETL()
    erros = []

    for year in years:
        for month in months:
            try:
                print(f'Importando {month}/{year}')
                await etl.run(year, month)
            except Exception as e:
                erro = {
                    "ano": year,
                    "mes": month,
                    "erro": str(e)
                }
                print(f"Erro ao importar {month}/{year}: {e}")
                erros.append(erro)

    if erros:
        with open('erros_etl.json', 'w', encoding='utf-8') as f:
            json.dump(erros, f, ensure_ascii=False, indent=4)

    return jsonify({"message": "ETL completed", "erros_encontrados": len(erros)})

@app.route('/chat-message', methods=['POST'])
async def chat_message():
    data = await request.get_json()

    if not data or "question" not in data:
        return jsonify({"error": "Missing 'question' field"}), 400

    question = data["question"]
    await database.init()

    await MensagensChat.create(
        chat_id=1, 
        sender="user", 
        content=question
    )

    recent_questions_raw = await MensagensChat.all().order_by("-criado_em").limit(20)

    recent_questions = recent_data = [
        {"id": q.id, "chat_id": q.chat_id, "content": q.content, "criado_em": q.criado_em.isoformat()}
        for q in recent_questions_raw
    ]
    rag = RAG(question, recent_questions)
    
    response = await rag.execute_rag()

    return jsonify({"answer": response["final_answer"], "sql": response["sql_query"]})
