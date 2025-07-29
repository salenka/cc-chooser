import streamlit as st
from functions import q_update, render_html_file, render_license

# Inicialização dos estados das variáveis:
st.session_state.setdefault('q4_disables', False)
st.session_state.setdefault('q2_disables', False)
license = ""
submitted = None

st.image("qualcc_logo.jpg", width=400)
st.subheader("Selecione uma licença Creative Commons")
      
# PERGUNTAS DO FORMULÁRIO

question1 = st.radio(
    "1\) Você sabe qual é a licença que você precisa?", 
    ("Sim", "Não"), 
    index=None,
    key="q1", 
    ) 

if st.session_state.get("q1") == "Sim":
    license = st.selectbox("", ["CC BY", "CC BY-SA", "CC BY-ND", "CC BY-NC", "CC BY-NC-SA", "CC BY-NC-ND", "CC0"], index=None, key="license_select", placeholder="Selecione a licença desejada")
  
else:
    if st.session_state.get("q1") == "Não":
    
        cc_options = st.container()
        with cc_options:
            question2 = st.radio(
                "2\) Você requer que a autoria de seu trabalho seja atribuída a você?", 
                ("Sim", "Não"), 
                index=None, 
                key="q2",
                on_change=q_update
                )
            
            question3 = st.radio("3\) Você aceita que seu trabalho seja usado com fins comerciais?", ("Sim", "Não"), index=None, key="q3", disabled=st.session_state.get("q2_disables", False))
            question4 = st.radio("4\) Você aceita que seu trabalho seja modificado, dando origem a uma obra derivada?", ("Sim", "Não"), index=None, key="q4", disabled=st.session_state.get("q2_disables", False), on_change=q_update)
            question5 = st.radio("5\) Você requer que obras derivadas de seu trabalho sejam disponibilizadas sob estas mesmas condições?", ("Sim", "Não"), index=None, key="q5", disabled=st.session_state.q2_disables or st.session_state.q4_disables)
        
        if st.session_state.get("q2") == "Não":
            license = "CC0"
            
        else:

            with st.form("cc_chooser_form", clear_on_submit=False, enter_to_submit=True, border=False, width="stretch", height="content"):

                if st.session_state.get("q2") == "Sim":
                    if st.session_state.get("q3") == "Sim":
                        if st.session_state.get("q4") == "Não":
                            license = "CC BY-ND"
                        else:
                            if st.session_state.get("q4") == "Sim":
                                if st.session_state.get("q5") == "Sim":
                                    license = "CC BY-SA"
                                else:
                                    if st.session_state.get("q5") == "Não":
                                        license = "CC BY"
                    else:
                        if st.session_state.get("q3") == "Não":
                            if st.session_state.get("q4") == "Não":    
                                license = "CC BY-NC-ND"
                            else:
                                if st.session_state.get("q4") == "Sim": 
                                    if st.session_state.get("q5") == "Não":
                                        license = "CC BY-NC"
                                    else:
                                        if st.session_state.get("q5") == "Sim":
                                            license = "CC BY-NC-SA"
                     
                submitted = st.form_submit_button("Enviar")

if st.session_state.get("q1") == "Sim" or st.session_state.get("q2") == "Não":
    if license:
        st.subheader("A licença selecionada é")         
        render_license(license)
else:
    if submitted:
        if license: 
            st.subheader("A licença selecionada é")         
            render_license(license)
        else:
            st.write("Responta a todas as perguntas ativadas")

            

    
















        





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
    
    





