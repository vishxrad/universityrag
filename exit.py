import re
import requests
import json

# Function to clean text: remove special characters, lowercase, etc.
def clean_text(text):
    # Remove special characters and numbers
    text = re.sub(r'[^A-Za-z\s]', '', text)
    # Convert to lowercase
    text = text.lower().strip()
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)
    return text

# Function to get embeddings using Ollama Mistral API
def get_ollama_embeddings(text, model="mistral"):
    url = "https://api.ollama.com/v1/embeddings"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer <YOUR_OLLAMA_API_KEY>"
    }
    
    # Payload for the API request
    payload = {
        "model": model,
        "prompt": text
    }
    
    # Make API request
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        embeddings = response.json().get("embeddings", [])
        return embeddings
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Main function to clean text and get embeddings
def process_text_file(file_path):
    # Read the text file with UTF-8 encoding
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except UnicodeDecodeError:
        print("Error: Unable to decode the file. Please check the file's encoding.")
        return

    # Clean the text
    cleaned_text = clean_text(text)
    print(f"Cleaned Text: {cleaned_text}")
    
    # Get embeddings from Ollama Mistral model
    embeddings = get_ollama_embeddings(cleaned_text)
    
    if embeddings:
        print(f"Embeddings: {embeddings}")
    else:
        print("Failed to retrieve embeddings.")

# Usage
file_path = "vault.txt"  # Specify your text file path
process_text_file(file_path)
