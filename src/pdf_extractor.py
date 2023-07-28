import os
import PyPDF2
import re
import shutil

def read_pdf_file(file_path):
    pdf_text = ""
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            pdf_text += page.extract_text()
    return pdf_text

def extract_city(pdf_text):
    pattern = r'Local de Incidência do ISS\s*\d{4}\s+([^0-9\n]*)'
    match = re.search(pattern, pdf_text)
    if match:
        nome_cidade = match.group(1).strip()
    else:
        nome_cidade = None
    return nome_cidade

def create_cities_folder(project_dir):
    cities_folder = os.path.join(project_dir, "Cidades")
    if not os.path.exists(cities_folder):
        os.mkdir(cities_folder)
    return cities_folder

def create_city_folders(cities_folder, city_names):
    for city_name in city_names:
        city_folder = os.path.join(cities_folder, city_name)
        if not os.path.exists(city_folder):
            os.mkdir(city_folder)

def copy_pdf_to_city_folder(pdf_file, city_folder):
    file_name = os.path.basename(pdf_file)
    dest_file_path = os.path.join(city_folder, file_name)

    # Checks if the file already exists in the city folder before copying
    if not os.path.exists(dest_file_path):
        shutil.copy2(pdf_file, dest_file_path)
        print(f"Arquivo '{file_name}' copiado para a pasta '{os.path.basename(city_folder)}'.")

def main():
    folder_path = './pdfs'
    city_names = []

    #append only cities without repeats
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path) and file_name.lower().endswith('.pdf'):
            pdf_text = read_pdf_file(file_path)
            city_name = extract_city(pdf_text)

            if city_name and city_name not in city_names:
                city_names.append(city_name)

    print("Nomes de cidade encontrados:")
    print(city_names)


    project_dir = os.getcwd()  # Obtém o diretório atual do projeto
    cities_folder = create_cities_folder(project_dir)
    create_city_folders(cities_folder, city_names)

    print("Pastas criadas para cada cidade.")


    # Copiar cada PDF para a pasta da respectiva cidade
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path) and file_name.lower().endswith('.pdf'):
            pdf_text = read_pdf_file(file_path)
            city_name = extract_city(pdf_text)

            if city_name:
                city_folder = os.path.join(cities_folder, city_name)
                copy_pdf_to_city_folder(file_path, city_folder)

    print("Processo de cópia concluído.")

if __name__ == "__main__":
    main()
