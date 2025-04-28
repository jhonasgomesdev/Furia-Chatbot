import google.generativeai as genai

genai.configure(api_key="AIzaSyDbV_5-mALKfTJGkAjn8XUGLe8obotBJpc")

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Contexto fixo para o Gemini focar na FURIA
contexto = """
    Você é um torcedor fanático e especialista em FURIA eSports.
    Responda apenas sobre a FURIA e seus times de CS2, Valorant e outros.
    Se não souber alguma informação, responda: "Não tenho certeza no momento.".
    """

def get_bot_response(user_message: str) -> str:
    user_message = user_message.lower()
    response = model.generate_content([
        {"role": "user", "parts": [{"text": contexto}]},
        {"role": "user", "parts": [{"text": user_message}]}
    ])
    return response.text

# Exemplo de pergunta
resposta = get_bot_response("Quando é o próximo jogo?")
print(resposta)
