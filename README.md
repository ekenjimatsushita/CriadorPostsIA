# Criador de Posts com IA (EngajaAI)

## 🎈 Introdução

Experimente! [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ekenjimatsushita-criadorpostsia-project-sm-lxfuym.streamlit.app)

Essa é uma aplicação com objetivo de auxiliar o usuário a criar posts para suas redes sociais a partir de uma ideia e tendo um objetivo em mente. Utilizando a API do Gemini, a ferramenta consegue gerar uma postagem, a partir de ideias do usuário, que consiga alcançar a audiência de acordo com os objetivos explicitados.


## 🤖 Tecnologias

* O software funciona utilizando como framework o Streamlit, com deploy em nuvem no Streamlit Comunnity Cloud.
* Foram utilizadas as bibliotecas streamlit, google-generativeai, dotenv do python
* A IA utilizada é a API Gemini do Google 

## 🔥 Utilização 
O usuário é introduzido e instruído ao funcionamento da aplicação por meio de uma interface onde serão inseridas as informações necessárias para gerar o post. A ideia principal deve ser digitada em um campo, enquanto a rede social e os objetivos devem ser escolhidos dentre as opções disponíveis. A partir disso, a API é configurada com base nos parâmetros definidos, de forma que sua temperatura e seu número máximo de tokens sejam específicos para cada opção escolhida pelo usuário. Depois disso é gerado um prompt, também característico, para que a IA faça a criação da postagem. Por fim, há a instrução de inserir um Call to Action e Hashtags que servem para impulsionar nas redes sociais.

Veja um pouco abaixo!

![image](https://github.com/user-attachments/assets/e869c2cd-0e01-4f1d-b6bc-735f7ddad257) ![image](https://github.com/user-attachments/assets/d3f93fa7-e94f-4d68-8f8d-9584e31529e2)



## ⚙️ Configuração do Ambiente

Siga estas etapas para configurar e executar o projeto localmente.

### Pré-requisitos

* **Python 3.8+**
* **Git**
* **Chave da API do Google Gemini:** Obtenha uma chave gratuita no [Google AI Studio](https://aistudio.google.com/).

### 1. Clonar o Repositório

```bash
git clone [https://github.com/ekenjimatsushita/CriadorPostsIA.git](https://github.com/ekenjimatsushita/CriadorPostsIA.git)
cd CriadorPostsIA
