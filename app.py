import streamlit as st
import google.generativeai as genai
from deep_translator import GoogleTranslator

# Configure the Gemini model
genai.configure(api_key="AIzaSyBVW3RRt8316M4q0tkVt_z8oQeI5bYCCko")
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to explain code using Gemini model
def explain_code(code):
    response = model.generate_content(f"Explain the following code: {code}")
    return response.text

# Function to translate text
def translate_text(text, lang):
    translated = GoogleTranslator(source='auto', target=lang).translate(text)
    return translated

# Language options
languages = {
    "Hindi": "hi",
    "Tamil": "ta",
    "Malayalam": "ml",
    "Kannada": "kn",
}

# Streamlit UI
st.title("AI Code Explainer in native languages")

# Input code
code_input = st.text_area("Enter your code here:")

# Select language for translation
selected_language = st.selectbox("Select language for translation:", list(languages.keys()))

# Button to explain code
if st.button("Explain Code"):
    explanation = explain_code(code_input)
    translated_explanation = translate_text(explanation, languages[selected_language])
    
    st.subheader("Code Explanation:")
    st.write(explanation)
    
    st.subheader("Translated Explanation:")
    st.write(translated_explanation)