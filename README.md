# Projeto(FREELA): Extrator de Dados de PDF e Criador de Planilha

## 🇧🇷 Descrição

Este projeto fornece um conjunto de classes e funções para extrair informações de arquivos PDFs com um formato específico e criar uma planilha (arquivo Excel) contendo os dados extraídos. O script busca por padrões específicos no conteúdo dos PDFs usando expressões regulares para extrair informações relevantes.

## Pré-requisitos

Antes de executar o script, certifique-se de que você tenha o seguinte:

- Python 3.x
- Bibliotecas Python necessárias: `os`, `re`, `pandas`, `PyPDF2`

Instale as bibliotecas necessárias usando o `pip`:

```
pip install pandas PyPDF2
```


## Uso

1. Coloque os arquivos PDF que deseja processar em uma pasta chamada `pdfs`.

2. Execute a função `main()` no script.

3. O script irá extrair informações dos arquivos PDF válidos encontrados na pasta `pdfs`.

4. Uma planilha chamada `dados_pdfs.xlsx` será criada na pasta `output`. Este arquivo conterá as informações extraídas dos PDFs.

# Project(FREELA): PDF Data Extractor and Spreadsheet Creator


---


## 🇺🇸 Description

This project provides a set of classes and functions to extract information from PDF files with a specific format and create a spreadsheet (Excel file) containing the extracted data. The script looks for specific patterns in the PDF content using regular expressions to extract relevant information.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x
- Required Python libraries: `os`, `re`, `pandas`, `PyPDF2`

Install the required libraries using `pip`:

```
pip install pandas PyPDF2
```

## Usage

1. Place the PDF files you want to process in a folder called `pdfs`.

2. Execute the `main()` function in the script.

3. The script will extract information from the valid PDF files found in the `pdfs` folder.

4. A spreadsheet named `dados_pdfs.xlsx` will be created in the `output` folder. This file will contain the information extracted from the PDFs.
