import streamlit as st
import openai
import os

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("AI Study Assistant 📚")

prompt = st.text_area("Ask me anything about your studies:")

if st.button("Generate Answer"):
    if prompt.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            st.write(response["choices"][0]["message"]["content"])


