"""

Este arquivo serve para ler algum arquivo individualmente, 
utilizando pdfminer, e ver seu conteúdo convertido em String no console.

This file serves to read a file individually, 
using pdfminer, and see its content converted into String in the console.


pip install pdfminer.six
"""

# import os
# from pdfminer.high_level import extract_text



# def read_pdf_file(file_path):
#     pdf_text = extract_text(file_path)
#     return pdf_text

# def main():
#     #dir pdfs
#     folder_path = '../pdfs'
#     #pdfname
#     file_name = 'PDFname.pdf'           

#     file_path = os.path.join(folder_path, file_name)

#     if os.path.exists(file_path):
#         pdf_text = read_pdf_file(file_path)
#         print(pdf_text)
#     else:
#         print(f"Arquivo '{file_name}' não encontrado na pasta '{folder_path}'.")

# if __name__ == "__main__":
#     main()