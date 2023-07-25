import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
import openai

# Configuração da API do OpenAI GPT (Insira sua chave de API aqui)
openai.api_key = "gerar nova chave"

def get_job_description(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        description = soup.find('div', class_='item-text project-description formatted-text')
        return description.get_text() if description else None
    else:
        response.raise_for_status()

def main():
    job_url = 'https://www.99freelas.com.br/project/estrategia-de-carteira-de-acoes-em-python-457414?fs=t'
    
    try:
        descricao_projeto = get_job_description(job_url)

        if descricao_projeto:
            print(f"{Fore.GREEN}Descrição do Projeto:{Style.RESET_ALL}")
            print(descricao_projeto)
        else:
            print("A descrição do projeto não foi encontrada.")
    except Exception as e:
        print(f"Ocorreu o seguinte erro ao obter a descrição do projeto: {e}")

    # Usar a descrição do projeto como input para o GPT
    if descricao_projeto:
        try:
            print(f"{Fore.GREEN}Iniciando chat com GPT...{Style.RESET_ALL}")
            resposta_gpt = openai.Completion.create(
                engine="text-davinci-002",
                prompt=descricao_projeto,
                temperature=0.7,
                max_tokens=150
            )
            resposta_gpt = resposta_gpt['choices'][0]['text'].strip()
            print(f"{Fore.GREEN}Resposta do GPT:{Style.RESET_ALL}")
            print(resposta_gpt)
        except openai.error.APIError as api_err:
            print(f"Erro ao fazer solicitação à API do GPT: {api_err}")
        except Exception as e:
            print(f"Erro inesperado ao interagir com o GPT: {e}")

if __name__ == "__main__":
    main()

