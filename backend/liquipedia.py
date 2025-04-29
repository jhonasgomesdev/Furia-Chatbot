from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def consultar_liquipedia(query: str) -> str:
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.get("https://liquipedia.net/counterstrike/FURIA")
        html = driver.page_source
        driver.quit()

        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table", class_="wikitable wikitable-striped roster-card")
        if not table:
            return "Tabela de jogadores não encontrada."

        jogadores = []
        for row in table.find_all("tr"):
            name_cell = row.find("td", class_="Name")
            if name_cell:
                name_div = name_cell.find("div", class_="LargeStuff")
                if name_div:
                    jogador = name_div.get_text(strip=True)
                    jogadores.append(f"- {jogador}")

        if jogadores:
            return "Jogadores ativos da FURIA:\n" + "\n".join(jogadores)
        else:
            return "Nenhum jogador ativo encontrado."

    except Exception as e:
        return f"Erro inesperado: {e}"
