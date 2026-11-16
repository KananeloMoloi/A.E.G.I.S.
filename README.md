# A.E.G.I.S.
### Autonomous Engine for Governance, Intelligence & Security

> **Intelligence with Authority. Autonomy with Accountability.**

A.E.G.I.S. is a Python-based, multi-agent AI assistant powered locally through **Ollama**. It uses an agent manager to interpret a user's request and route it to a suitable specialised agent.

The current implementation includes a conversational **Chat Agent** and a **Research Agent**, both powered by the configured Ollama model (`qwen3:4b`).

A.E.G.I.S. is being developed around a broader vision: bringing autonomous task handling, intelligent assistance, governance, and security into one extensible system.

---

## Contents

- [Project overview](#project-overview)
- [Current features](#current-features)
- [Architecture](#architecture)
- [Technology stack](#technology-stack)
- [Requirements](#requirements)
- [Getting started](#getting-started)
- [Running A.E.G.I.S.](#running-aegis)
- [How agent routing works](#how-agent-routing-works)
- [Project structure](#project-structure)
- [Current limitations](#current-limitations)
- [Roadmap](#roadmap)
- [Contributing](#contributing)

---

## Project overview

A.E.G.I.S. is designed as a modular AI assistant rather than a single, fixed-purpose chatbot. When a user submits a request, the Agent Manager asks the AI model to decide whether the task is best handled by the Chat Agent or the Research Agent. The selected agent then processes the request and returns a response.

The project currently runs in a terminal and communicates with a locally hosted Ollama service.

### What A.E.G.I.S. stands for

| Letter | Meaning | Intended focus |
|---|---|---|
| **A** | Autonomous | Handling tasks within defined boundaries |
| **E** | Engine | The core processing and orchestration layer |
| **G** | Governance | Policies, permissions, and accountability |
| **I** | Intelligence | Reasoning, analysis, and decision support |
| **S** | Security | Protecting data, access, and operations |

These five pillars describe the project's broader direction. Not all five are implemented as software modules yet.

---

## Current features

- **Local model integration:** Sends chat requests to an Ollama server running on the local machine.
- **Agent management:** Maintains a registry of available agents and selects one for each request.
- **Chat Agent:** Handles general conversation, questions, explanations, and assistance.
- **Research Agent:** Handles research-oriented prompts using the model's available knowledge.
- **Command-line interface:** Provides an interactive terminal session.
- **Basic error handling:** Displays errors raised during request processing.
- **Exit command:** Type `exit` to close the application.

---

## Architecture

The current request flow is:

```text
                  USER
                    |
                    v
          A.E.G.I.S. CLI (main.py)
                    |
                    v
              AgentManager
                    |
          Selects an appropriate agent
                    |
             +------+------+
             |             |
             v             v
         Chat Agent    Research Agent
             |             |
             +------+------+
                    |
                    v
               OllamaAI
                    |
                    v
             Ollama API
                    |
                    v
              qwen3:4b
                    |
                    v
              AI RESPONSE
                    |
                    v
                  USER
```

### Main components

| Component | File | Responsibility |
|---|---|---|
| Application entry point | `backend/main.py` | Starts the terminal application and handles user input |
| Agent base class | `backend/agents/base.py` | Defines the common agent interface |
| Agent manager | `backend/agents/manager.py` | Chooses and runs the appropriate agent |
| Chat Agent | `backend/agents/chat.py` | Handles general conversation |
| Research Agent | `backend/agents/research.py` | Handles research-oriented requests |
| Ollama integration | `backend/ai/ollama.py` | Sends messages to Ollama and returns model responses |

---

## Technology stack

| Technology | Purpose |
|---|---|
| Python | Application logic and agent implementation |
| Ollama | Local model runtime and chat API |
| Qwen 3 4B (`qwen3:4b`) | Language model used by the current configuration |
| Requests | HTTP communication with the Ollama API |

---

## Requirements

Before running A.E.G.I.S., make sure you have:

1. Python installed.
2. [Ollama](https://ollama.com/) installed and running.
3. The `qwen3:4b` model downloaded in Ollama.
4. Internet access for the initial software and model downloads. Once installed, model requests are sent to the local Ollama service.

---

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/KananeloMoloi/A.E.G.I.S.git
cd A.E.G.I.S
```

### 2. Download the Ollama model

Make sure Ollama is installed, then run:

```bash
ollama pull qwen3:4b
```

Ensure the Ollama service is running. Ollama normally exposes its local API at:

```text
http://localhost:11434
```

### 3. Install the Python dependency

The current source code imports the `requests` package. Install it with:

```bash
python -m pip install requests
```

### 4. Start A.E.G.I.S.

Run the application from the `backend` directory so that its current package imports resolve correctly:

```bash
cd backend
python main.py
```

You should see the A.E.G.I.S. startup information in the terminal.

---

## Running A.E.G.I.S.

Once the application starts, enter a message at the prompt:

```text
YOU: Hello A.E.G.I.S.

[Agent Manager: Chat Agent]

A.E.G.I.S:
Hello! How can I help you today?
```

The exact response and agent selection depend on the model output.

To close the application:

```text
YOU: exit
```

---

## How agent routing works

The Agent Manager currently has two registered agents:

### Chat Agent

Use this agent for:
- General questions.
- Explanations.
- Everyday conversation.
- General assistance.

### Research Agent

Use this agent for:
- Research-oriented questions.
- Information analysis.
- Exploring a topic.
- Identifying what information would be useful to investigate.

**Current research limitation:** The Research Agent does not have internet-search functionality. It uses the configured language model and explicitly should not claim to have searched the internet. Its answers are based on the model's available knowledge and the information supplied in the prompt.

---

## Project structure

```text
A.E.G.I.S/
│
├── README.md
│
└── backend/
    │
    ├── main.py
    │
    ├── agents/
    │   ├── __init__.py
    │   ├── base.py
    │   ├── chat.py
    │   ├── manager.py
    │   └── research.py
    │
    └── ai/
        ├── __init__.py
        └── ollama.py
```

---

## Current limitations

A.E.G.I.S. is an evolving project. The following points describe the current codebase and should be considered before using it beyond local experimentation:

- The application currently runs through a command-line interface; no web or desktop interface is included in the inspected source.
- Only the Chat Agent and Research Agent are registered.
- Agent selection is performed by the language model, so routing is not guaranteed to be deterministic.
- The Research Agent does not perform live web searches or retrieve external sources.
- Dedicated governance, policy-enforcement, permissions, and security-monitoring modules are not yet implemented.
- The Ollama integration currently uses a fixed local endpoint and model configuration in the source.
- The current Ollama client prints the raw model response for debugging.

A.E.G.I.S. should therefore be treated as a development project, not as a production-ready security or governance platform.

---

## Roadmap

The following are potential development milestones, not claims about existing functionality.

- [ ] Improve agent selection and routing reliability.
- [ ] Add more specialised agents.
- [ ] Introduce configurable agent registration.
- [ ] Add conversation history and contextual memory.
- [ ] Implement a dedicated governance and policy layer.
- [ ] Introduce permission checks before sensitive actions.
- [ ] Add security monitoring and audit logging.
- [ ] Add optional research tools with source attribution.
- [ ] Build a user-friendly graphical interface.
- [ ] Add automated tests and deployment documentation.

---

## Contributing

Contributions, suggestions, and technical feedback are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test the changes locally.
5. Submit a pull request describing what changed and why.

For major changes, open an issue first so the proposed direction can be discussed.

---

## Security

Do not commit passwords, API keys, tokens, or other secrets.

Keep local environment files such as `.env` out of version control. If a secret has already been committed or shared, revoke or rotate it. A `.gitignore` file should be used to exclude local environment files, Python cache directories, and other generated files.

---

## Project

**A.E.G.I.S. — Autonomous Engine for Governance, Intelligence & Security**

GitHub: https://github.com/KananeloMoloi/A.E.G.I.S

> Building intelligent systems that can think, act, and execute — without losing control of what they do.

**A.E.G.I.S. — Intelligence with Authority. Autonomy with Accountability.**
