#transformação de dados

import zipfile
import os
from urllib.parse import urljoin  
import re
import tkinter as tk
from tkinter import filedialog
import pandas as pd
from pdfminer.high_level import extract_text


def extrair_tabela_pdf(pdf_path):
    print("Processando PDF")
    try:
        texto = extract_text(pdf_path)
        linhas = [linha.strip() for linha in texto.split('\n') if linha.strip()]
        
        dados = []
        for linha in linhas: 
            if re.match(r'^\d{4}\s+', linha):
                partes = re.split(r'\s{2,}', linha)
                dados.append(partes[:5])
                
        if not dados: 
            raise Exception("Nenhuma tabela encontrada")
        
        colunas = ['Código', 'Descrição', 'Tipo', 'Porte', 'Data de Inclusão']
        return pd.DataFrame(dados, columns=colunas)
    
    except Exception as e:
        print(f"Erro ao processar dados do PDF: {e}")
        return None

def substituir_abreviacoes(df):
    print("Substituindo abreviações")
    df["OD/AMB"] = df ["OD/AMB"].replace({
        "OD": "Odontologia",
        "AMB": "Ambulatorial"
    })
    return df

def salvar_e_compactar(df, nome_arquivo, diretorio):
    try:
        csv_path = os.path.join(diretorio, f"{nome_arquivo}.csv")
        zip_path = os.path.join(diretorio, f"{nome_arquivo}.zip")
        
        print("Salvando {csv_path}")
        df.to_csv(csv_path, index=False, encoding='utf-8')
        
        print("Compactando {zip_path}")
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.write(csv_path, os.path.basename(csv_path))
        os.remove(csv_path)
        print("Arquivo salvo e compactado com sucesso")
        return True
    except Exception as e:
        print("Erro ao salvar e compactar arquivo: {e}")
        return False

def extrair_pdfs_do_zip(zip_path, diretorio_temp):
    print("Extraindo arquivos do ZIP")
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(diretorio_temp)
        pdf_files = [os.path.join(diretorio_temp, f) for f in os.listdir(diretorio_temp) if f.endswith('.pdf')]
        if not pdf_files:
            raise Exception("Nenhum arquivo PDF encontrado no ZIP")
        return pdf_files
    except Exception as e:
        print(f"Erro ao extrair arquivos do ZIP: {e}")
        return []

def main():
    try:
        root = tk.Tk()
        root.withdraw()
        diretorio = filedialog.askdirectory(title="Selecione a pasta para salvar os arquivos")
        if not diretorio:
            raise Exception("Nenhum diretório selecionado")
        
        zip_path = filedialog.askopenfilename(
            title="Selecione o arquivo ZIP contendo os PDFs",
            filetypes=[("ZIP files", "*.zip")]
        )
        if not zip_path:
            raise Exception("Nenhum arquivo ZIP selecionado")
        
        diretorio_temp = os.path.join(diretorio, "temp_extracao")
        os.makedirs(diretorio_temp, exist_ok=True)
        
        pdf_files = extrair_pdfs_do_zip(zip_path, diretorio_temp)
        if not pdf_files:
            raise Exception("Erro ao extrair PDFs do ZIP")
        
        dfs = []
        for pdf_path in pdf_files:
            df = extrair_tabela_pdf(pdf_path)
            if df is not None:
                dfs.append(df)
        
        if not dfs:
            raise Exception("Nenhuma tabela válida foi extraída dos PDFs")
        
        df_final = pd.concat(dfs, ignore_index=True)
        df_final = substituir_abreviacoes(df_final)
        
        nome_arquivo = input("Digite o seu Nome: ").strip()
        if not nome_arquivo:
            nome_arquivo = "Tabela_ANS"
        else:
            nome_arquivo = f"Teste_{nome_arquivo}"
        
        if not salvar_e_compactar(df_final, nome_arquivo, diretorio):
            raise Exception("Erro ao salvar e compactar arquivo")
        
        # Limpeza do diretório temporário
        for f in os.listdir(diretorio_temp):
            os.remove(os.path.join(diretorio_temp, f))
        os.rmdir(diretorio_temp)
        
    except Exception as e:
        print(f"Erro: {e}")
        print("Verifique o arquivo ZIP, os PDFs e a pasta de destino")

main()