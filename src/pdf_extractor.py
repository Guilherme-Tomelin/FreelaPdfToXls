import os
import re
from pdfminer.high_level import extract_text

pdf_path = "./exemplo/NFSE_38_75011_2_1.pdf"

def pdf_content_extraction(pdf_path):
    try:
        content = extract_text(pdf_path)
        return content
    except Exception as e:
        print(f"Erro ao extrair o conteúdo do PDF: {e}")
        return None


text = pdf_content_extraction(pdf_path)

nf_pattern = r'Número da NFS-e\s*(\d+)'
data_fato_gerador_pattern = r'Data Fato Gerador\s*(\d{2}/\d{2}/\d{4})'
valor_total_pattern = r'Valor Total\s*(\d{1,3}(?:\.\d{3})*(?:,\d{2}))'
issrf_pattern = r'ISSRF\s*(\d{1,3}(?:\.\d{3})*(?:,\d{2}))'
issqn_pattern = r'ISSQN\s*(\d{1,3}(?:\.\d{3})*(?:,\d{2}))'
local_pattern = r'Local de Incidência do ISS\s*\d{4}\s+(.*)'

result_nf = re.search(nf_pattern,text)
numero_nf = result_nf.group(1)

data_fato_gerador = re.search(data_fato_gerador_pattern,text)
data = data_fato_gerador.group(1)

valor_total = re.search(valor_total_pattern,text)
valor = valor_total.group(1)

issrf = re.search(issrf_pattern,text)
issrf_value = issrf.group(1)

issqn = re.search(issqn_pattern,text)
issqn_value = issqn.group(1)

local = re.search(local_pattern,text)
local_value = local.group(1)

print("Número da NFS-e:", numero_nf)
print("Data Fato Gerador:", data)
print("Valor Total:", valor)
print("ISSRF:", issrf_value)
print("ISSQN:", issqn_value)
print("Local de Incidência do ISS:", local_value)


    # data_patterns = {
    #     "nf": nf,
    #     "data_fato_gerador": data_fato_gerador,
    #     "valor_total": valor_total,
    #     "issrf": issrf,
    #     "issqn": issqn,
    #     "local": local
    # }