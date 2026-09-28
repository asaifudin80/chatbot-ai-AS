import streamlit as st
import google.generativeai as genai

# Konfigurasi API key
genai.configure(api_key="MASUKKAN_API_KEY_KAMU")

# Judul aplikasi
st.title("🤖 Chatbot AI dengan Streamlit")

# Inisialisasi model
model = genai.GenerativeModel("gemini-2.0-flash")

# Simpan riwayat chat di session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan riwayat chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input pengguna
if prompt := st.chat_input("Tulis pesanmu..."):
    # Tampilkan pesan user
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Balasan AI
    with st.chat_message("assistant"):
        with st.spinner("Mengetik..."):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append(
                {"role": "assistant", "content": response.text}
            )
