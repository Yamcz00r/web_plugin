import requests
import json
from schemas.comment_schema import CommentItem

ollama_url = 'http://ollama:11434/api/generate'


def toxic_classify(comments):
    
    data = {
        "model": "toxic-model",
        "prompt": comments,
        "format": "json",
        "stream": False
    }



    try:
        response = requests.post(ollama_url, json=data)
        response.raise_for_status()
        result = response.json()

        return result['response']
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(req_err)




