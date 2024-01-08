import requests

def send_comment_to_ollama(comment_text):
    ollama_url = 'http://127.0.0.1:11434/api/endpoint' 
    data = {'comment': comment_text}

    response = requests.post(ollama_url, json=data)

    if response.status_code == 200:
        result = response.json()
        if result['sentiment'] == 'positive':
            print(f"Komentarz '{comment_text}' jest pozytywny.")
        elif result['sentiment'] == 'negative':
            print(f"Komentarz '{comment_text}' jest negatywny.")
        else:
            print(f"Komentarz '{comment_text}' ma neutralny sentyment.")
    else:
        print(f"Błąd przy wysyłaniu komentarza do OllaMa. Status code: {response.status_code}")

