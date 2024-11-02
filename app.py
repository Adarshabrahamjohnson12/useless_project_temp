from flask import Flask, render_template, jsonify, request
from together import Together

app = Flask(__name__)

# Initialize the Together client
client = Together(api_key='e7a501a28a46881b3559d8599dd96cf6bb100fe303fc4cfa67f02c023b193d41')

# Prompt templates
PROMPT_TEMPLATES = {
    '1': "Write a hilariously absurd excuse for why someone was late to work because of a pet raccoon.",
    '2': "Make up a funny excuse for missing an assignment involving aliens.",
    '3': "Write a ridiculous reason for forgetting an anniversary, preferably involving talking animals or time travel.",
    '4': "Give a silly excuse for not attending a friend's party because of a highly unusual reason.",
    '5': "Create a bizarre reason for avoiding household chores, involving imaginary creatures."
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-excuse', methods=['POST'])
def generate_excuse():
    category = request.json.get('category')
    messages = [{"role": "user", "content": PROMPT_TEMPLATES[category]}]

    completion = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        messages=messages
    )

    if completion and hasattr(completion, 'choices') and len(completion.choices) > 0:
        excuse = completion.choices[0].message.content.strip()
        return jsonify({'excuse': excuse})

    return jsonify({'error': 'No excuse generated. Please try again.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
