# University Chatbot with RAG and Ollama

This project implements a chatbot for university information using Retrieval-Augmented Generation (RAG) and Ollama with the Mistral model. The chatbot is designed to answer queries about a university using its prospectus.

## Features

- Uses RAG (Retrieval-Augmented Generation) for context-aware responses
- Integrates Ollama with the Mistral model for natural language processing
- Embeds and retrieves relevant information from a university prospectus
- Supports query rewriting for improved context understanding
- Provides colorized console output for better readability

## Prerequisites

- Python 3.7+
- Ollama installed and running locally

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/university-chatbot.git
   cd university-chatbot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Prepare your university prospectus data in a file named `vault2.txt`.

2. Run the chatbot:
   ```
   python main.py --model mistral
   ```

3. Start asking questions about the university. Type 'quit' to exit the program.

## How it works

1. The script loads the university prospectus data from `vault2.txt`.
2. It generates embeddings for each line in the prospectus using Ollama's embedding model.
3. When a user asks a question, the script:
   - Rewrites the query for better context understanding
   - Retrieves relevant context from the prospectus using cosine similarity
   - Generates a response using the Mistral model via Ollama
   - Maintains a conversation history for context-aware responses

## Dependencies

- openai
- torch
- PyPDF2
- ollama
- pyyaml
- beautifulsoup4
- lxml
- python-dotenv

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
