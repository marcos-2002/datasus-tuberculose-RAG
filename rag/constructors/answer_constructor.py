from rag.services.db_service import DatabaseService
from rag.services.llm_service import LLM_service


class AnswerContructor:
    _QUERY_PROMPT = """
        Você é um agente de IA especializado em análise de dados. Sua tarefa é responder à pergunta do usuário com base nos dados obtidos de um banco de dados.

        - Foi realizada uma consulta SQL para buscar dados relevantes à pergunta do usuário.
        
        ### Instruções:
        1. Analise os dados fornecidos.
        2. Responda à pergunta do usuário de forma clara e concisa.
        3. Se os dados não forem suficientes para responder à pergunta, informe isso ao usuário.
        4. Evite suposições ou informações que não estejam nos dados fornecidos.
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
        print(final_answer)

        return final_answer