# 🐾 Pet Name Generator

Welcome to the **Pet Name Generator**! This project uses the power of Google Generative AI (Gemini-1.5-pro) and LangChain to suggest creative and unique pet names based on the type of animal and its colors.

## 🚀 Features

- **Animal Selection:** Choose from a variety of animals like cats, dogs, horses, rabbits, and birds.
- **Color Customization:** Input one or more colors to get personalized name suggestions.
- **AI-Powered Suggestions:** Leverages Google's Gemini AI for generating creative pet names.

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/farukh-javed/Pet-name-Generator-with-Gemini-Langchain.git
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables by creating a `.env` file and adding your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## 🖥️ Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open the app in your browser and start generating pet names!

## 📄 Code Overview

- `app.py`: The main application file that sets up the Streamlit interface and integrates with Google Generative AI using LangChain.

## 🤖 Powered By

- **LangChain**
- **Google Generative AI (Gemini-1.5-pro)**
- **Streamlit**

## 📝 License

This project is licensed under the MIT License.
