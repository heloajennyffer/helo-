import streamlit as st

# CONFIG
st.set_page_config(page_title="Empresas Parceiras", layout="wide")

# TÍTULO
st.title("🌐 Empresas Parceiras")

# COLUNAS
col1, col2, col3 = st.columns(3)

# =========================
# WEPINK
# =========================
with col1:
    try:
        st.image("wepink.png", width=250)
    except:
        st.warning("Imagem wepink.png não encontrada")

    st.subheader("💄 WePink")

    st.write("""
    Marca de beleza e cosméticos conhecida pelos seus produtos modernos
    e femininos.
    """)

    st.link_button(
        "Acessar Site",
        "https://wepink.com.br/"
    )

# =========================
# SHEIN
# =========================
with col2:
    try:
        st.image("shein.png", width=250)
    except:
        st.warning("Imagem shein.png não encontrada")

    st.subheader("🛍️ SHEIN")

    st.write("""
    Loja online de moda famosa pelas tendências atuais
    e preços acessíveis.
    """)

    st.link_button(
        "Acessar Site",
        "https://br.shein.com/"
    )

# =========================
# APPLE
# =========================
with col3:
    try:
        st.image("apple.png", width=250)
    except:
        st.warning("Imagem apple.png não encontrada")

    st.subheader("🍎 Apple")

    st.write("""
    Empresa mundialmente conhecida pelos seus produtos tecnológicos,
    como iPhone, iPad e MacBook.
    """)

    st.link_button(
        "Acessar Site",
        "https://www.apple.com/br/"
    )
