from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from .config import OPENAI_API_KEY, MODEL_NAME


class PDFChatAgents:
    def __init__(self, pdf_search_tool):
        self.llm = ChatOpenAI(model_name=MODEL_NAME,
                              openai_api_key=OPENAI_API_KEY, temperature=0)
        self.pdf_search_tool = pdf_search_tool

    def create_researcher(self):
        return Agent(
            role='Researcher',
            goal='Search for relevant information in the PDF',
            backstory='You are an expert at finding relevant information in documents.',
            tools=[self.pdf_search_tool],
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def create_writer(self):
        return Agent(
            role='Writer',
            goal='Formulate clear, concise, and varied answers based on the research',
            backstory='You are a skilled writer, able to craft informative and diverse responses.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def create_crew(self, query):
        researcher = self.create_researcher()
        writer = self.create_writer()

        research_task = Task(
            description=f'Search the PDF for information relevant to the user query: "{query}". Provide detailed and relevant results.',
            agent=researcher,
            expected_output=f"Detailed and relevant information from the PDF related to the user's query: {query}"
        )

        writing_task = Task(
            description=f'Use the research results to formulate a clear, concise, and specific answer to the user query: "{query}". Ensure the response is tailored to the specific question and not a generic answer.',
            agent=writer,
            expected_output=f"A clear, concise, and specific answer to the user's query: {query}"
        )

        return Crew(
            agents=[researcher, writer],
            tasks=[research_task, writing_task],
            verbose=True,
            process=Process.sequential
        )

    def get_pdf_response(self, query):
        crew = self.create_crew(query)
        result = crew.kickoff()
        return result
