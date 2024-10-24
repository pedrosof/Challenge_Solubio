import json
import requests

def get_watson_response(api_key, assistant_id, message):
    """
    Envia uma mensagem para o Watson Assistant e retorna a resposta.

    Args:
        api_key: Chave de API do Watson Assistant.
        assistant_id: ID do assistente.
        message: Mensagem a ser enviada.

    Returns:
        Dicionário com a resposta do Watson Assistant.
    """

    url = "https://api.us-east.assistant.watson.cloud.ibm.com/v1/assistants/{}/sessions".format(assistant_id)
    headers = {
        "Authorization": "Bearer {}".format(api_key),
        "Content-Type": "application/json"
    }

    # Criar uma nova sessão
    try:
        session_response = requests.post(url, headers=headers)
        session_response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        session_id = session_response.json().get("session_id")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao criar sessão: {e}")
        return None

    # Enviar a mensagem
    message_data = {"text": message}
    message_url = f"{url}/{session_id}/messages"
    try:
        message_response = requests.post(message_url, headers=headers, json=message_data)
        message_response.raise_for_status()
        return message_response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar mensagem: {e}")
        return None

# Exemplo de uso
api_key = "fcIaNhYjZOQA5TJghKQSvBKmtYsaoahTClTdoMeZIw3n"
assistant_id = "91b4b6f5-14f1-46f6-b06c-73d22d776a92"
message = "Olá, tudo bem?"

response = get_watson_response(api_key, assistant_id, message)

if response:
    print(response["response"]["text"])
else:
    print("Não foi possível obter uma resposta do Watson Assistant.")