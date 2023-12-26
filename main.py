import streamlit as st
import google.generativeai as palm
from dotenv import load_dotenv
import os
from langdetect import detect
from translate import Translator

load_dotenv()

API_KEY = os.environ.get("PALM_API_KEY")
palm.configure(api_key=API_KEY)

def detect_language(text):
    try:
        lang = detect(text)
        return lang
    except:
        return 'en' 

def translate_text(text, target_language='en'):
    translator = Translator(to_lang=target_language)
    translated_text = translator.translate(text)
    return translated_text

def main():
    st.set_page_config(
        page_title="AI Ku Chat",
        page_icon="🤖",
        layout="centered"
    )

    st.sidebar.title("Menu")
    selected_page = st.sidebar.radio("", ["Home", "AI"])

    if selected_page == "Home":
        show_homepage()
    elif selected_page == "AI":
        show_ai_page()

def show_homepage():
    st.title("AI Ku")
    ai_symbol_path = "ai2.png"
    st.image(ai_symbol_path, width=100, caption="Logo AI Ku")
    st.markdown("""
        AI ini dibuat oleh mahasiswa semester III 
        Kampus Bina Sarana Informatika Tasikmalaya,
                :bold[Maaf jika AI ini masih mengandung banyak bug]
                 
    """)
    st.markdown("""
        :green[Wisnu Dwijaya Kusuma~]                
""")

def show_ai_page():
    st.title("Chat With AI")
    st.write("")
    st.write("""
         Silahkan cari apapun sesuka hatimu
    """)

    prompt = st.text_area("Ayo Cari yang kamu mau...", placeholder="Cari di sini ya", key="input_text", height=100)

    if st.button("SEND", use_container_width=True):

        input_language = detect_language(prompt)

        model = "models/text-bison-001"
        try:
            response = palm.generate_text(
                model=model,
                prompt=prompt,
                max_output_tokens=1024
            )

            output_language = detect_language(response.result)

            st.write("")
            st.header("Response")
            st.markdown(f"**Detected Input Language:** {input_language}")
            st.markdown(f"**Detected Output Language:** {output_language}")
            response_text_area = st.text_area("AI Response", value=response.result, height=200)

            if st.button("Copy Response"):
                st.text_area("Copied!", value=response_text_area, height=50)

        except Exception as e:
            st.error(f"Error: {e}. The requested language may not be supported by the model.")
            st.text_area("AI Response", value="Sorry, an error occurred. Please try again.", height=200)

if __name__ == "__main__":
    main()

    #AI made with python program 
    #made by inuu.dk