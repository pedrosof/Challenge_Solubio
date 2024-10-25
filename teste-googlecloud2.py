import os
import uuid
from google.cloud.dialogflowcx_v3beta1.services.agents import AgentsClient
from google.cloud.dialogflowcx_v3beta1.types import session
from google.cloud.dialogflowcx_v3beta1 import SessionsClient

# Defina o caminho para o arquivo JSON das credenciais
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/pedrosof/Documents/FIAP/Trabalhos/Challenge_Solubio/solubio-chatbot-99cf215dab01.json"

def run_sample():
    # Substitua estes valores conforme necessário
    project_id = "solubio-chatbot"
    location_id = "us-central1"
    agent_id = "00297d11-cd38-4536-bf51-7be2cbc5f050"
    agent = f"projects/{project_id}/locations/{location_id}/agents/{agent_id}"

    # Configuração da sessão e entrada de texto
    session_id = str(uuid.uuid4())  # Gera um UUID único para a sessão
    texts = ["Hello"]  # Altere para outros inputs conforme necessário
    language_code = "en-us"

    # Chamada da função para detectar intenções
    detect_intent_texts(agent, session_id, texts, language_code)

def detect_intent_texts(agent, session_id, texts, language_code):
    """Executa a detecção de intenções a partir de uma lista de textos."""
    
    # Cria a sessão com o caminho do agente
    session_path = f"{agent}/sessions/{session_id}"
    print(f"Session path: {session_path}\n")

    # Define o endpoint da API conforme a localização
    client_options = None
    agent_components = AgentsClient.parse_agent_path(agent)
    location_id = agent_components["location"]
    
    if location_id != "global":
        api_endpoint = f"{location_id}-dialogflow.googleapis.com:443"
        print(f"API Endpoint: {api_endpoint}\n")
        client_options = {"api_endpoint": api_endpoint}
    
    # Inicializa o cliente de sessão com as opções definidas
    session_client = SessionsClient(client_options=client_options)

    for text in texts:
        text_input = session.TextInput(text=text)
        query_input = session.QueryInput(text=text_input, language_code=language_code)
        request = session.DetectIntentRequest(
            session=session_path, query_input=query_input
        )
        
        # Envia a solicitação para detecção de intenção
        response = session_client.detect_intent(request=request)

        # Exibe o texto da consulta e da resposta
        print("=" * 20)
        print(f"Query text: {text}")
        response_messages = [
            " ".join(msg.text.text) for msg in response.query_result.response_messages
        ]
        print(f"Response text: {' '.join(response_messages)}\n")

# Chamada da função principal para executar o script
if __name__ == "__main__":
    run_sample()
