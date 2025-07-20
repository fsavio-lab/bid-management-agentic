# entity-agent-interaction

**Agentic System Backend for Business Domains**

---

## Overview

`entity-agent-interaction` is a backend service designed to manage intelligent agent workflows across business domains. It combines document processing, agent orchestration, and database integration to support end-to-end “agentic” pipelines.

## Features

- **Agent Pipeline**: Orchestrates tasks using LangChain agents and Celery workers.
- **Document & LLM Integration**: Utilizes LangChain with MongoDB for checkpointing and context persistence.
- **PDF & OCR Support**: Leverages `pymupdf4llm` and `pytesseract` for document processing.
- **Beanie ODM**: MongoDB object-document mapping for domain models such as `Tender`, `Bid`, and `Review`.
- **REST API**: FastAPI-powered CRUD endpoints for procurement and agent entities.

## Tech Stack

| Component              | Description                                         |
|------------------------|-----------------------------------------------------|
| Python ≥3.12           | Modern typing, improved performance                 |
| FastAPI                | Fast, modern web framework for APIs                 |
| Beanie                 | MongoDB ORM built on Pydantic                       |
| Celery                 | Distributed task queue for asynchronous workloads   |
| LangChain              | Framework for building language model agents        |
| MongoDB                | Persistent database storage                         |
| PyMuPDF + pytesseract  | PDF parsing and OCR capabilities                    |

## Getting Started

### Prerequisites

- MongoDB
- Redis or RabbitMQ (for Celery)
- OpenAI API Key (set as `OPENAI_API_KEY`)
- Python ≥ 3.12

### Installation

#### Windows

**Make sure to install Python and PIP from Python Main Site**

```bash
# Clone the Repository
git clone https://github.com/your-username/entity-agent-interaction.git
cd entity-agent-interaction

# Create and Activate Virtual Environment
python -m venv .venv
.venv/Scripts/activate

# Install dependencies
pip install .

uvicorn app.main:app --host 0.0.0.0 # or 127.0.0.1 or localhost 
\ --port 8000 
\ --reload
```

#### Linux
```bash

echo "Updating system..."
sudo apt update && sudo apt upgrade -y

echo "Installing prerequisites..."
sudo apt install -y software-properties-common build-essential libssl-dev libffi-dev libbz2-dev libreadline-dev libsqlite3-dev wget

echo "Adding Deadsnakes PPA..."
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update

echo "Installing Python 3.12 and venv..."
sudo apt install -y python3.12 python3.12-venv python3.12-dev

echo "Clone the Repository"
git clone https://github.com/your-username/entity-agent-interaction.git
cd entity-agent-interaction

python3 -m venv .venv
pip3 install .
uvicorn app.main:app --host 0.0.0.0 # or 127.0.0.1 or localhost 
\ --port 8000 
\ --reload
```
## Roadmap
- Authentication and Authorization (JWT, OAuth)
- Task tracing, telemetry, and analytics for agent pipelines
- Containerization with Docker
- Expanded developer documentation

## License

This project is released under the MIT License.

## Author

Created by Savio Fernando