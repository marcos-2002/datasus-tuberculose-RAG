from rag.constructors.context_construtor import ContextConstructor
from rag.constructors.query_construtor import QueryConstructor
from rag.constructors.answer_constructor import AnswerContructor
from rag.services.llm_service import LLM_service

class RAG:
    def __init__(self, question: str, last_questions):
        self.question = question
        self.last_questions = last_questions
        self.llm_service = LLM_service()

    async def execute_rag(self):
        response = await self.llm_service.ask_question(
            instructions="Você é um agente responsável por ajudar pesquisadores da área da saúde. Você faz parte da primeira etapa de uma pipeline para responder a pergunta do usuário. Se a pergunta do usuário não envolver dados do datasus e tubercolose ou se esses dados já estiverem disponíveis nas últimas mensagens, você irá responder a pergunta do usuário. Caso contrário, você responde 0 e será feita uma busca por mais dados para que a pergunta possa respodinda em uma etapa posterior da pipeline. Você deve analisar a pergunta e verificar, baseado no teor da pergunta e também baseado nas informações das últimas mensagens, se você já é capaz de responder a pergunta ou precisa de mais dados. Se você precisar de mais dados, apenas retorne a string 0. Você deve julgar que é capaz de responder a pergunta do usuário apenas se tiver muita certeza de que a resposta para a pergunta envolve dados que você já tem disponível. Além disso, se você achar que tem os dados disponível, deve fazer uma segunda checagem, comparando exatamente a pergunta e exatamente os dados que você tem disponível para confirmar se realmente eles respondem a pergunta (por exemplo se forem dados parecidos mas agora o usuário pediu em relação a outro período de tempo ou outra região, você deve retornar 0). Caso você ache que possa envolver quaisquer dados sobre o datasus e tubercolose que você ainda não tem, retorne 0. Você deve levar em consideração o teor da pergunta para saber se necessita de dados do datasus e tubercolose ou não, para a resposta. Considere que a pergunta pode ser referente a ajuda para analisar dados que já foram mencionados em mensagens anteriores. Também leve e consideração o seguinte: baseado na pergunta, se eu tivesse mais dados do datasus e tubercolose, isso levaria para uma resposta mais precisa? se sim, retorne 0. Mas pode ser que seja uma pergunta simples e que a resposta não envolva dados. Nesse caso apenas analise a pergunta e de uma resposta para o usuário. Por exemplo, se o usuário disser Olá ou Teste ou perguntas de teor geral (que não são relacionadas a tuberculose), apenas responda uma mensagem amigável, como se você fosse um assistente de chat normal, considere que essa resposta será vista pelo usuário normal então nesse caso você deve tratar no contexto de uma resposta geral",
            context=[f"{q['content']} ({q['criado_em']})" for q in self.last_questions],
            question=self.question
        )

        if response.strip() != "0":
            return {
                "final_answer": response,
                "sql_query": ""
            }

        context_constructor = ContextConstructor(self.question)
        context = await context_constructor.create_context()
        
        query_constructor = QueryConstructor(self.question, context)
        sql_query = await query_constructor.create_query()

        if not sql_query:
            return "Could not generate a valid SQL query."
       
        answer_constructor = AnswerContructor(self.question, sql_query)
        final_answer = await answer_constructor.create_answer()
       
        return {
            "final_answer": final_answer,
            "sql_query": sql_query
        }
