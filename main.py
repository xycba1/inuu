import streamlit as st
import google.generativeai as palm
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY=os.environ.get("PALM_API_KEY")
palm.configure(api_key=API_KEY)

def main():
 st.header("Chat With AI")
 st.write("")
st.title("AI Ku")
st.write("""
         Ini web Ai buatan Inuu.dk 
        
""")

prompt = st.text_input("Please dong curhat...", placeholder="Sini curhat", label_visibility="visible")


if st.button("SEND", use_container_width=True):
 model = "models/text-bison-001"

 response = palm.generate_text(
  model=model,
  prompt=prompt,
  max_output_tokens=1024
 )

 st.write("")
 st.header(":blue[Response]")
 st.write("")

 st.markdown(response.result, unsafe_allow_html=False, help=None)

if __name__ == "__main__":
 main()