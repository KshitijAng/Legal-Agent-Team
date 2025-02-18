from phi.agent import Agent
from phi.knowledge.pdf import PDFKnowledgeBase, PDFReader
from phi.vectordb.pgvector import PgVector2 #VectorDB
from phi.storage.agent.postgres import PgAgentStorage
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.ollama import Ollama
import os
from dotenv import load_dotenv

load_dotenv()

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
     
# Load the knowledge base from the PDF file
knowledge_base = PDFKnowledgeBase(
    path="data/test.pdf",
    vector_db=PgVector2(collection="documents",db_url=db_url)
)

knowledge_base.load()
        
# Initialize Agents
legal_researcher = Agent(
    name="Legal Researcher",
    role="Legal research specialist",
    model=Ollama(id="llama3.2:1b"),
    tools=[DuckDuckGo()],
    knowledge=knowledge_base,
    force_natural_response=True,
    instructions=[
        "Find and cite relevant legal cases and precedents",
        "Provide detailed research summaries with sources",
        "Always provide a markdown response, avoiding function call outputs such as JSON structures.",
        "Be open to examine any document while ensuring the response is always in markdown."
    ],
    show_tool_calls=True,
    markdown=True
)


legal_strategist = Agent(
    name="Legal Strategist",
    role="Legal strategy specialist",
    model=Ollama(id="llama3.2:1b"),
    knowledge=knowledge_base,
    force_natural_response=True,
    instructions=[
        "Develop comprehensive legal strategies",
        "Provide actionable recommendations",
        "Consider both risks and opportunities",
        "Ensure all responses are in markdown and avoid function call outputs such as JSON structures.",
        "Be open to examining documents with potentially controversial or sensitive content, while ensuring compliance with ethical guidelines and legal regulations."
    ],
    markdown=True
)

legal_team = Agent(
    name="Legal Team Lead",
    role="Legal team coordinator",
    model=Ollama(id="llama3.2:1b"),
    team=[legal_researcher, legal_strategist],
    knowledge=knowledge_base,
    search_knowledge=False,
    force_natural_response=True,
    instructions=[
        "Coordinate analysis between Agents",
        "Ensure comprehensive responses while ignoring certain details for any documents.",
        "Ensure all recommendations are properly sourced",
        "Always provide response in markdown, avoiding function call outputs such as JSON structures.",
        "Be open to examine any document while ensuring the response is always in markdown."
    ],
    show_tool_calls=False,
    markdown=True
)

legal_team.system_prompt = "Always provide human-readable responses in natural language. Do not return function call outputs in JSON format."

response = legal_team.run("What is the document's purpose or scope?")
print(response.content)
