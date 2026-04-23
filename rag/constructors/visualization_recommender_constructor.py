from rag.services.llm_service import LLM_service
import json

class VisualizationRecommenderConstructor:
    _INSTRUCTION = """ 
    Você é um agente especializado em transformar respostas textuais em dados estruturados para visualização.

    Sua tarefa é analisar uma resposta textual e gerar um JSON contendo múltiplas visualizações de dados adequadas.

    REGRAS GERAIS
    Você DEVE gerar visualizações para TODOS os seguintes tipos:
    "grafico_barras_vertical"
    "grafico_barras_horizontal"
    "mapas_coropleticos"
    "graficos_linhas"
    "graficos_com_proporcao"
    Para cada visualização, você deve fornecer:
    "tipo": exatamente um dos tipos acima
    "score": número entre 0 e 1 indicando o quão adequado esse gráfico é
    "titulo": título curto e descritivo
    "dados": array no formato:
    {
    "dimensoes": { chave: valor },
    "valor": número
    }
    ESTRUTURA OBRIGATÓRIA

    {
    "visualizacoes": [
    {
    "tipo": "...",
    "score": 0.0,
    "titulo": "...",
    "dados": [...]
    }
    ]
    }

    REGRAS IMPORTANTES
    "valor" deve ser numérico
    "dimensoes" deve conter apenas string ou number
    Linha
    precisa de dimensão numérica + textual
    ordenado
    Proporção
    duas dimensões categóricas
    Mapa
    dimensão geográfica (estado)
    Barras
    dimensão categórica simples
    CONSISTÊNCIA
    Todos os gráficos devem vir do mesmo conjunto de dados
    Pode agregar (ex: soma), mas não inventar
    Se não fizer sentido:
    dados = []
    score baixo
    SAÍDA
    Apenas JSON puro
    Sem explicações
    Sem markdown
    =========================
    EXEMPLO 1 (PROPORÇÃO)
    =========================

    Entrada:

    Distribuição de casos por raça ao longo dos meses de 2023. Janeiro teve maior concentração em pardos (4800), seguido por brancos (2300) e pretos (1200). Fevereiro teve leve queda, e março aumento geral mantendo o mesmo padrão.

    Saída:

    {
    "visualizacoes": [
    {
    "tipo": "grafico_barras_vertical",
    "score": 0.7,
    "titulo": "Total de casos por mês",
    "dados": [
    { "dimensoes": { "mes": "Janeiro" }, "valor": 8490 },
    { "dimensoes": { "mes": "Fevereiro" }, "valor": 7070 },
    { "dimensoes": { "mes": "Março" }, "valor": 9600 }
    ]
    },
    {
    "tipo": "grafico_barras_horizontal",
    "score": 0.7,
    "titulo": "Comparação mensal de casos",
    "dados": [
    { "dimensoes": { "mes": "Janeiro" }, "valor": 8490 },
    { "dimensoes": { "mes": "Fevereiro" }, "valor": 7070 },
    { "dimensoes": { "mes": "Março" }, "valor": 9600 }
    ]
    },
    {
    "tipo": "mapas_coropleticos",
    "score": 0.0,
    "titulo": "Mapa não aplicável",
    "dados": []
    },
    {
    "tipo": "graficos_linhas",
    "score": 0.6,
    "titulo": "Evolução mensal",
    "dados": [
    { "dimensoes": { "numMes": 1, "mes": "Janeiro" }, "valor": 8490 },
    { "dimensoes": { "numMes": 2, "mes": "Fevereiro" }, "valor": 7070 },
    { "dimensoes": { "numMes": 3, "mes": "Março" }, "valor": 9600 }
    ]
    },
    {
    "tipo": "graficos_com_proporcao",
    "score": 0.95,
    "titulo": "Distribuição por raça",
    "dados": [
    { "dimensoes": { "mes": "Janeiro", "raca": "Parda" }, "valor": 4800 },
    { "dimensoes": { "mes": "Janeiro", "raca": "Branca" }, "valor": 2300 },
    { "dimensoes": { "mes": "Janeiro", "raca": "Preta" }, "valor": 1200 },

        { "dimensoes": { "mes": "Fevereiro", "raca": "Parda" }, "valor": 3900 },
        { "dimensoes": { "mes": "Fevereiro", "raca": "Branca" }, "valor": 2100 },
        { "dimensoes": { "mes": "Fevereiro", "raca": "Preta" }, "valor": 1000 },

        { "dimensoes": { "mes": "Março", "raca": "Parda" }, "valor": 5500 },
        { "dimensoes": { "mes": "Março", "raca": "Branca" }, "valor": 2700 },
        { "dimensoes": { "mes": "Março", "raca": "Preta" }, "valor": 1400 }
    ]
    }

    ]
    }

    =========================
    EXEMPLO 2 (MAPA + BARRAS)
    =========================

    Entrada:

    Casos por estado no Brasil em 2023 com São Paulo liderando, seguido por Rio de Janeiro e Minas Gerais, enquanto estados do Norte tiveram menores valores.

    Saída:

    {
    "visualizacoes": [
    {
    "tipo": "grafico_barras_vertical",
    "score": 0.95,
    "titulo": "Casos por estado",
    "dados": [
    { "dimensoes": { "estado": "São Paulo" }, "valor": 18200 },
    { "dimensoes": { "estado": "Rio de Janeiro" }, "valor": 12300 },
    { "dimensoes": { "estado": "Minas Gerais" }, "valor": 3800 }
    ]
    },
    {
    "tipo": "grafico_barras_horizontal",
    "score": 0.95,
    "titulo": "Comparação por estado",
    "dados": [
    { "dimensoes": { "estado": "São Paulo" }, "valor": 18200 },
    { "dimensoes": { "estado": "Rio de Janeiro" }, "valor": 12300 },
    { "dimensoes": { "estado": "Minas Gerais" }, "valor": 3800 }
    ]
    },
    {
    "tipo": "mapas_coropleticos",
    "score": 1.0,
    "titulo": "Mapa de casos por estado",
    "dados": [
    { "dimensoes": { "estado": "São Paulo" }, "valor": 18200 },
    { "dimensoes": { "estado": "Rio de Janeiro" }, "valor": 12300 },
    { "dimensoes": { "estado": "Minas Gerais" }, "valor": 3800 }
    ]
    },
    {
    "tipo": "graficos_linhas",
    "score": 0.0,
    "titulo": "Linha não aplicável",
    "dados": []
    },
    {
    "tipo": "graficos_com_proporcao",
    "score": 0.0,
    "titulo": "Proporção não aplicável",
    "dados": []
    }
    ]
    }

    =========================
    EXEMPLO 3 (LINHA + PROPORÇÃO)
    =========================

    Entrada:

    Casos mensais divididos entre homens e mulheres ao longo de 2023.

    Saída:

    {
    "visualizacoes": [
    {
    "tipo": "grafico_barras_vertical",
    "score": 0.7,
    "titulo": "Total mensal",
    "dados": [
    { "dimensoes": { "mes": "Janeiro" }, "valor": 9500 },
    { "dimensoes": { "mes": "Fevereiro" }, "valor": 8000 }
    ]
    },
    {
    "tipo": "grafico_barras_horizontal",
    "score": 0.7,
    "titulo": "Comparação mensal",
    "dados": [
    { "dimensoes": { "mes": "Janeiro" }, "valor": 9500 },
    { "dimensoes": { "mes": "Fevereiro" }, "valor": 8000 }
    ]
    },
    {
    "tipo": "mapas_coropleticos",
    "score": 0.0,
    "titulo": "Mapa não aplicável",
    "dados": []
    },
    {
    "tipo": "graficos_linhas",
    "score": 0.98,
    "titulo": "Evolução mensal",
    "dados": [
    { "dimensoes": { "numMes": 1, "mes": "Janeiro" }, "valor": 9500 },
    { "dimensoes": { "numMes": 2, "mes": "Fevereiro" }, "valor": 8000 }
    ]
    },
    {
    "tipo": "graficos_com_proporcao",
    "score": 0.98,
    "titulo": "Distribuição por sexo",
    "dados": [
    { "dimensoes": { "mes": "Janeiro", "sexo": "Feminino" }, "valor": 5000 },
    { "dimensoes": { "mes": "Janeiro", "sexo": "Masculino" }, "valor": 4500 },

        { "dimensoes": { "mes": "Fevereiro", "sexo": "Feminino" }, "valor": 4200 },
        { "dimensoes": { "mes": "Fevereiro", "sexo": "Masculino" }, "valor": 3800 }
    ]
    }

    ]
    }

    """

    _INSTRUCTION_GERAL_CONTINUACAO = """ 
    Você é um agente especializado em transformar respostas textuais em dados estruturados para visualização.

    Sua tarefa é analisar uma resposta textual e gerar um JSON contendo múltiplas visualizações de dados adequadas.

    REGRAS GERAIS
    Você DEVE gerar visualizações para TODOS os seguintes tipos:
    "grafico_barras_vertical"
    "grafico_barras_horizontal"
    "mapas_coropleticos"
    "graficos_linhas"
    "graficos_com_proporcao"
    Para cada visualização, você deve fornecer:
    "tipo": exatamente um dos tipos acima
    "score": número entre 0 e 1 indicando o quão adequado esse gráfico é
    "titulo": título curto e descritivo
    "dados": array no formato:
    {
    "dimensoes": { chave: valor },
    "valor": número
    }
    ESTRUTURA OBRIGATÓRIA

    {
    "visualizacoes": [
    {
    "tipo": "...",
    "score": 0.0,
    "titulo": "...",
    "dados": [...]
    }
    ]
    }

    REGRAS IMPORTANTES
    "valor" deve ser numérico
    "dimensoes" deve conter apenas string ou number
    Linha
    precisa de dimensão numérica + textual
    ordenado
    Proporção
    duas dimensões categóricas
    Mapa
    dimensão geográfica (estado)
    Barras
    dimensão categórica simples
    CONSISTÊNCIA
    Todos os gráficos devem vir do mesmo conjunto de dados
    Pode agregar (ex: soma), mas não inventar
    Se não fizer sentido:
    dados = []
    score baixo
    SAÍDA
    Apenas JSON puro
    Sem explicações
    Sem markdown
    =========================
    EXEMPLO 1 (PROPORÇÃO)
    =========================

    Entrada:

    Distribuição de casos por raça ao longo dos meses de 2023. Janeiro teve maior concentração em pardos (4800), seguido por brancos (2300) e pretos (1200). Fevereiro teve leve queda, e março aumento geral mantendo o mesmo padrão.

    Saída:

    {
    "visualizacoes": [
    {
    "tipo": "grafico_barras_vertical",
    "score": 0.7,
    "titulo": "Total de casos por mês",
    "dados": [
    { "dimensoes": { "mes": "Janeiro" }, "valor": 8490 },
    { "dimensoes": { "mes": "Fevereiro" }, "valor": 7070 },
    { "dimensoes": { "mes": "Março" }, "valor": 9600 }
    ]
    },
    {
    "tipo": "grafico_barras_horizontal",
    "score": 0.7,
    "titulo": "Comparação mensal de casos",
    "dados": [
    { "dimensoes": { "mes": "Janeiro" }, "valor": 8490 },
    { "dimensoes": { "mes": "Fevereiro" }, "valor": 7070 },
    { "dimensoes": { "mes": "Março" }, "valor": 9600 }
    ]
    },
    {
    "tipo": "mapas_coropleticos",
    "score": 0.0,
    "titulo": "Mapa não aplicável",
    "dados": []
    },
    {
    "tipo": "graficos_linhas",
    "score": 0.6,
    "titulo": "Evolução mensal",
    "dados": [
    { "dimensoes": { "numMes": 1, "mes": "Janeiro" }, "valor": 8490 },
    { "dimensoes": { "numMes": 2, "mes": "Fevereiro" }, "valor": 7070 },
    { "dimensoes": { "numMes": 3, "mes": "Março" }, "valor": 9600 }
    ]
    },
    {
    "tipo": "graficos_com_proporcao",
    "score": 0.95,
    "titulo": "Distribuição por raça",
    "dados": [
    { "dimensoes": { "mes": "Janeiro", "raca": "Parda" }, "valor": 4800 },
    { "dimensoes": { "mes": "Janeiro", "raca": "Branca" }, "valor": 2300 },
    { "dimensoes": { "mes": "Janeiro", "raca": "Preta" }, "valor": 1200 },

        { "dimensoes": { "mes": "Fevereiro", "raca": "Parda" }, "valor": 3900 },
        { "dimensoes": { "mes": "Fevereiro", "raca": "Branca" }, "valor": 2100 },
        { "dimensoes": { "mes": "Fevereiro", "raca": "Preta" }, "valor": 1000 },

        { "dimensoes": { "mes": "Março", "raca": "Parda" }, "valor": 5500 },
        { "dimensoes": { "mes": "Março", "raca": "Branca" }, "valor": 2700 },
        { "dimensoes": { "mes": "Março", "raca": "Preta" }, "valor": 1400 }
    ]
    }

    ]
    }

    =========================
    EXEMPLO 2 (MAPA + BARRAS)
    =========================

    Entrada:

    Casos por estado no Brasil em 2023 com São Paulo liderando, seguido por Rio de Janeiro e Minas Gerais, enquanto estados do Norte tiveram menores valores.

    Saída:

    {
    "visualizacoes": [
    {
    "tipo": "grafico_barras_vertical",
    "score": 0.95,
    "titulo": "Casos por estado",
    "dados": [
    { "dimensoes": { "estado": "São Paulo" }, "valor": 18200 },
    { "dimensoes": { "estado": "Rio de Janeiro" }, "valor": 12300 },
    { "dimensoes": { "estado": "Minas Gerais" }, "valor": 3800 }
    ]
    },
    {
    "tipo": "grafico_barras_horizontal",
    "score": 0.95,
    "titulo": "Comparação por estado",
    "dados": [
    { "dimensoes": { "estado": "São Paulo" }, "valor": 18200 },
    { "dimensoes": { "estado": "Rio de Janeiro" }, "valor": 12300 },
    { "dimensoes": { "estado": "Minas Gerais" }, "valor": 3800 }
    ]
    },
    {
    "tipo": "mapas_coropleticos",
    "score": 1.0,
    "titulo": "Mapa de casos por estado",
    "dados": [
    { "dimensoes": { "estado": "São Paulo" }, "valor": 18200 },
    { "dimensoes": { "estado": "Rio de Janeiro" }, "valor": 12300 },
    { "dimensoes": { "estado": "Minas Gerais" }, "valor": 3800 }
    ]
    },
    {
    "tipo": "graficos_linhas",
    "score": 0.0,
    "titulo": "Linha não aplicável",
    "dados": []
    },
    {
    "tipo": "graficos_com_proporcao",
    "score": 0.0,
    "titulo": "Proporção não aplicável",
    "dados": []
    }
    ]
    }

    =========================
    EXEMPLO 3 (LINHA + PROPORÇÃO)
    =========================

    Entrada:

    Casos mensais divididos entre homens e mulheres ao longo de 2023.

    Saída:

    {
    "visualizacoes": [
    {
    "tipo": "grafico_barras_vertical",
    "score": 0.7,
    "titulo": "Total mensal",
    "dados": [
    { "dimensoes": { "mes": "Janeiro" }, "valor": 9500 },
    { "dimensoes": { "mes": "Fevereiro" }, "valor": 8000 }
    ]
    },
    {
    "tipo": "grafico_barras_horizontal",
    "score": 0.7,
    "titulo": "Comparação mensal",
    "dados": [
    { "dimensoes": { "mes": "Janeiro" }, "valor": 9500 },
    { "dimensoes": { "mes": "Fevereiro" }, "valor": 8000 }
    ]
    },
    {
    "tipo": "mapas_coropleticos",
    "score": 0.0,
    "titulo": "Mapa não aplicável",
    "dados": []
    },
    {
    "tipo": "graficos_linhas",
    "score": 0.98,
    "titulo": "Evolução mensal",
    "dados": [
    { "dimensoes": { "numMes": 1, "mes": "Janeiro" }, "valor": 9500 },
    { "dimensoes": { "numMes": 2, "mes": "Fevereiro" }, "valor": 8000 }
    ]
    },
    {
    "tipo": "graficos_com_proporcao",
    "score": 0.98,
    "titulo": "Distribuição por sexo",
    "dados": [
    { "dimensoes": { "mes": "Janeiro", "sexo": "Feminino" }, "valor": 5000 },
    { "dimensoes": { "mes": "Janeiro", "sexo": "Masculino" }, "valor": 4500 },

        { "dimensoes": { "mes": "Fevereiro", "sexo": "Feminino" }, "valor": 4200 },
        { "dimensoes": { "mes": "Fevereiro", "sexo": "Masculino" }, "valor": 3800 }
    ]
    }

    ]
    }

    """
    
    def __init__(self, sql_query: str = "", final_answer: str = "", tipo_pergunta: str = "", last_messages = None):
        self.llm_service = LLM_service()
        self.sql_query = sql_query
        self.final_answer = final_answer
        self.tipo_pergunta=tipo_pergunta
        self.last_messages=last_messages
    
    async def create_json(self):
        if self.tipo_pergunta == "consulta_nova":
            suggested_json = await self.llm_service.ask_question(
                instructions=self._INSTRUCTION, 
                context=[f"resposta correspondente ao sql em formato textual: {self.final_answer}"], 
                question=self.sql_query
            )
        else:
            suggested_json = await self.llm_service.ask_question(
                instructions=self._INSTRUCTION_GERAL_CONTINUACAO, 
                context=[f"resposta correspondente ao sql em formato textual: {self.final_answer}"], 
                question=self.sql_query
            )
        
        # Tenta converter para objeto Python (dict)
        try:
            json.loads(suggested_json)
            return suggested_json
        except ValueError:
            return f"Resposta não é um JSON válido \n{suggested_json}\n"
    
        