import requests

def generate_llama_response(comment: str):
    ollama_url = 'http://localhost:11434/api/generate' 
    data = {
        "model": "llama2",
        "prompt": comment,
        "stream": False
    }

    try:
        response = requests.post(ollama_url, json=data)
        response.raise_for_status()
        result = response.json()
        return result
    except requests.exceptions.RequestException as e:
        print(f"Błąd przy wysyłaniu zapytania do OllaMa: {e}")
        return None
