# University Chatbot with RAG, Ollama, and Intel Extension for PyTorch

This project implements a chatbot for university information using Retrieval-Augmented Generation (RAG) and Ollama with the Mistral model. The chatbot is designed to answer queries about a university using its prospectus and is optimized to run on Intel CPUs using Intel Extension for PyTorch (IPEX).

## Features

- Uses RAG (Retrieval-Augmented Generation) for context-aware responses
- Integrates Ollama with the Mistral model for natural language processing
- Embeds and retrieves relevant information from a university prospectus
- Supports query rewriting for improved context understanding
- Optimized with Intel Extension for PyTorch (IPEX) for enhanced performance on Intel hardware
- Provides colorized console output for better readability

## Prerequisites

- Python 3.7+
- Ollama installed and running locally
- Intel CPUs for optimized performance with Intel Extension for PyTorch

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
3. Install Intel Extension for PyTorch to optimize performance on Intel CPUs:
   ```
   pip install intel-extension-for-pytorch
   ```

## Usage

1. Prepare your university prospectus data in a file named `vault2.txt`.

2. Run the chatbot:
   ```
   python ollamaragbutintel.py
   ```
3. Start asking questions about the university. Type 'quit' to exit the program.

# Enabling Intel Optimizations
To take advantage of Intel optimizations, you can modify the chatbot code to use Intel Extension for PyTorch (IPEX). Below is an example of how to apply Intel's optimizations when running the chatbot:
```python
import intel_extension_for_pytorch as ipex
import torch

# Example: Define a simple model (replace with your actual model)
model = torch.nn.Linear(10, 5)

# Optimize the model with Intel Extension for PyTorch
model = ipex.optimize(model)
```
Once optimized, proceed with your usual inference or training. The IPEX optimizations will boost performance on Intel hardware.
```python
# Example input tensor
input_tensor = torch.randn(64, 10)

# Run inference with the optimized model
output = model(input_tensor)
```

## How it works

1. The script loads the university prospectus data from `vault2.txt`.
2. It generates embeddings for each line in the prospectus using Ollama's embedding model.
3. When a user asks a question, the script:
   - Rewrites the query for better context understanding
   - Retrieves relevant context from the prospectus using cosine similarity
   - Generates a response using the Mistral model via Ollama
   - Optimizes the model using Intel Extension for PyTorch to speed up inference
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
- intel-extension-for-pytorch

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Sample
![image](https://github.com/user-attachments/assets/8adb6fba-2c97-4bb4-8a15-3a6c481919dd)

