import zipfile
import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import pdfplumber

#extrai a tabela do pdf
def extrair_tabela_pdf(pdf_path):
    print("Processando PDF")
    todas_linhas = []
    cabecalho = None
    
    #abre o pdf e extrai o texto
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if "PROCEDIMENTO" in text and "VIGÊNCIA" in text:
                for tabela in page.extract_tables():
                    if len(tabela) > 1:
                        if "PROCEDIMENTO" in str(tabela[0][0]):
                            cabecalho = tabela[0]
                            for linha in tabela[1:]:
                                if linha[0] and linha[0].strip():
                                    todas_linhas.append(linha)
    if not cabecalho:
        raise ValueError("Cabeçalho da tabela não encontrado no PDF")
    
    #cria o dataframe com os dados 
    df = pd.DataFrame(todas_linhas, columns=cabecalho)
    
    #adição das colunas relevantes
    colunas_relevantes = [
        'PROCEDIMENTO', 'RN', 'VIGÊNCIA', 'OD', 'AMB', 'HCO', 'HSO', 
        'REF', 'PAC', 'DUT', 'SUBGRUPO', 'GRUPO', 'CAPÍTULO'
    ]
    df = df[[col for col in colunas_relevantes if col in df.columns]]
    
    return df

#substitui as abreviações
def substituir_abreviacoes(df):
    print("Substituindo abreviações")
    
    df = df.replace({
        'OD': 'Odontológica',
        'AMB': 'Ambulatorial',
        'HCO': 'Hospitalar Com Obstetrícia',
        'HSO': 'Hospitalar Sem Obstetrícia',
        'REF': 'Referência',
        'PAC': 'Procedimento de Alta Complexidade',
        'DUT': 'Diretriz de Utilização'
    })
    
    return df

#salva em .csv e compacta o arquivo em zip
def salvar_e_compactar(df, nome_arquivo, diretorio):
    try:
        #define o caminho do zip
        csv_path = os.path.join(diretorio, f"{nome_arquivo}.csv")
        zip_path = os.path.join(diretorio, f"{nome_arquivo}.zip")
        
        print(f"Salvando {csv_path}")
        df.to_csv(csv_path, index=False, encoding='utf-8')
        
        print(f"Compactando {zip_path}")
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.write(csv_path, os.path.basename(csv_path))
        os.remove(csv_path)
        print("Arquivo salvo e compactado com sucesso")
        return zip_path
    except Exception as e:
        print(f"Erro ao salvar e compactar arquivo: {e}")
        return None
    
#processar o arquivo
def processar_anexo1(pdf_path, nome_usuario, diretorio_saida = 'output' ):
    try:
        #diretorio de saida
        if not os.path.exists(diretorio_saida):
            os.makedirs(diretorio_saida)
        
        #extrai a tabela do pdf com a função
        df = extrair_tabela_pdf(pdf_path)
        #substitui as abreviações com a função
        df = substituir_abreviacoes(df)
        
        #define o nome do arquivo final
        nome_arquivo = f"Teste_{nome_usuario}"
        #salva e compacta o arquivo com a função
        zip_path = salvar_e_compactar(df, nome_arquivo, diretorio_saida)
        
        if zip_path:
            print(f"Arquivo salvo e compactado em: {zip_path}")
        else:
            print("Erro ao salvar e compactar o arquivo")
        
        return zip_path
    except Exception as e:
        print(f"Erro ao processar Anexo I: {e}")
        return None

def main():
    #janela oculta com o tkinter para selecionar o arquivo
    root = tk.Tk()
    root.withdraw()
    print("Selecione o arquivo ZIP contendo o PDF.")
    zip_path = filedialog.askopenfilename(
        title="Selecione o arquivo ZIP",
        filetypes=[("Arquivos ZIP", "*.zip")]
    )
    
    if not zip_path:
        print("Nenhum arquivo selecionado. Encerrando o programa.")
        exit(1)
    
    #extrai o o primeiro pdf do zip
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        pdf_files = [f for f in zip_ref.namelist() if f.endswith('.pdf')]
        if not pdf_files:
            print("Nenhum arquivo PDF encontrado no ZIP.")
            exit(1)
        zip_ref.extract(pdf_files[0])
        pdf_path = pdf_files[0]
    #processa o anexo1 com o nome do usuario
    nome_usuario = input("Digite o nome do usuário: ")
    processar_anexo1(pdf_path, nome_usuario)

main()