from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import streamlit as st
import os
import time

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

st.set_page_config(
    page_title="Pet Name Generator",
    page_icon=":paw_prints:",
    layout="centered"
)

st.title("🐾Pet Name Generator")
st.write("Generate creative pet names based on the type of animal and its colors!")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0, api_key=api_key)

template = """
Suggest a pet name for an animal that is a {name}\
with the following colors: {colors}.
List only 10 names
"""

st.sidebar.header("Customize Your Pet")

name = st.sidebar.selectbox("Select the type of animal:", ["Cat", "Dog", "Horse", "Rabbit", "Bird"])

colors = st.sidebar.text_area("Enter the colors of the animal (comma-separated):", placeholder="e.g., black, white, brown")

prompt_template = ChatPromptTemplate.from_template(template)
prompt = prompt_template.format_messages(name=name.lower(), colors=colors.strip())

def generate_pet_name():
    retries = 3
    delay = 2

    for i in range(retries):
        try:
            response = llm(prompt)
            return response.content.strip()
        except Exception as e:
            st.error(f"Error: {str(e)}")
            if i < retries - 1:
                st.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)
                delay *= 2
            else:
                st.error("Failed to generate a pet name. Please try again later.")
                return None

if st.button("Generate Pet Name"):
    if colors:
        pet_name = generate_pet_name()
        if pet_name:
            st.subheader("Your Pet Name Suggestion:")
            st.markdown(f"{pet_name}")
    else:
        st.error("Please enter at least one color.")

st.markdown("---")
st.write("Powered by Gemini-AI")
