from rag.services.llm_service import LLM_service
import json

class VisualizationRecommenderConstructor:
    _INSTRUCTION = """ 
    Você é um agente responsável por sugerir tipos de visualizações de dados.

    Será fornecida uma query SQL e a resposta correspondente em formato textual.
    Sua tarefa é analisar os dados retornados e indicar quais tipos de gráficos, dentre as opções disponíveis, são mais adequados para representar a informação.

    As opções são exatamente estas, e os nomes devem ser usados idênticos no JSON de saída:
    grafico_de_barras_horizontal, grafico_de_barras_vertical, grafico_de_linhas, mapas_coropleticos, graficos_com_proporcao

    Regras:
    - Para cada opção, atribua um peso de relevância entre 0 e 1.
    - Responda apenas com um JSON **puro**, **sem usar blocos de código Markdown** (```) ou quaisquer outros caracteres adicionais.
    - Não inclua explicações, texto ou palavras fora do JSON.

    Exemplo de resposta (JSON puro):
    {
        "grafico_de_barras_horizontal": 0.9,
        "grafico_de_barras_vertical": 0.9,
        "grafico_de_linhas": 0.2,
        "mapas_coropleticos": 0.1,
        "graficos_com_proporcao": 0.8
    }

    """
    
    def __init__(self, sql_query: str, final_answer: str):
        self.llm_service = LLM_service()
        self.sql_query = sql_query
        self.final_answer = final_answer
    
    async def create_json(self):
        suggested_json = await self.llm_service.ask_question(
            instructions=self._INSTRUCTION, 
            context=[f"resposta correspondente ao sql em formato textual: {self.final_answer}"], 
            question=self.sql_query
        )
        
        # Tenta converter para objeto Python (dict)
        try:
            json.loads(suggested_json)
            return suggested_json
        except ValueError:
            return f"Resposta não é um JSON válido \n{suggested_json}\n"
    
        