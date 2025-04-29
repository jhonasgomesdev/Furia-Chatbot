import google.generativeai as genai
from liquipedia import consultar_liquipedia

genai.configure(api_key="AIzaSyDbV_5-mALKfTJGkAjn8XUGLe8obotBJpc")

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

contexto = """
Você é um torcedor fanático e especialista em FURIA eSports.
Você é super empolgado, e dinâmico em sua fala. Sempre retrata a pessoa como Guerreiro ou Furioso.
Não utilize "*" na resposta, apenas emojis.
Não escreva tudo em letra maiúscula.
"""

def traduzir_com_gemini(texto: str) -> str:
    prompt = f"{contexto}\n\nAgora traduza e estilize o texto abaixo para português mantendo os fatos corretos:\n\n{texto}"
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print("Erro na tradução com Gemini:", e)
        return texto  # fallback: retorna o original em inglês

def get_bot_response(user_message: str) -> str:
    resposta_liquipedia = consultar_liquipedia(user_message)

    if not resposta_liquipedia or resposta_liquipedia.strip() == "":
        return "Não encontrei informações sobre isso na Liquipedia."

    return traduzir_com_gemini(resposta_liquipedia)
