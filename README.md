# 📚💬 PDF Chat App

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Overview

PDF Chat App is an innovative AI-powered application that allows users to interact with and extract information from PDF documents through a conversational interface. Built with state-of-the-art natural language processing technologies, this app enables users to upload PDFs, ask questions, and receive accurate answers based on the content of the documents.

## Features

- 📤 PDF Upload: Users can upload multiple PDF files.
- 🔍 Intelligent Search: Advanced semantic search capabilities for finding relevant information in PDFs.
- 💬 Interactive Chat: User-friendly chat interface for asking questions about PDF content.
- 📊 Multi-Document Support: Ability to chat with multiple selected PDFs simultaneously.
- 🗑️ PDF Management: Users can delete uploaded PDFs when they're no longer needed.
- 🚀 Efficient Text Extraction: Extracts and stores PDF text content for faster subsequent queries.
- 🧠 AI-Powered Responses: Utilizes advanced AI models to generate accurate and context-aware answers.

## Technologies Used

- Python 3.10+
- Streamlit
- LangChain
- CrewAI
- OpenAI GPT models
- PyPDF2
- FAISS (Facebook AI Similarity Search)
- Docker
- AWS (for deployment)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/dynamikapps/pdf-chat-app.git
   cd pdf-chat-app
   ```

2. Create a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your OpenAI API key

## Usage

1. Run the Streamlit app:

   ```
   streamlit run main.py
   ```

2. Open your web browser and go to `http://localhost:8501`

3. Upload PDF files using the file uploader.

4. Select the PDFs you want to chat about.

5. Start asking questions in the chat interface!

## Project Structure

```
pdf_chat_app/
│
├── main.py              # Main Streamlit application
├── requirements.txt     # Project dependencies
├── .env                 # Environment variables (not in version control)
│
├── src/
│   ├── __init__.py
│   ├── agents.py        # CrewAI agents definition
│   ├── tools.py         # Custom tools for PDF processing
│   ├── utils.py         # Utility functions
│   └── config.py        # Configuration settings
│
└── data/
    └── uploaded_pdfs/   # Directory for storing uploaded PDFs
```

## How It Works

1. **PDF Upload**: When a user uploads a PDF, the app extracts the text content and stores it for efficient retrieval.

2. **User Query**: The user selects PDFs and asks a question through the chat interface.

3. **AI Processing**:

   - A CrewAI crew is created with two agents: a Researcher and a Writer.
   - The Researcher agent uses the PDFSearchTool to find relevant information in the selected PDFs.
   - The Writer agent formulates a clear and concise answer based on the Researcher's findings.

4. **Response**: The app displays the AI-generated response to the user's query.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, please contact [handy@dynamikapps.com](mailto:handy@dynamikapps.com).
