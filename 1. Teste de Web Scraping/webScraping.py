#web scraping em python

import requests
from bs4 import BeautifulSoup
import zipfile
import os
import time
from urllib.parse import urljoin  
import re

def baixar_anexos():
    try:
        #acesso ao site
        url_ans = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
        
        #simulação de navegador
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        print("Acessando a página")
        
        resposta = requests.get(url_ans, headers=headers)
        
        #verifica se a pagina carregou
        if resposta.status_code != 200:
            raise Exception("Erro ao acessar a página da ANS: ", resposta.status_code)
        
        #pegando links 
        print("Pegando links dos anexos")
        soup = BeautifulSoup(resposta.text, 'html.parser')
        links_pdf = []
        
        padroes_anexo = ['anexo i', 'anexo ii', 'anexo1', 'anexo2', 'anexo I', 'anexo II', 'Anexo I', 'Anexo II', "Anexo I.pdf", "Anexo II.pdf", 'Anexo_I', 'Anexo_II']
        
        for link in soup.find_all('a', href=True):
            href = link['href'].lower()
            texto = link.get_text(strip=True).lower()
            
             # Verifica se é PDF e contém referência aos anexos
            if (any(padrao in href or padrao in texto for padrao in padroes_anexo) 
                and href.endswith('.pdf')):
                
                # Corrige links relativos e remove possíveis duplicatas
                full_link = urljoin(url_ans, link['href'])
                if full_link not in links_pdf:
                    links_pdf.append(full_link)
        
        if not links_pdf:
            raise Exception ("Nenhum link encontrado")
        
        #baixar pdf
        print(f'Encontrados {len(links_pdf)} arquivos. Baixando...')
        arquivos_baixados = []
        
        for link in links_pdf:
            nome_arquivo = link.split('/')[-1]
            print(f'Baixando {nome_arquivo}')
            
            #tentativas de download caso falhe
            for tentativa in range(3):
                try: 
                    resposta_pdf = requests.get(link, headers=headers, timeout=10)
                    resposta_pdf.raise_for_status()
                    
                    with open(nome_arquivo, 'wb') as f:
                        f.write(resposta_pdf.content)
                    
                    arquivos_baixados.append(nome_arquivo)
                    break
                except Exception as e:
                    if tentativa == 2:
                        print(f"Falha ao baixar {nome_arquivo}: {e}")
                    time.sleep(2) #espera antes de tentar novamente

        #compactar em zip após baixar todos os arquivos
        if arquivos_baixados:
            nome_zip = "Anexos_ANS.zip"
            print(f"Compactando arquivos em {nome_zip}...")
            
            with zipfile.ZipFile(nome_zip, 'w') as zipf:
                for arquivo in arquivos_baixados:
                    zipf.write(arquivo)
            #limpar temporarios
            for arquivo in arquivos_baixados:
                os.remove(arquivo)
            print("Concluído! Arquivo ZIP criado com sucesso.")
        else:
            print("Nenhum arquivo foi baixado.")
    except Exception as e:
        print(f"ERRO: {e}")
        print("Verifique a conexão ou o site da ANS.")



baixar_anexos()