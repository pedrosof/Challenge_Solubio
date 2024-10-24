from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Credenciais da API do Watson Assistant
api_key = '3BI_CbD-h6_CpdpIJb-Lslj02_eCM9F5OTpSo1C7PWIK'  # Substitua pela sua API Key
url = 'https://api.us-east.assistant.watson.cloud.ibm.com/instances/4471e0d3-49c2-4f0c-9f8d-f8144f838ba3'  # Substitua pela URL do Watson Assistant
assistant_id = '91b4b6f5-14f1-46f6-b06c-73d22d776a92'  # Substitua pelo Assistant ID

# Autenticar no Watson Assistant
authenticator = IAMAuthenticator(api_key)
assistant = AssistantV2(
    version='2021-06-14',
    authenticator=authenticator
)
assistant.set_service_url(url)

# Criar uma nova sessão
session = assistant.create_session(
    assistant_id=assistant_id
).get_result()

session_id = session['session_id']
print("Sessão iniciada com sucesso!")

# Função para enviar uma mensagem do usuário ao chatbot
def send_message(text):
    response = assistant.message(
        assistant_id=assistant_id,
        session_id=session_id,
        input={
            'message_type': 'text',
            'text': text
        }
    ).get_result()
    
    output = response['output']['generic']
    if output:
        for item in output:
            print('Chatbot: ' + item['text'])

# Loop para simular a conversa com o chatbot
try:
    while True:
        user_message = input("Você: ")
        if user_message.lower() == 'sair':
            print("Encerrando a conversa...")
            break
        send_message(user_message)

finally:
    # Fechar a sessão ao encerrar a conversa
    assistant.delete_session(
        assistant_id=assistant_id,
        session_id=session_id
    )
    print("Sessão encerrada.")
