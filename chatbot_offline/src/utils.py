import requests
import json

def call_ollama_model(model, prompt, stream=False):

    url = 'http://localhost:11434/api/generate'
    params = {
        'model': model,
        'prompt': prompt,
        'stream': stream
    }

    payload = json.dumps(params)
    response = requests.post(url, data=payload,
                            headers={'Content-Type': 'application/json'})
    
    if response.status_code != 200:
        return 'ERROR'
    
    else:
        
        return response.json()['response']
        

if __name__ == '__main__':
    model = 'qwen2.5-coder:7b'
    prompt = input('Ask Your Question: ')
    result = call_ollama_model(model, prompt)
    print(result)