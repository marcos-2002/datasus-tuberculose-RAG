from rag.services.db_service import DatabaseService
from rag.services.llm_service import LLM_service
from database.models.general import MensagensChat

class AnswerContructor:
    _QUERY_PROMPT = """
        Você é um agente de IA especializado em análise de dados. Sua tarefa é responder à pergunta do usuário com base nos dados obtidos de um banco de dados.

        - Foi realizada uma consulta SQL para buscar dados relevantes à pergunta do usuário.
        
        ### Instruções:
        1. Analise os dados fornecidos.
        2. Responda à pergunta do usuário de forma clara e com base nos dados.
        3. Se os dados não forem suficientes para responder à pergunta, informe ao usuário que os dados são insuficientes mas não envie os dados que recebeu.
        4. Evite suposições ou informações que não estejam nos dados fornecidos.
        5. Encontre a melhor forma de responder. Se você achar que, baseado nos dados, pode contruir uma resposta mais detalhada, de forma que uma análise seja útil ao usuário, faça isso. 
    """
    
    def __init__(self, question: str, sql: str):
        self.llm_service = LLM_service()
        self.db_service = DatabaseService()
        self.question = question
        self.sql = sql

    async def create_answer(self):
        result_data = await self.db_service.execute_sql(self.sql)

        #validar erro ou se não retornou dados
        
        final_answer = await self.llm_service.ask_question(
            instructions=self._QUERY_PROMPT,
            context=[f"Dados obtidos no banco de dados: f{result_data}"],
            question=self.question,
        )
        
        await MensagensChat.create(
            chat_id=1, 
            sender="bot", 
            content=final_answer
        )

        return final_answer