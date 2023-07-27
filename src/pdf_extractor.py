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
data_fato_gerador_pattern = r'Data Fato Gerador\s*\d{2}/\d{2}/\d{4}'
valor_total_pattern = r'Valor Total\s*(\d{1,3}(?:\.\d{3})*(?:,\d{2}))'
issrf_pattern = r'ISSRF\s*(\d{1,3}(?:\.\d{3})*(?:,\d{2}))'
issqn_pattern = r'ISSQN\s*(\d{1,3}(?:\.\d{3})*(?:,\d{2}))'
local_pattern = r'Local de Incidência do ISS\s*\d{4}\s+(.*)'

result = re.search(nf_pattern,text)
numero_nfs = result.group(1)
print(result)
print()
print(numero_nfs)


    # data_patterns = {
    #     "nf": nf,
    #     "data_fato_gerador": data_fato_gerador,
    #     "valor_total": valor_total,
    #     "issrf": issrf,
    #     "issqn": issqn,
    #     "local": local
    # }