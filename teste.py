from bs4 import BeautifulSoup
import requests
from colorama import Fore, Style

def get_job_description(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        description = soup.find('div', class_='item-text project-description formatted-text')
        return description.get_text() if description else None
    else:
        response.raise_for_status()

def main():
    job_url = 'https://www.99freelas.com.br/project/script-python-automatizar-mensagens-457264'
    
    try:
        description = get_job_description(job_url)

        if description:
            print(f"{Fore.GREEN}Descrição do Projeto:{Style.RESET_ALL}")
            print(description)
        else:
            print("A descrição do projeto não foi encontrada.")
    except Exception as e:
        print(f"Ocorreu o seguinte erro: {e}")

if __name__ == "__main__":
    main()








