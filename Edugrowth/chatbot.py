from flask import Flask, render_template, request, jsonify 
import google as genai
import os

# Configure Gemini API Key
genai.configure(api_key=os.getenv('use_your_Gemini_API_Key'))  # Use environment variable for API key

# Initialize Model
model = genai.GenerativeModel('gemini-pro')
chat_session = model.start_chat(history=[])

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')
    if user_message:
        try:
            response = chat_session.send_message(user_message)
            bot_reply = response.text
            return jsonify({'response': bot_reply})
        except Exception as e:
            return jsonify({'response': f"Error: {str(e)}"}), 500
    return jsonify({'response': "No message received."}), 400

if __name__ == '__main__':
    app.run(debug=True)