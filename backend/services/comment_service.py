import requests
import json
from schemas.comment_schema import CommentItem

ollama_url = 'http://ollama:11434/api/generate'

def toxic_classify(comment):
#     dict_comment = dict(comment)
#     json_comment = json.dumps(dict_comment)
#     prompt = json.dumps(json_comment) #CRAZY THINGS ARE GOING HERE!!
    data = {
        "model": "llama2-toxic",
        "prompt": "[{'username': 'user123', 'id': 1, 'comment': 'Hello, how are you'}, {'username': 'user13', 'id': 2, 'comment': 'Kill yourself'}]",
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


#TODO TRANSFORM DATA TO EASILY PARSE ARRAY OF JSON

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
