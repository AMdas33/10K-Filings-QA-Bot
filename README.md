 🧠 10-K Filings Q&A Bot

A Generative AI-powered chatbot that allows users to ask questions about 10-K financial filings. Built using **LangChain**, **OpenAI**, **Pandas**, and **Streamlit**.

## 🚀 Features
- Upload and parse 10-K reports (PDF or text)
- Embedding + Retrieval-based QA using LangChain
- Streamlit interface for interaction
- Works with OpenAI API or Hugging Face embeddings

## 🛠️ Tech Stack
- Python
- LangChain
- OpenAI / HuggingFace Embeddings
  

## 📂 Project Structure
- `src/` contains all backend logic (loading, parsing, and QA logic)
- `app.py` serves the Streamlit interface

## 📦 Setup

```bash
git clone https://github.com/yourusername/10K-Filings-QA-Bot.git
cd 10K-Filings-QA-Bot
pip install -r requirements.txt
cp .env.example .env  # Add your OpenAI API key
