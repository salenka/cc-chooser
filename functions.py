import streamlit as st

# Inicialização dos estados das perguntas
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


# Carregar HTML
def render_html_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            st.markdown(file.read(), unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Arquivo HTML da licença não encontrado: {file_path}")
    except Exception as e:
        st.error(f"Erro ao carregar HTML: {str(e)}")

def render_license(license):
        render_html_file(f"{license}_4.0.html")


def licence_selection():
    license_selecty = st.session_state.license_select
    return st.toast(f"Selecionou: {license_selecty}")