# app.py

import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    st.error("OpenAI API key not found. Please set it in the .env file.")
    st.stop()

# Set the OpenAI API key
openai.api_key = openai_api_key

# Streamlit app code
st.title("Hello, World!")
st.write("Welcome to the Hello World Streamlit App!")

user_input = st.text_input("Enter your message:")

if st.button("Send"):
    if user_input:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=50,
                temperature=0.7
            )
            st.write(f"**Response:** {response.choices[0].message['content'].strip()}")
        except Exception as e:
            st.error(f"Error communicating with OpenAI: {e}")
    else:
        st.warning("Please enter a message.")
