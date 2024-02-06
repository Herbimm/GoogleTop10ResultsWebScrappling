import requests
from bs4 import BeautifulSoup


def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        #print(response.text)
        return response.text
    except requests.RequestException as e:
        print("Erro durante a requisição:", e)
        return None


def parse_search_results(html):
    results = []
    soup = BeautifulSoup(html, "html.parser")
    #print(soup.prettify())
    #search_results = soup.find_all("div")[:5]  # Pegar os 5 primeiros resultados
    search_results = soup.find_all("div")  # Pegar os 5 primeiros resultados
    print("Resultados Quantidade: {}".format(len(search_results)))
    for title in soup.find_all('h3'):
        print(title.div.string)
        results.append(title.div.string)

    return results


def main():
    page = 1
    query = input("Digite o termo de pesquisa: ")
    html = google_search(query)

    if html:
        print(f"\nResultados da pesquisa para '{query}':\n")
        search_results = parse_search_results(html)
        query = input("Pagina ?")
    else:
        print("Nenhum resultado encontrado.")


if __name__ == "__main__":
    main()
