import asyncio
from flask import Flask, json, jsonify, request
from etl.etl import ETL

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return jsonify({"message": "Hello world!"})

@app.route('/etl', methods=['GET'])
async def etl():
    years = [f"{i:02}" for i in range(22, 24)]  # Anos de 02 até 23
    months = [f"{i}" for i in range(2, 14)]  # Meses de 2 até 13
    dimensions = [
        "Região_de_notificação", "UF_de_notificação", "Município_de_notificação",
        "Capital_de_notificação", "Região_de_Saúde_(CIR)_de_notif", "Macrorreg.de_Saúde_de_notific",
        "Microrregião_IBGE_de_notific", "Reg.Metropolit/RIDE_de_notific", "Territ_da_Cidadania_de_notific",
        "Mesorregião_PNDR_de_notific", "Região_de_residência", "UF_de_residência",
        "Município_de_residência", "Capital_de_residência", "Região_de_Saúde_(CIR)_de_resid",
        "Macrorreg.de_Saúde_de_residênc", "Microrregião_IBGE_de_residênc", "Reg.Metropolit/RIDE_de_resid",
        "Territ_da_Cidadania_de_resid", "Fx_Etária", "Fx_Etária_7", "Fx_Etária_13",
        "Sexo", "Tipo_de_entrada__", "Institucionalizado", "PPL",
        "Imigrante", "Benefic._governo", "Forma", "Se_Extrapulm.1", "Se_Extrapulm.2", "Aids", "Alcoolismo",
        "Diabetes", "Doença_mental", "Drogas_ilícitas", "Tabagismo", "Outra_doença", "Confirmação_laboratorial",
        "1ªBac_Escarro", "Teste_rápido_TB", "Teste_sensibilidade", "HIV",
        "Antirretroviral", "TDO_realizado", "Bacilosc_2º_mês", "Bacilosc_6º_mês", "Situação_Encerra."
    ]
        
        #"Mesorregião_PNDR_de_residência"
        #Pop._Sit._Rua
        #"Profissionais de Saúde"
        #"2ªBac_Escarro"
        #"Cultura_escarro"
        
   # teste
    # years = [f"{i:02}" for i in range(23, 24)]  # Anos de 02 até 23
    # months = [f"{i}" for i in range(2, 3)]  # Meses de 2 até 14
    # dimensions = [
    #     "Macrorreg.de_Saúde_de_notific",
    # ]
    etl = ETL()
    
    errors = [] 

    for year in years:
        for month in months:
            for dimension in dimensions:
                try:
                    print(f'importando {dimension} - {month}/{year}')
                    await etl.run(year, month, dimension)
                    await asyncio.sleep(1)
                except Exception as e:
                    print(f"Error in {year}-{month} ({dimension}): {e}")
                    errors.append({"year": year, "month": month, "dimension": dimension, "error": str(e)})

    if errors:
        with open("etl_errors.json", "w") as f:
            json.dump(errors, f, indent=4)

    return jsonify({"message": "ETL completed", "errors": errors})
    
if __name__ == '__main__':
    app.run(debug=True)
