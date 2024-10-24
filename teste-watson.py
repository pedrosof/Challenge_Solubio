from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Credenciais do Watson Assistant
api_key = 'fcIaNhYjZOQA5TJghKQSvBKmtYsaoahTClTdoMeZIw3n'
url = 'https://api.us-east.assistant.watson.cloud.ibm.com/instances/4471e0d3-49c2-4f0c-9f8d-f8144f838ba3'
assistant_id = '91b4b6f5-14f1-46f6-b06c-73d22d776a92'

# Autenticação
authenticator = IAMAuthenticator(api_key)
assistant = AssistantV2(
    version='2021-06-14',
    #version='2020-04-01',
    authenticator=authenticator
)
assistant.set_service_url(url)

# Criar uma sessão
try:
    session = assistant.create_session(
        assistant_id=assistant_id
    ).get_result()
    print("Sessão criada com sucesso:", session['session_id'])
except Exception as e:
    print(f"Erro ao criar a sessão: {e}")
