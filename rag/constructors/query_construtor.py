from rag.services.db_service import DatabaseService
from rag.services.llm_service import LLM_service
from rag.services.sql_validator_service import SQLValidatorService


class QueryConstructor:
    _QUERY_PROMPT = """ 
    Você é um agente de construção de querys para o postgres SQL em um processo de RAG.
    O banco de dados está estrutura em um esquema estrela
    existe uma tabela de fatos, chamada "fatos". ela tem os campos principais chamados de "data", "metrica" e "valor",
    a tabela de fatos tambem tem as foreignkeys que fazem referencia a todas as outras tabelas de dimensão
    o nome de todas as foreign_keys na tabela fatos, é o mesmo nome da tabela de dimensão, porém com "_id" no final.
    por exemplo, a tabela de fatos tem a "uf_notif_id" para referenciar a tabela uf_notif
    atualmente a tabela fatos tem apenas uma metrica, que é "casos_confirmados"
    Se o usuário pedir um período específico, use a coluna "data" na tabela fatos. Contudo, considere que não temos informações de dias. Dessa forma, todas as datas são salvas com o dia primeiro do mês. Portanto, se o usuário pedir informações granulada em dia, diga que não tem essa informação e que pode fornecer dados de no mínimo um período mensal.
    todas as tabelas de dimensão tem a mesma estrutura que é a abaixo:
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=255)
    criado_em = fields.DatetimeField(auto_now_add=True)
    
    Baseado nessas informações, construa a query SQL para o postgres, seguinte todas as boas práticas SQL, de forma que busque dados relacionados a pergunta do usuário. Essa consulta será executada em um processo posterior 
    do RAG, então envie como resposta apenas a string da consulta. não inclua frases que não são SQL. inclua Markdown code block -> ```sql , você deve sempre retornar uma string com esse markdown.
    
    Você está recebendo a estrutura do banco de dados. O banco tem mais dimensões, porém ainda não terminei de descrever elas para você, então considere apenas as que você possui a descrição. Se o usuário fizer perguntar que envolvam quais outras informações além das que você tem disponível a partir das dimensões, desconsidere.
    Também considere que as dimensões pop_sit_rua e cultura_escarro ainda não estão sendo importadas corretamente, então desconsidere elas caso o usuário pergunte algo sobre.
    Se o usuário solicitar um **período de tempo**, utilize `WHERE fatos.data BETWEEN ...`, garantindo que os filtros sejam feitos com base no primeiro dia do mês.
    Para obter a quantidade total de casos, sempre use SUM na coluna valor de fator, nunca use COUNT
     Os dados possuem uma única métrica: número de casos. Cada dimensão apresenta um total independente, e a soma entre dimensões pode levar a duplicação
    por exemplo, numero de casos por uf_notif.
    numero de casos por faixa etaria.
    se eu somar o numero de casos por uf_notif, tenho o numero total de casos
    mas se eu somar o numero de casos por uf_notif e o numero de casos por faixa etaria, vai dar o dobro em relação ao numero total de casos reais.
    Outra informação muito importante sobre a modelagem, é que os registros na tabela de fatos, só tem uma dimensão por registro. Dessa forma, você não pode fazer JOIN entre 2 dimensões na tabela de fatos.
    """
    
    def __init__(self, question: str, context: str):
        self.llm_service = LLM_service()
        self.db_service = DatabaseService()  
        self.sql_validator_service = SQLValidatorService()
        self.context = context
        self.question = question
    
    async def create_query(self):
        sql = await self.llm_service.ask_question(
            instructions=self._QUERY_PROMPT, 
            #context=[f"estrutura do banco de dados: {self.context["db_structure"]}"], 
            question=self.question
        )
        print(sql)
        
        validatorResponse = self.sql_validator_service.validate(sql)
        
        if validatorResponse["is_valid"] == False: return #todo: pensar no que fazer aqui
        
        query = validatorResponse["valid_sql"]
        return query
    
        