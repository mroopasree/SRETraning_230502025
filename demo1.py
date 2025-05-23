from flask import Flask, request, jsonify, render_template
import openai  # LLM API client

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_input = data.get('question', '')

    if not user_input:
        return jsonify({'error': 'No question provided'}), 400

    # Call OpenAI API for completion
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7
        )
        answer = response.choices[0].text.strip()
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)