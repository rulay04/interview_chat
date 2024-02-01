from flask import Flask, render_template, request
from interview import chatbot

app = Flask(__name__, static_url_path='/static')

# Keep track of chat history
chat_history = []

@app.route('/')
def index():
    return render_template('index.html', chat_history=chat_history)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    bot_response = chatbot(user_input)

    # Add user and bot messages to chat history
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "bot", "content": bot_response})

    return render_template('index.html', chat_history=chat_history)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
