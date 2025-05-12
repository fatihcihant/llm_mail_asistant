# Gmail-LLM-Assistant
A Python-based Gmail assistant using the Gemini 2.5 Flash model to read, summarize, and categorize emails, detect urgent ones, and generate draft replies.
## Features

- **Authenticate with Gmail API using OAuth2.
- **Fetch and summarize emails with Gemini 2.5 Flash.
- **Detect urgent emails and notify via console.
- **Categorize emails by sentiment (positive, negative, neutral).
- **Generate draft replies for urgent emails.

## Prerequisites

Python 3.12
uv package manager
Google Cloud project with Gmail API enabled
Gemini API key from Google AI Studio

## Setup

### Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env
```

### Install uv with pip:
```bash
pip install uv
```

### Clone the repository:
```bash
git clone https://github.com/fatihcihant/llm_mail_asistant.git
cd Gmail-LLM-Assistant
```

### Set up Python environment:
```bash
uv python install 3.12
uv sync
```


### Configure Gmail API:

Go to Google Cloud Console.
Create a project and enable the Gmail API.
Create OAuth 2.0 credentials (select "Desktop app") and download credentials.json.
Place credentials.json in the project root.
If you encountered permission denied problem you have to assign target email adress to test user.
-> Google Cloud Console → APIs & Services → OAuth Consent Screen → Test user → ADD USERS



### Set up Gemini API:

Get an API key from Google AI Studio.
Create a .env file in the project root:GEMINI_API_KEY=your_api_key_here




## Run the application:
uv run python src/main.py



## Project Structure

```
LLM-Mail-Assistant/
├── src/
│   ├── agents/
│   │   ├── email_fetcher.py
│   │   ├── email_processor.py
│   │   └── notification_agent.py
│   ├── utils/
│   │   ├── gmail_api.py
│   │   ├── gemini_api.py
│   │   └── config.py
│   └── main.py
├── credentials.json
├── settings.yaml
├── .gitignore
├── README.md
├── LICENSE
├── pyproject.toml
├── .python-version
└── .env

```


src/agents/: Agent classes for fetching, processing, and notifying.

src/utils/: Utility functions for Gmail and Gemini APIs.

settings.yaml: Configuration for adjustable parameters.

main.py: Entry point to run the assistant.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.
