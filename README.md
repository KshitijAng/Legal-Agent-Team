# 👨‍⚖️ AI Legal Agent Team

A full-service legal team using multiple AI agents using **Phidata** to analyze legal documents and provide comprehensive legal insights. Each agent represents a different legal specialist role, from research and contract analysis to strategic planning, working together to provide thorough legal analysis and recommendations.

## Features

### Specialized Legal AI Agent Team

- **Legal Researcher**: Equipped with DuckDuckGo search tool to find and cite relevant legal cases and precedents. Provides detailed research summaries with sources and references specific sections from uploaded documents.
- **Legal Strategist**: Focuses on developing comprehensive legal strategies, providing actionable recommendations while considering both risks and opportunities.
- **Team Lead**: Coordinates analysis between team members, ensures comprehensive responses, properly sourced recommendations, and references to specific document parts. Acts as an Agent Team coordinator for all three agents.

### Document Analysis Types

- **Contract Review** - Done by Contract Analyst
- **Legal Research** - Done by Legal Researcher
- **Risk Assessment** - Done by Legal Strategist, Contract Analyst
- **Compliance Check** - Done by Legal Strategist, Legal Researcher, Contract Analyst
- **Custom Queries** - Done by Agent Team - Legal Researcher, Legal Strategist, Contract Analyst

## How to Run

### Setup Environment

1. **Install dependencies**
  ```bash
  pip install -r requirements.txt
  ```

2. **Database Integration (pgvector):** This application leverages pgvector for managing embeddings in a PostgreSQL database. pgvector allows the storage and querying of vector embeddings efficiently, making it an ideal choice for high-performance document analysis. For setting up and using pgvector in the system, follow the installation in the [PhiData documentation](https://docs.phidata.com/examples/integrations/pgvector) via **Docker**.

4. **Use the Interface**
- Enter API credentials
- Upload a legal document (PDF) in ```data/``` directory
- Add custom queries if needed
- View analysis results

4. Run the Application
```bash
python main.py
```

## Notes
- Uses **Phidata** for creating the agent
- Supports PDF documents only
- Uses **Ollama** to serve open-source models
- Uses **pgvector** as VectorDB
- Requires stable internet connection
- Requires OPENAI api key and usage costs apply
