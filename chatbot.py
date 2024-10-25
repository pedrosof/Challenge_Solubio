import os
import uuid
from google.cloud.dialogflowcx_v3beta1.services.agents import AgentsClient
from google.cloud.dialogflowcx_v3beta1.types import session
from google.cloud.dialogflowcx_v3beta1 import SessionsClient

# Defina o caminho para o arquivo JSON das credenciais
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/pedrosof/Documents/FIAP/Trabalhos/Challenge_Solubio/solubio-chatbot-99cf215dab01.json"

def start_chatbot():
    # Configurações do agente
    project_id = "solubio-chatbot"
    location_id = "us-east1"
    agent_id = "abd45053-6c47-4015-ab08-111ec3bd0707"
    agent = f"projects/{project_id}/locations/{location_id}/agents/{agent_id}"

    # Configuração da sessão
    session_id = str(uuid.uuid4())
    language_code = "en-us"

    print("Chatbot iniciado! Digite sua mensagem ou 'sair' para encerrar.")

    # Loop de interação com o usuário
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            print("Encerrando o chatbot. Até logo!")
            break

        # Chama a função para detectar a intenção com o texto do usuário
        response_text = detect_intent_text(agent, session_id, user_input, language_code)
        print(f"Chatbot: {response_text}")

def detect_intent_text(agent, session_id, text, language_code):
    """Envia uma mensagem e obtém a resposta do Dialogflow."""
    
    session_path = f"{agent}/sessions/{session_id}"
    client_options = None
    agent_components = AgentsClient.parse_agent_path(agent)
    location_id = agent_components["location"]
    
    if location_id != "global":
        api_endpoint = f"{location_id}-dialogflow.googleapis.com:443"
        client_options = {"api_endpoint": api_endpoint}
    
    # Inicializa o cliente de sessão com as opções definidas
    session_client = SessionsClient(client_options=client_options)

    # Prepara a entrada e envia a solicitação
    text_input = session.TextInput(text=text)
    query_input = session.QueryInput(text=text_input, language_code=language_code)
    request = session.DetectIntentRequest(session=session_path, query_input=query_input)
    
    response = session_client.detect_intent(request=request)
    response_messages = [
        " ".join(msg.text.text) for msg in response.query_result.response_messages
    ]
    
    return " ".join(response_messages)

# Executa o chatbot interativo
if __name__ == "__main__":
    start_chatbot()