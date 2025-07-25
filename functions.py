import streamlit as st

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
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    # Carrega o CSS manualmente
    with open("styles/style.css", "r", encoding="utf-8") as css_file:
        css = f"<style>{css_file.read()}</style>"
    st.markdown(css + html_content, unsafe_allow_html=True)

def render_license(license):
        render_html_file(f"{license}_4.0.html")
