"""

Este arquivo serve para ler algum arquivo individualmente, 
utilizando PyPDF2, e ver seu conteúdo convertido em String no console.

This file serves to read a file individually, 
using PyPDF2, and see its content converted into String in the console.

"""


import os
import PyPDF2

def read_pdf_file(file_path):
    pdf_text = ""
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            pdf_text += page.extract_text()
    return pdf_text

def main():
    #dir pdfs
    folder_path = '../pdfs'
    #pdfname
    file_name = 'PDFname.pdf'         

    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(file_path):
        pdf_text = read_pdf_file(file_path)
        print(pdf_text)
    else:
        print(f"Arquivo '{file_name}' não encontrado na pasta '{folder_path}'.")

if __name__ == "__main__":
    main()