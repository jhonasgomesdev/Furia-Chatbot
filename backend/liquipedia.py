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
        query = query.lower()

                # --- Partidas / Última partida ---
        partidas_variacoes = [
            "últimas partidas", "partidas recentes", "últimos jogos", "últimos resultados",
            "resultados recentes", "matches", "jogos", "partidas"
        ]
        partida_variacoes = [
            "última partida", "último jogo", "último resultado", "partida", "jogo", "match"
        ]

        if any(termo in query for termo in partidas_variacoes):
            return get_recent_matches(soup)

        if any(termo in query for termo in partida_variacoes):
            return get_recent_match(soup)




        # --- Coach / Jogadores ---
        table = soup.find("table", class_="wikitable wikitable-striped roster-card")
        if not table:
            return "Tabela de jogadores não encontrada."

        jogadores = []
        coach = None

        for row in table.find_all("tr"):
            name_cell = row.find("td", class_="Name")
            role_cell = row.find("td", class_="Position")

            if name_cell:
                name_div = name_cell.find("div", class_="LargeStuff")
                if name_div:
                    nome = name_div.get_text(strip=True)
                    role = role_cell.get_text(strip=True).lower() if role_cell else ""

                    if "coach" in role:
                        coach = nome
                    else:
                        jogadores.append(nome)

        if "coach" in query or "treinador" in query:
            return f"O coach atual da FURIA é: {coach}." if coach else "Coach não encontrado."
        else:
            if jogadores:
                return "Jogadores ativos da FURIA:\n" + "\n".join(f"- {j}" for j in jogadores)
            else:
                return "Nenhum jogador ativo encontrado."

    except Exception as e:
        return f"Erro inesperado: {e}"

def get_recent_matches(soup) -> str:
    try:
        rows = soup.select("tbody > tr[class^='recent-matches-bg']")

        if not rows:
            return "Não foram encontradas partidas recentes."

        partidas = []

        for row in rows[:3]:  # Limita às 3 primeiras
            cols = row.find_all("td")
            if len(cols) < 9:
                continue

            data = cols[0].get_text(strip=True)
            #hora = cols[1].get_text(strip=True)
            #tier = cols[2].get_text(strip=True)
            #tipo = cols[3].get_text(strip=True)
            evento = cols[5].get_text(strip=True)
            score = cols[7].get_text(strip=True)
            adversario = cols[8].get_text(strip=True)

            partidas.append(f"{data} — vs {adversario} | {score} ({evento})")

        return "Últimas partidas da FURIA:\n" + "\n".join(partidas)

    except Exception as e:
        return f"Erro ao obter partidas: {e}"

def get_recent_match(soup) -> str:
    try:
        rows = soup.select("tbody > tr[class^='recent-matches-bg']")

        if not rows:
            return "Não foram encontradas partidas recentes."

        partida = []

        for row in rows[:1]:
            cols = row.find_all("td")
            if len(cols) < 9:
                continue

            data = cols[0].get_text(strip=True)
            #hora = cols[1].get_text(strip=True)
            #tier = cols[2].get_text(strip=True)
            #tipo = cols[3].get_text(strip=True)
            evento = cols[5].get_text(strip=True)
            score = cols[7].get_text(strip=True)
            adversario = cols[8].get_text(strip=True)

            partida.append(f"{data} — vs {adversario} | {score} ({evento})")

        return "Última partida da FURIA:\n" + "\n".join(partida)

    except Exception as e:
        return f"Erro ao obter partidas: {e}"
