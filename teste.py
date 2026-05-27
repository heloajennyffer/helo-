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
    st.image("wepink.png", width=250)

    st.subheader("💄 WePink")

    st.write("""
    Marca de beleza e cosméticos conhecida pelos seus produtos modernos,
    femininos e de alta qualidade.
    """)

    st.link_button(
        "Acessar Site",
        "https://wepink.com.br/"
    )

# =========================
# SHEIN
# =========================
with col2:
    st.image("shein.png", width=250)

    st.subheader("🛍️ SHEIN")

    st.write("""
    Loja online de moda famosa pelas tendências atuais,
    roupas estilosas e preços acessíveis.
    """)

    st.link_button(
        "Acessar Site",
        "https://br.shein.com/"
    )

# =========================
# APPLE
# =========================
with col3:
    st.image("apple.png", width=250)

    st.subheader("🍎 Apple")

    st.write("""
    Empresa mundialmente conhecida pelos seus produtos tecnológicos,
    como iPhone, iPad e MacBook.
    """)

    st.link_button(
        "Acessar Site",
        "https://www.apple.com/br/"
    )
