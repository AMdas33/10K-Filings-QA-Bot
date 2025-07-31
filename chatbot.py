import pandas as pd
import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Step 1: Load structured 10-K data
df = pd.read_csv("10k_filing.csv")

# Step 2: Turn dataframe into list of Documents
documents = [
    Document(page_content=f"{row['Item']}: {row['Description']}")
    for _, row in df.iterrows()
]

# Step 3: Embed the documents
embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)
db = FAISS.from_documents(documents, embedding)

# Step 4: Create a retriever and chatbot chain
retriever = db.as_retriever()
llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Step 5: Ask questions
while True:
    query = input("Ask a question about the 10-K report (or 'exit'): ")
    if query.lower() == 'exit':
        break
    result = qa_chain.run(query)
    print(f"\nAnswer: {result}\n")
