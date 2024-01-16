import requests
import json
from schemas.comment_schema import CommentItem

ollama_url = 'http://localhost:11434/api/generate'


def toxic_classify(comment):
    data = {
        "model": "llama2-toxic",
        "prompt": dict(comment),
        "stream": False,
        "format": "json"
    }
    try:
        response = requests.post(ollama_url, json=data)
        response.raise_for_status()
        result = response.json()
        print(result)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")


#TODO TRY TO FIGURE OUT WHY REQUEST DOSENT WORK

def generate_llama_response(comment: CommentItem):

    data = {
        "model": "llama2-toxic",
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
