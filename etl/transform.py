from bs4 import BeautifulSoup
from lxml import etree
import re

from database.enums import DimensionEnum

class Transformer():
    def parse(self, data):
        result = []
        
        fixed_html = self.fix_html(data["raw"])
        soup = BeautifulSoup(fixed_html, 'html.parser')
       
        tbody = soup.find('tbody', attrs={'valign': 'BOTTOM'})
        thead = soup.find('thead')

        headers = thead.find_all('th')
        first_column_name = headers[0].get_text(strip=True)
        rows = tbody.find_all('tr')
        
        for row in rows:
            cells = row.find_all('td')
            if len(cells) < 2:   
                continue

            first_column_value = cells[0].get_text(strip=True)
            
            if "TOTAL" in first_column_value.upper():
                continue

            second_column_value = cells[1].get_text(strip=True)
            
            first_column_value, second_column_value = self.apply_specific_transformations(first_column_name, first_column_value, second_column_value)
            
            formatted_first_column_name = next(entry.value[0] for entry in DimensionEnum if entry.value[3] == first_column_name)
            
            result.append({
                "metric": "confirmed_cases",
                "value": int(float(second_column_value)),
                "dimensions": {
                    "ano": int(data["year"]) - 1,
                    "mes": int(data["month"]) - 1,
                    formatted_first_column_name: first_column_value 
                }
            })

        return result
    
    def fix_html(self, html):
        parser = etree.HTMLParser(recover=True)
        tree = etree.fromstring(html, parser)
        return etree.tostring(tree, pretty_print=True, method="html").decode()
    
    def apply_specific_transformations(self, first_column_name, first_column_value, second_column_value):
        if first_column_name == "UF de notificação" or first_column_name == "Município de notificação" or first_column_name == "Capital de notificação" or first_column_name == "Região de Saúde (CIR) de notif" or first_column_name == "Macrorreg.de Saúde de notific" or first_column_name == "Microrregião IBGE de notific":
           first_column_value = re.sub(r'\d+', '', first_column_value).strip()
        if first_column_name == "Região de notificação":
            first_column_value = re.sub(r'\d+', '', first_column_value).strip().split(" ")[1]
        return first_column_value, second_column_value
           
