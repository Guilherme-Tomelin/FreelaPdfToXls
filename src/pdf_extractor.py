import os
import re
import pandas as pd
from pdfminer.high_level import extract_text
import PyPDF2

class PDFExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_text(self):
        """
        Extracts text content from a PDF file.

        Returns:
            str or None: The extracted text content from the PDF, or None if an error occurs.
        """
        try:
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
            return text
        except Exception as e:
            print(f"Erro ao extrair o conteúdo do PDF: {e}")
            return None

class InformationExtractor:
    def __init__(self, text):
        self.text = text

    def _search_pattern(self, pattern):
        """
        Search for a specific regular expression pattern in the given text.

        Args:
            pattern (str): Regular expression pattern to search for.

        Returns:
            str or None: The extracted pattern match or None if not found.
        """
        result = re.search(pattern, self.text)
        return result.group(1) if result else None

    def extract_info(self):
        """
        Extracts information from a text using regular expression patterns.

        Returns:
            dict: A dictionary containing extracted information with keys as the information names.
                If no information is found, an empty dictionary is returned.
        """


        keywords = ["Encruzilhada", "Ivoti", "OutraCidade", "MaisUmaCidade"]

        patterns = {
            "Número da NFS-e": r'Número da NFS-e\s*(\d+)',
            "Data Fato Gerador": r'Data/Hora Emissão\s*(\d{2}/\d{2}/\d{4})',
            "Valor Total": r'Valor Total\s*(\d{1,3}(?:\.\d{3})*(?:,\d{2}))',
            "ISSRF": r'ISSRF\s*(\d{1,3}(?:\.\d{3})*(?:,\d{2}))',
            "ISSQN": r'ISSQN\s*(\d{1,3}(?:\.\d{3})*(?:,\d{2}))',
            "Local de Incidência do ISS": r'Local de Incidência do ISS\s*\d{4}\s+([^0-9\n]*)',
            "Local de Incidência do ISS (opção 2)": r'Local de Incidência do ISS\s+(\d+)\s+.*\n(.+)',
            
        }

        data = {}
        for field, pattern in patterns.items():
            match = re.search(pattern, self.text)
            if match:
                data[field] = match.group(1).strip()
            else:
                data[field] = None

        return data

class SpreadsheetCreator:
    def __init__(self, sheet_data_list, output_file):
        self.sheet_data_list = sheet_data_list
        self.output_file = output_file

    def create_spreadsheet(self):

        """
        Creates a spreadsheet (Excel file) from the provided data.

        The spreadsheet will contain the extracted information.

        Returns:
            None
        """

        fields = ["Número da NFS-e", "Data Fato Gerador", "Valor Total", "ISSRF", "ISSQN", "Local de Incidência do ISS"]

        output_folder = os.path.join(".", "output")
        os.makedirs(output_folder, exist_ok=True)

        output_path = os.path.join(output_folder, self.output_file)

        df = pd.DataFrame(self.sheet_data_list, columns=fields)
        df.to_excel(output_path, index=False)

def get_valid_pdfs(pdf_folder_path):

    """
    Get a list of valid PDF files in the specified folder.

    PDF files are considered valid if they match a specific name pattern.

    Args:
        pdf_folder_path (str): The folder path containing the PDF files.

    Returns:
        list: A list of valid PDF file paths.
    """

    pdf_name_pattern = r'NFSE_(\d+)_(\d+)_(\d+)\.pdf'
    valid_pdfs = []
    for filename in os.listdir(pdf_folder_path):
        match = re.match(pdf_name_pattern, filename)
        if match:
            valid_pdfs.append(os.path.join(pdf_folder_path, filename))
    return valid_pdfs

def main():

    """
    Main function to extract information from PDF files and create a spreadsheet.

    This function uses the PDFExtractor and InformationExtractor classes to extract information
    from each valid PDF file found in the specified folder. The extracted data is then used to create
    a spreadsheet using the SpreadsheetCreator class.
    """

    pdfs_folder = "./pdfs"
    valid_pdfs = get_valid_pdfs(pdfs_folder)

    pdfs_path_list = [os.path.join(pdfs_folder, filename) for filename in os.listdir(pdfs_folder)]

    all_data_patterns = []
    for pdf_path in pdfs_path_list:
        pdf_extractor = PDFExtractor(pdf_path)
        text = pdf_extractor.extract_text()

        if text:
            info_extractor = InformationExtractor(text)
            data_patterns = info_extractor.extract_info()
            all_data_patterns.append(data_patterns)
        else:
            print(f"Não foi possível extrair o texto do PDF: {pdf_path}")

    if all_data_patterns:
        spreadsheet_creator = SpreadsheetCreator(all_data_patterns, "dados_pdfs.xlsx")
        spreadsheet_creator.create_spreadsheet()
        print("Dados extraídos de todos os PDFs e planilha consolidada criada com sucesso.")
    else:
        print("Não foi possível extrair dados de nenhum PDF.")

if __name__ == "__main__":
    main()