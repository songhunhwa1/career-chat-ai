from flask import Flask, request, jsonify, render_template
import openai
import os
from dotenv import load_dotenv
from urllib.parse import quote as url_quote

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a career consultant."},
            {"role": "user", "content": user_input},
        ]
    )
    return jsonify({"response": response.choices[0].message['content']})

if __name__ == '__main__':
    app.run(debug=True)
