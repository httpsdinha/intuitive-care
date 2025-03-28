import pandas as pd
import os
from tkinter import Tk, filedialog

# Selecionar o diretório contendo os arquivos CSV
Tk().withdraw()  # Oculta a janela principal do Tkinter
directory_path = filedialog.askdirectory(title="Selecione o diretório com os arquivos CSV")

# Pré-processar cada arquivo CSV no diretório
for file_name in os.listdir(directory_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(directory_path, file_name)
        df = pd.read_csv(file_path, sep=';', decimal=',')  # Substituir ',' por '.' ao ler
        df['DATA'] = pd.to_datetime(df['DATA'], dayfirst=True).dt.strftime('%Y-%m-%d')
        output_path = os.path.join(directory_path, f"P{file_name}")
        df.to_csv(output_path, sep=';', decimal='.', index=False)  # Substituir '.' por ',' ao salvar
