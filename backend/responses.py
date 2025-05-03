import google.generativeai as genai
from liquipedia import consultar_liquipedia

genai.configure(api_key="AIzaSyDbV_5-mALKfTJGkAjn8XUGLe8obotBJpc")

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

contexto = """
Você é um especialista na FURIA eSports.
Comece a frase com Eae, Guerreiro.
Você é empolgado ao responder o usuário, e fala o nick dos jogadores juntamente com o nome deles, o nick do Danil é molodoy.
Não utilize "*" na resposta.
arT Andrei Andrei Piovezan não está na fúria.
Não escreva tudo em letra maiúscula.
Não exagere no que escrever.
Mantenha o conteúdo que recebeu.
Não substitua palavras por emojis, mas utilize emojis para melhorar o texto.
Formate as datas para o padrão do brasil dd/MM/aaaa.
"""

def traduzir_com_gemini(texto: str) -> str:
    prompt = f"{contexto}\n\nAgora traduza e estilize o texto abaixo para português mantendo os fatos corretos:\n\n{texto}"
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print("Erro na tradução com Gemini:", e)
        return texto  # fallback: retorna o original em inglês

def is_query_valid(query: str) -> bool:
    palavras_chave = [
        "furia", "elenco", "roster", "jogadores", "lineup", "escalação",
        "coach", "treinador", "player", "membros", "fúria", "jogador" 
    ]
    query = query.lower()
    return any(p in query for p in palavras_chave)


def get_bot_response(user_message: str) -> str:
    if not is_query_valid(user_message):
        return "Furioso, essa pergunta não parece estar relacionada ao time FURIA! Tente perguntar sobre os jogadores, técnico ou escalação. 🔥"

    resposta_liquipedia = consultar_liquipedia(user_message)

    if not resposta_liquipedia or resposta_liquipedia.strip() == "":
        return "Não encontrei informações sobre isso na Liquipedia."

    return traduzir_com_gemini(resposta_liquipedia)

