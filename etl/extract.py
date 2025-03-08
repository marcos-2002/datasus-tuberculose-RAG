import json
import requests
import re
from bs4 import BeautifulSoup
import urllib.parse

class Extractor:
    
    async def extract(self):
        raw_data_list = []
        
        #years = [f"{i:02}" for i in range(2, 24)]  # Anos de 02 até 23
        #months = [f"{i}" for i in range(2, 15)]  # Meses de 2 até 14
        # dimensions = [
        #     "Fx_Etária", "Região_de_notificação", "UF_de_notificação", "Município_de_notificação",
        #     "Capital_de_notificação", "Região_de_Saúde_(CIR)_de_notif", "Macrorreg.de_Saúde_de_notific",
        #     "Microrregião_IBGE_de_notific", "Reg.Metropolit/RIDE_de_notific", "Territ_da_Cidadania_de_notific",
        #     "Mesorregião_PNDR_de_notific", "Região_de_residência", "UF_de_residência",
        #     "Município_de_residência", "Capital_de_residência", "Região_de_Saúde_(CIR)_de_resid",
        #     "Macrorreg.de_Saúde_de_residênc", "Microrregião_IBGE_de_residênc", "Reg.Metropolit/RIDE_de_resid",
        #     "Territ_da_Cidadania_de_resid"
        # ]
        
        
        #teste
        years = [f"{i:02}" for i in range(23, 24)]  # Anos de 02 até 23
        months = [f"{i}" for i in range(13, 14)]  # Meses de 2 até 14
        dimensions = ["Fx_Etária"]

        print(years)
        print(months)
        print(dimensions)
        for year in years:
            for month in months:
                for dimension in dimensions:
                    response = await self.make_request(dimension, year, month)
                    raw_data_list.append(response)
        
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(raw_data_list, json_file, ensure_ascii=False, indent=4)

        print("Arquivo JSON salvo com sucesso: data.json")

    async def make_request(self, dimension, year, notification_month):
        url = "http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sinannet/cnv/tubercbr.def"

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "http://tabnet.datasus.gov.br",
            "Referer": "http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sinannet/cnv/tubercbr.def",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
        }
        
        body = "Linha=Situa%E7%E3o_Encerra.&Coluna=--N%E3o-Ativa--&Incremento=Casos_confirmados&Arquivos=tubebr23.dbf&pesqmes1=Digite+o+texto+e+ache+f%E1cil&SAno_Diagn%F3stico=TODAS_AS_CATEGORIAS__&pesqmes2=Digite+o+texto+e+ache+f%E1cil&SM%EAs_Diagn%F3stico=2&pesqmes3=Digite+o+texto+e+ache+f%E1cil&SAno_Notifica%E7%E3o=TODAS_AS_CATEGORIAS__&pesqmes4=Digite+o+texto+e+ache+f%E1cil&SM%EAs_Notifica%E7%E3o=2&pesqmes5=Digite+o+texto+e+ache+f%E1cil&SAno_In._Tratamento=TODAS_AS_CATEGORIAS__&pesqmes6=Digite+o+texto+e+ache+f%E1cil&SM%EAs_In._Tratamento=TODAS_AS_CATEGORIAS__&SRegi%E3o_de_notifica%E7%E3o=TODAS_AS_CATEGORIAS__&pesqmes8=Digite+o+texto+e+ache+f%E1cil&SUF_de_notifica%E7%E3o=TODAS_AS_CATEGORIAS__&pesqmes9=Digite+o+texto+e+ache+f%E1cil&SMunic%EDpio_de_notifica%E7%E3o=TODAS_AS_CATEGORIAS__&pesqmes10=Digite+o+texto+e+ache+f%E1cil&SCapital_de_notifica%E7%E3o=TODAS_AS_CATEGORIAS__&pesqmes11=Digite+o+texto+e+ache+f%E1cil&SRegi%E3o_de_Sa%FAde_%28CIR%29_de_notif=TODAS_AS_CATEGORIAS__&pesqmes12=Digite+o+texto+e+ache+f%E1cil&SMacrorreg.de_Sa%FAde_de_notific=TODAS_AS_CATEGORIAS__&pesqmes13=Digite+o+texto+e+ache+f%E1cil&SMicrorregi%E3o_IBGE_de_notific=TODAS_AS_CATEGORIAS__&pesqmes14=Digite+o+texto+e+ache+f%E1cil&SReg.Metropolit%2FRIDE_de_notific=TODAS_AS_CATEGORIAS__&pesqmes15=Digite+o+texto+e+ache+f%E1cil&STerrit_da_Cidadania_de_notific=TODAS_AS_CATEGORIAS__&pesqmes16=Digite+o+texto+e+ache+f%E1cil&SMesorregi%E3o_PNDR_de_notific=TODAS_AS_CATEGORIAS__&SAmaz%F4nia_Legal_%28notifica%E7%E3o%29=TODAS_AS_CATEGORIAS__&SSemi%E1rido_%28notifica%E7%E3o%29=TODAS_AS_CATEGORIAS__&SFaixa_de_Fronteira_%28notific%29=TODAS_AS_CATEGORIAS__&SZona_de_Fronteira_%28notific%29=TODAS_AS_CATEGORIAS__&SMunic_extrem_pobreza_%28notific%29=TODAS_AS_CATEGORIAS__&SRegi%E3o_de_resid%EAncia=TODAS_AS_CATEGORIAS__&pesqmes23=Digite+o+texto+e+ache+f%E1cil&SUF_de_resid%EAncia=TODAS_AS_CATEGORIAS__&pesqmes24=Digite+o+texto+e+ache+f%E1cil&SMunic%EDpio_de_resid%EAncia=TODAS_AS_CATEGORIAS__&pesqmes25=Digite+o+texto+e+ache+f%E1cil&SCapital_de_resid%EAncia=TODAS_AS_CATEGORIAS__&pesqmes26=Digite+o+texto+e+ache+f%E1cil&SRegi%E3o_de_Sa%FAde_%28CIR%29_de_resid=TODAS_AS_CATEGORIAS__&pesqmes27=Digite+o+texto+e+ache+f%E1cil&SMacrorreg.de_Sa%FAde_de_resid%EAnc=TODAS_AS_CATEGORIAS__&pesqmes28=Digite+o+texto+e+ache+f%E1cil&SMicrorregi%E3o_IBGE_de_resid%EAnc=TODAS_AS_CATEGORIAS__&pesqmes29=Digite+o+texto+e+ache+f%E1cil&SReg.Metropolit%2FRIDE_de_resid=TODAS_AS_CATEGORIAS__&pesqmes30=Digite+o+texto+e+ache+f%E1cil&STerrit_da_Cidadania_de_resid=TODAS_AS_CATEGORIAS__&pesqmes31=Digite+o+texto+e+ache+f%E1cil&SMesorregi%E3o_PNDR_de_resid%EAnc=TODAS_AS_CATEGORIAS__&SAmaz%F4nia_Legal_%28resid%EAncia%29=TODAS_AS_CATEGORIAS__&SSemi%E1rido_%28resid%EAncia%29=TODAS_AS_CATEGORIAS__&SFaixa_de_Fronteira_%28resid%EAnc%29=TODAS_AS_CATEGORIAS__&SZona_de_Fronteira_%28resid%EAnc%29=TODAS_AS_CATEGORIAS__&SMunic_extrem_pobreza_%28resid%29=TODAS_AS_CATEGORIAS__&SZona_Resid%EAncia=TODAS_AS_CATEGORIAS__&pesqmes38=Digite+o+texto+e+ache+f%E1cil&SFx_Et%E1ria=TODAS_AS_CATEGORIAS__&SFx_Et%E1ria_7=TODAS_AS_CATEGORIAS__&pesqmes40=Digite+o+texto+e+ache+f%E1cil&SFx_Et%E1ria_13=TODAS_AS_CATEGORIAS__&SRa%E7a=TODAS_AS_CATEGORIAS__&SSexo=TODAS_AS_CATEGORIAS__&STipo_de_entrada__=TODAS_AS_CATEGORIAS__&SInstitucionalizado=TODAS_AS_CATEGORIAS__&SPPL=TODAS_AS_CATEGORIAS__&SPop._Sit._Rua=TODAS_AS_CATEGORIAS__&SProf._sa%FAde=TODAS_AS_CATEGORIAS__&SImigrante=TODAS_AS_CATEGORIAS__&SBenefic._governo=TODAS_AS_CATEGORIAS__&SForma=TODAS_AS_CATEGORIAS__&pesqmes51=Digite+o+texto+e+ache+f%E1cil&SSe_Extrapulm.1=TODAS_AS_CATEGORIAS__&pesqmes52=Digite+o+texto+e+ache+f%E1cil&SSe_Extrapulm.2=TODAS_AS_CATEGORIAS__&SAids=TODAS_AS_CATEGORIAS__&SAlcoolismo=TODAS_AS_CATEGORIAS__&SDiabetes=TODAS_AS_CATEGORIAS__&SDoen%E7a_mental=TODAS_AS_CATEGORIAS__&SDrogas_il%EDcitas=TODAS_AS_CATEGORIAS__&STabagismo=TODAS_AS_CATEGORIAS__&SOutra_doen%E7a=TODAS_AS_CATEGORIAS__&SConfirma%E7%E3o_laboratorial=TODAS_AS_CATEGORIAS__&S1%AABac_Escarro=TODAS_AS_CATEGORIAS__&S2%AABac._Escarro=TODAS_AS_CATEGORIAS__&SCultura_Escarro__=TODAS_AS_CATEGORIAS__&STeste_r%E1pido_TB=TODAS_AS_CATEGORIAS__&STeste_sensibilidade=TODAS_AS_CATEGORIAS__&SHIV=TODAS_AS_CATEGORIAS__&SAntirretroviral=TODAS_AS_CATEGORIAS__&STDO_realizado=TODAS_AS_CATEGORIAS__&SBacilosc_2%BA_m%EAs=TODAS_AS_CATEGORIAS__&SBacilosc_6%BA_m%EAs=TODAS_AS_CATEGORIAS__&pesqmes71=Digite+o+texto+e+ache+f%E1cil&SSitua%E7%E3o_Encerra.=TODAS_AS_CATEGORIAS__&formato=table&mostre=Mostra"
        body = re.sub(r'(?<=Linha=)(.*?)(?=&|$)', urllib.parse.quote(dimension, encoding="latin-1"), body)
        body = re.sub(r'(?<=Arquivos=)(.*?)(?=&|$)', f"tubebr{year}.dbf", body)
        body = re.sub(r'(?<=SM%EAs_Notifica%E7%E3o=)(.*?)(?=&|$)', notification_month, body)
        response = requests.post(url, headers=headers, data=body)
        print(response)
        return self.clean_table(response.text)
    
    def clean_table(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        
        tbody = soup.find('tbody', attrs={'valign': 'BOTTOM'})
        thead = soup.find('thead')
        table = f'<table> {thead} {tbody} </table>'
        print(table)
        return table 
