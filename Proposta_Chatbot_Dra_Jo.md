
# Proposta de Arquitetura para o Chatbot da Dra. Jô

## 1. Objetivo e Escopo
O objetivo do chatbot é automatizar o atendimento ao cliente da Dra. Jô, permitindo que os usuários realizem agendamentos, tirem dúvidas frequentes e recebam suporte em tempo real. Isso reduz a carga de trabalho dos atendentes e melhora a experiência do usuário, fornecendo respostas rápidas e precisas.

## 2. Escolha do Chatbot: IBM Watson Assistant
Para criar um chatbot mais avançado, capaz de entender a linguagem natural e lidar com interações complexas, a solução proposta é o **IBM Watson Assistant**. Ele utiliza IA e processamento de linguagem natural (NLP) para interpretar mensagens e fornecer respostas adequadas.

## 3. Camadas da Arquitetura
Aqui está a proposta da arquitetura com foco na solução IBM:

### 3.1. Interface de Usuário (Front-end)
- **Plataformas:** O chatbot será integrado ao **site da Dra. Jô** por meio de um widget de chat e a plataformas de mensagens como **WhatsApp** e **Facebook Messenger**.
- **Função:** A interface permitirá que os clientes façam perguntas diretamente ao chatbot em um ambiente familiar (site ou app de mensagens).
- **Tecnologia:** IBM Watson Assistant tem integrações nativas com essas plataformas.

### 3.2. Motor de Processamento de Linguagem Natural (NLP) - IBM Watson Assistant
- **Função:** Interpretar as mensagens dos usuários e processá-las usando IA. O Watson Assistant é treinado com exemplos de perguntas e respostas, permitindo que ele compreenda a intenção por trás das perguntas e forneça respostas adequadas.
- **Treinamento:** Utilização de dados sintéticos e exemplos reais para melhorar o desempenho do chatbot em interações com clientes da Dra. Jô, cobrindo áreas como agendamentos, suporte técnico, e perguntas frequentes.
- **Ajuste Contínuo:** O modelo será continuamente ajustado com base nas interações reais dos usuários, para melhorar a precisão ao longo do tempo.

### 3.3. Back-end (Processamento e Integração com Sistemas)
- **Lógica de Negócio:** O back-end será responsável por processar as respostas e integrar o chatbot aos sistemas internos, como o sistema de agendamento ou CRM.
- **Tecnologia:** Utilizaremos **Node.js** para criar a lógica do servidor que conecta o chatbot com APIs de terceiros (como sistema de agendamentos e CRM).
- **Banco de Dados:** **IBM Db2** será usado para armazenar informações dos usuários, histórico de interações, e dados necessários para o funcionamento do chatbot.
- **Função:** Processar as respostas e garantir que o chatbot esteja sempre atualizado com as informações mais recentes. Integração via **API REST** com serviços de agendamento.

### 3.4. Infraestrutura em Nuvem - IBM Cloud
- **Hospedagem:** Toda a infraestrutura será executada na **IBM Cloud**, que oferece alta escalabilidade e segurança para as operações.
- **Containerização:** **Docker** será usado para empacotar o backend, o que permite escalar a aplicação de maneira eficiente em um ambiente de microsserviços.
- **Orquestração:** **Kubernetes** será utilizado para gerenciar os contêineres, permitindo escalar automaticamente conforme a demanda de usuários aumenta.
- **Função:** Garantir escalabilidade, desempenho e segurança em todas as camadas da solução, desde a infraestrutura até o gerenciamento de dados.

## 4. Descrição dos Elementos da Arquitetura
- **Interface de Usuário:** A comunicação com os clientes acontecerá por meio de widgets de chat no site e em aplicativos como WhatsApp e Messenger.
- **Motor de NLP:** O IBM Watson Assistant será o núcleo inteligente do chatbot, processando as perguntas e fornecendo respostas adequadas com base na IA e em dados treinados.
- **Back-end e Integração:** O backend criado com Node.js será responsável por integrar o chatbot com sistemas internos como agendamentos e CRM, garantindo que o chatbot tenha acesso a informações em tempo real.
- **Infraestrutura em Nuvem:** A IBM Cloud fornecerá a infraestrutura segura e escalável necessária para hospedar tanto o back-end quanto o Watson Assistant, além de garantir o armazenamento seguro dos dados com o IBM Db2.

## 5. Previsão de Custos

| **Componente**                       | **Custo Mensal**                                                                                                                                                    |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **IBM Watson Assistant**             | Plano gratuito disponível com até 10.000 mensagens mensais. Acima disso, o custo é baseado no número de interações. Custo adicional estimado: $0,0025 por mensagem. |
| **IBM Cloud**                        | Com os créditos de $50 mensais fornecidos pela FIAP, a IBM Cloud oferece serviços como Kubernetes e Docker sem custo inicial. Após o uso dos créditos, os custos variam conforme o uso. |
| **IBM Db2 (Banco de Dados)**         | Existe uma camada gratuita com limites de armazenamento. Caso exceda, o custo pode aumentar dependendo do volume de dados.                                          |
| **Docker/Kubernetes (Infraestrutura)**| Docker é gratuito, e o Kubernetes tem custos associados apenas ao uso da infraestrutura em nuvem, dependendo do volume de tráfego.                                 |
| **WhatsApp Business API**            | Gratuito para até 1.000 mensagens mensais, acima disso, cobra-se por mensagem adicional (cerca de $0,005 por mensagem).                                              |

**Total Estimado:** Com base no uso moderado (até 10.000 mensagens), a previsão inicial de custos pode ser **coberta pelos créditos** oferecidos pela AWS e IBM Cloud. Dependendo do aumento do uso, os custos podem variar, especialmente com a **escalabilidade da infraestrutura** e o **número de interações** no chatbot.

## 6. Resultados Esperados
- **Melhorias na Empresa:**
   - **Automatização de Processos:** O chatbot irá automatizar o agendamento e o suporte ao cliente, reduzindo a carga de trabalho humano e liberando tempo para tarefas mais complexas.
   - **Melhoria na Satisfação do Cliente:** Respostas rápidas e precisas, disponíveis 24/7, vão aumentar a satisfação dos clientes da Dra. Jô.
   - **Escalabilidade:** A solução pode escalar facilmente conforme a empresa cresce e o número de interações aumenta.

- **Valores Agregados ao Modelo de Negócio:**
   - **Eficiência Operacional:** Com a redução da necessidade de interações humanas, o chatbot pode lidar com perguntas frequentes e agendamentos simples, permitindo que a equipe se concentre em atendimentos mais complexos.
   - **Aumento de Receitas:** Com um atendimento mais rápido e eficiente, é provável que a empresa consiga aumentar a conversão de leads e a retenção de clientes.
   - **Melhoria no Atendimento:** O chatbot pode ser configurado para monitorar feedbacks e coletar dados, que podem ser usados para ajustar produtos e serviços com base nas necessidades dos clientes.

- **Possíveis Perdas:**
   - **Necessidade de Ajustes Futuros:** Inicialmente, o chatbot pode fornecer respostas incorretas ou incompletas, o que exige ajustes constantes na lógica e nos dados de treinamento.
   - **Custo de Escalabilidade:** Conforme o uso aumenta, especialmente se houver picos de demanda, os custos de infraestrutura podem escalar, exigindo um planejamento financeiro robusto.
