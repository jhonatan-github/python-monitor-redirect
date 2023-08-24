import requests
import sys

def check_redirect(url):
    try:
        # Faz uma solicitação HEAD para a URL com redirecionamentos desativados
        response = requests.head(url, allow_redirects=False)
        
        # Verifica o código de status da resposta
        if response.status_code == 301:
            print(f"+ {url} :: {response.status_code}")
        else:
            print(f"- Não está sendo redirecionado: {url} :: {response.status_code}")
            
            # Registra a URL e o código de status no arquivo "no_redirects.txt"
            with open("no_redirects.txt", "a") as no_redirect:
                no_redirect.write(f"{url} :: {response.status_code}\n")
    except requests.exceptions.RequestException as e:
        print(f"! Erro {url} :: {e}")

def load_urls(urlfile):
    clean_urls = []
    with open(urlfile) as f:
        urllist = f.readlines()
        
    # Limpa cada URL removendo espaços em branco e linhas vazias
    clean_urls = [url.strip() for url in urllist if url.strip()]
    return clean_urls

def main():
    args = sys.argv
    if len(args) != 2:
        print("! Erro: Argumentos insuficientes.\n\nUso: python check301.py urls.txt")
    else:
        try:
            url_file = args[1]
            
            # Carrega as URLs do arquivo
            urls = load_urls(url_file)
            
            # Verifica redirecionamentos para cada URL
            for url in urls:
                check_redirect(url)
        except Exception as e:
            print(f"Algo deu errado: {e}")

if __name__ == "__main__":
    main()
