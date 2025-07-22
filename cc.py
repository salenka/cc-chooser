import streamlit as st
# para rodar o programa, no terminal: streamlit run cc.py

st.title("Seletor de Licença Creative Commons")
st.write("Olá, mundo!!!")

# Inicialização dos estados
if 'q2_disables' not in st.session_state:
    st.session_state.q2_disables = False
if 'q4_disables' not in st.session_state:
    st.session_state.q4_disables = False

def q_update():
    if st.session_state.get("q2") == "Não":
        st.session_state.q3 = None
        st.session_state.q4 = None
        st.session_state.q5 = None
        st.session_state.q2_disables = True  # 👈 Define no session_state
    else:
        st.session_state.q2_disables = False


    if st.session_state.get("q4") == "Não":
        st.session_state.q5 = None
        st.session_state.q4_disables = True  # 👈 Define no session_state
    else:
        st.session_state.q4_disables = False
        

#perguntas

question1 = st.radio(
    "Você sabe qual é a licença que você precisa?", 
    ("Sim", "Não"), 
    index=None,
    key="q1", 
    ) 

if st.session_state.get("q1") == "Sim":
    license = st.selectbox("", ["CC BY", "CC BY-SA", "CC BY-ND", "CC BY-NC", "CC BY-NC-SA", "CC BY-NC-ND", "CC0"], index=None, placeholder="Selecione a licença desejada")
    
elif st.session_state.get("q1") == "Não":
    
    cc_options = st.container()
    with cc_options:
        question2 = st.radio(
            "Você deseja que a autoria do seu trabalho seja atribuída a você, necessariamente?", 
            ("Sim", "Não"), 
            index=None, 
            key="q2",
            on_change=q_update
            )
        
        question3 = st.radio("Você aceita que seu trabalho seja usado com fins comerciais?", ("Sim", "Não"), index=None, key="q3", disabled=st.session_state.get("q2_disables", False))
        question4 = st.radio("Você aceita que seu trabalho seja modificado, dando origem a uma obra derivada?", ("Sim", "Não"), index=None, key="q4", disabled=st.session_state.get("q2_disables", False), on_change=q_update)
        question5 = st.radio("Você deseja que obras derivadas de seu trabalho sejam disponibilizadas sob as mesmas condições?", ("Sim", "Não"), index=None, key="q5", 
                             disabled=st.session_state.q2_disables or st.session_state.q4_disables)
        













# SELETOR FASE 2 ___________________________________________________
Seletor_Fase2 = False
if Seletor_Fase2:
    cc_confirmations = st.container()
    with cc_confirmations:
        confirmation1 = st.checkbox("Eu tenho a autorizadade necessária para licenciar este trabalho", key="c1")
        confirmation2 = st.checkbox("Eu li e entendi os termos da licença", key="c2")
        confirmation3 = st.checkbox("Eu entendo que a licença Creative Commons é irrevogável", key="c3")

    cc_data = st.container()
    with cc_data:
        data1 = st.text_input(label="Título do trabalho", max_chars=200, help="Escreva o título do seu trabalho", key="d1")
        data2 = st.text_input(label="Criador do trabalho", max_chars=200, help="Escreva o nome do(s) autor(es) do trabalho, separados por vírgula", key="d2")
        data3 = st.text_input(label="Link para o trabalho", help="Insira o link para seu trabalho")
        data4 = st.text_input(label="Link para página do criador do trabalho", help="Insira o link para página do(s) autor(es) do trabalho")
        data5 = st.number_input(label="Ano de criação", value=2025, min_value=1955, max_value=2055, step=1, help="Informe o ano de criação", key="d5")
# __________________________________________________________________
    
    





