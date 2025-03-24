from rag.constructors.context_construtor import ContextConstructor
from rag.constructors.query_construtor import QueryConstructor
from rag.constructors.answer_constructor import AnswerContructor

class RAG:
    def __init__(self, question: str):
        self.question = question

    async def execute_rag(self):
        context_constructor = ContextConstructor(self.question)
        context = await context_constructor.create_context()
        
        query_constructor = QueryConstructor(self.question, context)
        sql_query = await query_constructor.create_query()

        if not sql_query:
            return "Could not generate a valid SQL query."
       
        answer_constructor = AnswerContructor(self.question, sql_query)
        final_answer = await answer_constructor.create_answer()
       
        return final_answer
