import os
import re
import pandas as pd
from pdfminer.high_level import extract_text

class PDFExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_text(self):
        try:
            return extract_text(self.pdf_path)
        except Exception as e:
            print(f"Erro ao extrair o conteúdo do PDF: {e}")
            return None

class InformationExtractor:
    def __init__(self, text):
        self.text = text

    def _search_pattern(self, pattern):
        result = re.search(pattern, self.text)
        return result.group(1) if result else None

    def extract_info(self):
        patterns = {
            "Número da NFS-e": r'Número da NFS-e\s*(\d+)',
            "Data Fato Gerador": r'Data Fato Gerador\s*(\d{2}/\d{2}/\d{4})',
            "Valor Total": r'Valor Total\s*(\d{1,3}(?:\.\d{3})*(?:,\d{2}))',
            "ISSRF": r'ISSRF\s*(\d{1,3}(?:\.\d{3})*(?:,\d{2}))',
            "ISSQN": r'ISSQN\s*(\d{1,3}(?:\.\d{3})*(?:,\d{2}))',
            "Local de Incidência do ISS": r'Local de Incidência do ISS\s*\d{4}\s+(.*)',
        }

        return {field: self._search_pattern(pattern) for field, pattern in patterns.items()}

class SpreadsheetCreator:
    def __init__(self, sheet_data, output_file):
        self.sheet_data = sheet_data
        self.output_file = output_file

    def create_spreadsheet(self):
        fields = ["Número da NFS-e", "Data Fato Gerador", "Valor Total", "ISSRF", "ISSQN", "Local de Incidência do ISS"]

        df = pd.DataFrame([self.sheet_data], columns=fields)

        output_folder = os.path.join(".", "output")
        os.makedirs(output_folder, exist_ok=True)

        output_path = os.path.join(output_folder, self.output_file)
        df.to_excel(output_path, index=False)

def main():
    pdf_path = "./exemplo/NFSE_38_75011_2_1.pdf"

    pdf_extractor = PDFExtractor(pdf_path)
    text = pdf_extractor.extract_text()

    if text:
        info_extractor = InformationExtractor(text)
        data_patterns = info_extractor.extract_info()

        spreadsheet_creator = SpreadsheetCreator(data_patterns, "teste.xlsx")
        spreadsheet_creator.create_spreadsheet()

        print("Dados extraídos e planilha criada com sucesso.")
    else:
        print("Não foi possível extrair o texto do PDF.")

if __name__ == "__main__":
    main()
