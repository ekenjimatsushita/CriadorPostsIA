import streamlit as st
from google import genai
from google.genai import types

# ---------------------------------------------------Funções---------------------------------------------------------------------
# definindo a chave API
api_key = st.secrets['GOOGLE_API_KEY']
if not api_key:
    st.error('Chave da API do Gemini não configurada')
    st.stop

# configurando a API
client = genai.Client(api_key=api_key)

# configurando as informações para cada rede social e objetivo
def get_api_config(rede_social, objetivo):
    # Redes sociais: Instagram, LinkedIn, Twitter/X e TikTok
    # Objetivos: Aumentar a Visibilidade/Alcance, Criar Consciência sobre uma Causa, Gerar Interação, Educar/Capacitar, Informar, Sensibilizar
    
    # configs base para
    api_configs = {
        'temperature': 0.7,
        'max_output_tokens': 3000,
        'top_p': 0.9
    }

    # para Instagram
    if rede_social == 'Instagram': 
        api_configs['max_output_tokens'] = 2200  
        if objetivo in ['Aumentar a Visibilidade/Alcance', 'Gerar Interação', 'Sensibilizar']:
            api_configs['temperature'] = 0.8 # texto mais criativo para prender a atenção
        else: 
            api_configs['temperature'] = 0.6 # texto mais técnico e preciso

    # para LinkedIn
    elif rede_social == 'LinkedIn':
        api_configs['max_output_tokens'] = 3000
        if objetivo in ['Informar', 'Educar/Capacitar']:
            api_configs['temperature'] = 0.4 # texto bastante técnico
        elif objetivo == 'Aumentar a Visibilidade/Alcance':
            api_configs['temperature'] = 0.6 # texto apropriadamente técnico mas com criatividade para engajar
        else: 
            api_configs['temperature'] = 0.7 # texto mais criativo

    # para Twitter
    elif rede_social == 'Twitter/X':
        api_configs['max_output_tokens'] = 2140
        if objetivo in ['Aumentar a Visibilidade/Alcance', 'Gerar Interação']:
            api_configs['temperature'] = 0.8
        else: 
            api_configs['temperature'] = 0.6 # para textos com maior necessidade de precisão

    # para TikTok
    elif rede_social == 'TikTok':
        api_configs['max_output_tokens'] = 2075
        if objetivo in ['Aumentar a Visibilidade/Alcance', 'Gerar Interação', 'Sensibilizar']:
            api_configs['temperature'] = 0.9 # textos curtos e bem criativos para chamar atenção
        else: 
            api_configs['temperature'] = 0.7 # textos criativos ainda, mas com certa técnica

    
    return api_configs


# fazendo um prompt base para ser utilizado de acordo com a rede social
def get_prompt(ideia, rede_social, objetivo):
    prompt_base = f'Faça um post para {rede_social} com objetivo de {objetivo} a partir da seguinte ideia: {ideia}.'
    cta = f'Faça um call to action curto que prenda a atenção do público e gere interesse de acordo com o objetivo {objetivo}.'
    hashtags = 'Inclua hashtags relevantes no final do texto, utilizando palavras chaves.'

    if rede_social == 'Instagram':
        prompt_final = f'{prompt_base}Utilize uma linguagem mais dinâmica, um tom engajador e emojis, se adequando a uma rede mais interativa.'
        if objetivo == 'Gerar Interação':
            prompt_final += 'Faça uma pergunta ou um chamativo para induzir as pessoas a comentarem no post.'
        elif objetivo in ['Sensibilizar', 'Criar Consciência sobre uma Causa']:
            prompt_final += 'Faça com que o post seja mais emotivo e impactante.'
    
    elif rede_social == 'LinkedIn':
        prompt_final = f'{prompt_base}Mantenha um tom profissional, forneça insights valiosos e incentive reflexões.'
        if objetivo == 'Educar/Capacitar':
            prompt_final += 'Apresente dados, dicas práticas ou um pequeno passo a passo.'
        elif objetivo == 'Informar':
            prompt_final += 'Seja preciso e direto nos fatos principais.'
    
    elif rede_social == "Twitter/X":
        prompt_final = f'{prompt_base}Seja preciso, coerente, impactante e utilize poucas palavras.'
        if objetivo == 'Aumentar a Visibilidade/Alcance':
            prompt_final += 'Pense em um gancho que convide ao retweet.'
        elif objetivo == 'Gerar Interação':
            prompt_final += 'Faça uma pergunta rápida ou uma enquete.'
    
    elif rede_social == 'TikTok':
        prompt_final = f'{prompt_base}Crie uma legenda muito curta e que gere curiosidade para um vídeo, usando emojis e um gancho rápido.'
        if objetivo == 'Gerar Interação':
            prompt_final += 'Faça uma pergunta simples nos comentários, para incentivar a interação dos usuários.'
        elif objetivo == 'Sensibilizar':
            prompt_final += 'Use frases curtas com forte impacto emocional.'
    
    return  prompt_final + cta + hashtags + 'Escreva somente a postagem e utilize a seguinte estutura: post com cta,divisor,hashtags. Deixe bem clara essa divisão usando divisores entre cada parte'

    
#----------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------Em tela------------------------------------------------------------------------

st.markdown('<h1 style="text-align: center; margin: auto; top: 1px"> EngajaAI </h1>', unsafe_allow_html=True)
st.write('')

st.header('Início', divider='orange')
st.write('Saudações! :sunglasses:')
st.write('Sabe aquela sensação de ter uma ideia genial borbulhando na cabeça, mas travar na hora de transformá-la em algo que realmente engaje nas redes sociais? Eu sei bem! Por isso, eu nasci. Sou a ferramenta que vai dar voz aos seus pensamentos, transformando simples ideias em posts irresistíveis, prontos para bombar na rede social de sua escolha. Diga-me o que você quer alcançar - mais seguidores, tráfego para o seu site, ou simplesmente espalhar uma mensagem - e me conte sobre a sua ideia. Deixe a inteligência artificial trabalhar a magia, e prepare-se para ver seus posts decolarem!')

st.header('Sobre', divider='orange')
st.write('A lógica por trás da aplicação é bem simples! Inicialmente o usuário irá selecionar uma rede social preferencial, definir um tema para ser abordado e indicar qual o objetivo da postagem. Por exemplo, o usuário dirá "preciso realizar um post sobre pets" e selecionará a rede social "Instagram" e o objetivo "Sensibilizar ou conscientizar". Protinho! O post será gerado em questão de segundos e você poderá colocá-lo para atrair atenção a suas redes.')

st.header('Aplicação', divider='orange')
st.subheader('Gerador de texto')
st.write('Agora você pode transformar suas ideias em posts de maneira eficiente e alcançando seu objetivo sem muito trabalho!')
st.text_area('Escreva aqui o que você está pensando para transformar em um post chamativo para sua rede social.', key='ideia_principal', placeholder='Ex: Como a IA está revolucionando a forma de interação entre usuários nas redes sociais?')

social_medias = ['Instagram', 'LinkedIn', 'Twitter/X', 'TikTok']
st.session_state.redes_sociais = st.selectbox('Selecione aqui a rede social de escolha. A rede social influencia muito na forma do post!', options=social_medias, key='rede_escolhida')

objetivos_post = ['Aumentar a Visibilidade/Alcance', 'Criar Consciência sobre uma Causa', 'Gerar Interação', 'Educar/Capacitar', 'Informar', 'Sensibilizar']
st.session_state.objetivos = st.selectbox('O objetivo é muito importante para estruturar sua postagem! Escolha seu principal objetivo.', options=objetivos_post, key='objetivo_escolhido')
st.write('')

# criando um histórico
if 'historico' not in st.session_state:
    st.session_state.historico = []

def display_history():
    for message in st.session_state.historico:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def add_history(func, conteudo):
    st.session_state.historico.append({"role": func, "content": conteudo})

if st.button('Histórico'):
    if st.session_state.historico == []:
        st.warning('Não há histórico, por favor realize uma interação.')
    else:
        display_history()

if st.button('Gerar Post'):
    if not st.session_state.ideia_principal:
        st.warning('Por favor, insira uma ideia para o post.')
        st.stop()
    with st.spinner('Produzindo seu post... :hourglass_flowing_sand:'):
        user_ideia = st.session_state.ideia_principal
        rede_social = st.session_state.redes_sociais
        objetivo = st.session_state.objetivos


        prompt = get_prompt(user_ideia, rede_social, objetivo)
        api_config = get_api_config(rede_social, objetivo)


        st.info(f'Gerando um post para {rede_social} com objetivo {objetivo}, a partir da ideia: {user_ideia}')

        add_history('user', f'Ideia: {user_ideia}, Rede Social: {rede_social}, Objetivo: {objetivo}')

        try:
            configs = types.GenerateContentConfig(
                max_output_tokens=api_config['max_output_tokens'],
                temperature=api_config['temperature'],
                top_p=api_config['top_p'],
            )
            resposta = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config=configs
            )
            conteudo_post = resposta.text
            add_history("assistant", conteudo_post)       
            st.success('Post gerado com sucesso! :heavy_check_mark:')

            st.subheader('Aqui está seu post!', divider='orange')
            st.write(f'{conteudo_post}')

        except:
            st.error('Ocorreu um erro ao chamar a API do Gemini :warning:')
            st.markdown('Tente novamente em alguns instantes e/ou verifique sua conexão com a internet')


        
#------------------------------------------------------------------------------------------------------------------------------------
