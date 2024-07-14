import streamlit as st
from src.utils import (
    allowed_file, save_uploaded_file, get_existing_pdfs,
    read_pdf_content, delete_pdf
)
from src.tools import PDFSearchTool
from src.agents import PDFChatAgents


def main():
    st.title("📚💬 PDF Chat App")

    # File uploader
    uploaded_files = st.file_uploader(
        "Upload PDF files", accept_multiple_files=True, type=['pdf'])

    if uploaded_files:
        for uploaded_file in uploaded_files:
            if allowed_file(uploaded_file.name):
                save_uploaded_file(uploaded_file)
        st.success("PDF(s) uploaded successfully!")

    # Display existing PDFs and allow selection
    existing_pdfs = get_existing_pdfs()
    if existing_pdfs:
        st.subheader("Existing PDFs:")
        selected_pdfs = st.multiselect(
            "Select PDFs to chat with:", existing_pdfs)

        # Delete PDF functionality
        pdf_to_delete = st.selectbox(
            "Select a PDF to delete (optional):", [""] + existing_pdfs)
        if st.button("Delete Selected PDF"):
            if pdf_to_delete:
                if delete_pdf(pdf_to_delete):
                    st.success(f"Deleted {pdf_to_delete}")
                    st.experimental_rerun()
                else:
                    st.error(f"Failed to delete {pdf_to_delete}")

        if selected_pdfs:
            pdf_content = read_pdf_content(selected_pdfs)
            pdf_search_tool = PDFSearchTool(pdf_content)
            agents = PDFChatAgents(pdf_search_tool.get_tool())

            # Chat interface
            if "messages" not in st.session_state:
                st.session_state.messages = []

            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

            if prompt := st.chat_input("Ask a question about the selected PDF(s)"):
                st.session_state.messages.append(
                    {"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)

                with st.chat_message("assistant"):
                    # Make sure 'prompt' is passed here
                    response = agents.get_pdf_response(prompt)
                    st.markdown(response)
                st.session_state.messages.append(
                    {"role": "assistant", "content": response})

        else:
            st.info("Please select one or more PDFs to start chatting.")
    else:
        st.info("Please upload one or more PDF files to start chatting.")


if __name__ == "__main__":
    main()
