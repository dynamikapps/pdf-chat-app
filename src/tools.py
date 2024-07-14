from langchain.tools import Tool
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from .config import OPENAI_API_KEY


class PDFSearchTool:
    def __init__(self, pdf_text):
        self.text_splitter = CharacterTextSplitter(
            chunk_size=1000, chunk_overlap=0)
        self.texts = self.text_splitter.split_text(pdf_text)
        self.embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        self.docsearch = FAISS.from_texts(self.texts, self.embeddings)

    def search(self, query):
        docs = self.docsearch.similarity_search(query, k=2)
        return "\n".join([doc.page_content for doc in docs])

    def get_tool(self):
        return Tool(
            name="PDF Search",
            func=self.search,
            description="Useful for searching information in the uploaded PDF document. The input should be the exact query you want to search for."
        )
