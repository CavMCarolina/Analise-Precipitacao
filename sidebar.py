import streamlit as st

def show_sidebar():
    # Oculta a navegação padrão do Streamlit com CSS
    st.markdown("""
        <style>
            [data-testid="stSidebarNav"] {display: none;}
        </style>
    """, unsafe_allow_html=True)

    # Criando o sidebar personalizado
    st.sidebar.title("Navegação")
    st.sidebar.write("❓ **Introdução**")
    st.sidebar.page_link("introducao.py", label="Contextualização do Problema")
    st.sidebar.page_link("pages/descricao.py", label="Descrição do Dataset")

    st.sidebar.divider()

    st.sidebar.write("🔍 **Análise**")
    st.sidebar.page_link("pages/normal.py", label="Distribuição Normal")
    st.sidebar.page_link("pages/confianca.py", label="Intervalo de Confiança")
    st.sidebar.page_link("pages/hipotese.py", label="Teste de Hipóteses")
    st.sidebar.page_link("pages/regional.py", label="Gráfico Regional")
    st.sidebar.page_link("pages/padroes.py", label="Padrões Sazonais")

    st.sidebar.divider()
    st.sidebar.markdown("Carolina Cavalli Machado")
    st.sidebar.markdown(f"""<a href="https://www.linkedin.com/in/carolinacavallimachado">Linkedin</a> • <a href="https://github.com/CavMCarolina">GitHub</a>""", unsafe_allow_html=True)