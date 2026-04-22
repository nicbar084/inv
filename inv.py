import streamlit as st
import random

st.set_page_config(page_title="Invitación", page_icon="🍔")

st.title("¿Te gustaría ir a comer conmigo? 🍕")

# Estado de sesión
if "rechazos" not in st.session_state:
    st.session_state.rechazos = 0

col1, col2 = st.columns(2)

# Botón SI
with col1:
    if st.button("Sí 😄"):
        st.success("¡Sabía que dirías que sí! 😍")
        st.balloons()
        st.write("Entonces... ¿viernes a las 8? 😉")

# Botón NO
with col2:
    if st.button("No 😢"):
        st.session_state.rechazos += 1

        mensajes = [
            "¿Segura/o? 😢",
            "Piénsalo bien 😅",
            "No puedes decir que no tan fácil 😭",
            "Última oportunidad 👀"
        ]

        st.warning(random.choice(mensajes))