from flask import Flask, render_template, request, Response
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    ollama_url = 'http://localhost:11434/api/generate'
    #ollama_url = 'http://172.26.190.53:11434/api/generate'
    data = {
        'model': 'deepseek-r1:1.5b',  # Replace with your actual model name
        'prompt': user_message,
        #"format": "json",
        'stream': True
    }
    
    try:
        response = requests.post(ollama_url, json=data, stream=True)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return Response(f"Error connecting to Ollama: {str(e)}", status=500)

    def generate():
        for line in response.iter_lines():
            if line:
                try:
                    json_chunk = json.loads(line.decode('utf-8'))
                    yield json_chunk.get('response', '')
                except json.JSONDecodeError:
                    continue

    return Response(generate(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
