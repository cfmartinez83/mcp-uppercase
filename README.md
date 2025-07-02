# MCP Server — JSON-RPC 2.0 Microservice

A simple **MCP (Model-Controller-Processor) server** implemented with FastAPI, supporting JSON-RPC 2.0 protocol.  
Designed to act as a minimal orchestrator for AI agents and tools.

---

## Features

- Supports JSON-RPC 2.0 protocol over HTTP/HTTPS  
- Implements two example methods:  
  - `get_status`: returns current UTC datetime and a unique server code  
  - `uppercase`: returns uppercase version of a given text  
- CORS enabled for web client compatibility  
- Dockerized for easy deployment  
- Ready for deployment on platforms like Render, AWS ECS, Fly.io, etc.

---

## Installation

### Prerequisites

- Python 3.10+  
- Docker & Docker Compose (optional but recommended)  

### Local Setup

1. Clone this repository  
2. (Optional) Create and activate a Python virtual environment  
3. Install dependencies:

```bash
pip install -r requirements.txt
