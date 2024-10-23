from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Credenciais da API do Watson Assistant
api_key = 'SUA_API_KEY_AQUI'  # Substitua pela sua API Key
url = 'SUA_URL_DO_WATSON_AQUI'  # Substitua pela URL do Watson Assistant
assistant_id = 'SEU_ASSISTENTE_ID_AQUI'  # Substitua pelo Assistant ID

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
