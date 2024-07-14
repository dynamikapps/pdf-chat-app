import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# File upload settings
UPLOAD_DIR = "data/uploaded_pdfs"
ALLOWED_EXTENSIONS = {"pdf"}

# LLM settings
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")