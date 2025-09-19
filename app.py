from flask import Flask, render_template, request, jsonify
from transformers import pipeline
import torch
import json

app = Flask(__name__)

# Initialize the model
model_id = "facebook/MobileLLM-R1-950M"

# Try to load the model with error handling
try:
    pipe = pipeline(
        "text-generation",
        model=model_id,
        dtype="auto",
        trust_remote_code=True,  # Allow custom model code
    )
    print(f"Model {model_id} loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    print("Falling back to a compatible model...")
    # Fallback to a more compatible model
    model_id = "microsoft/DialoGPT-medium"
    pipe = pipeline(
        "text-generation",
        model=model_id,
        dtype="auto",
    )

# Conversation modes
CONVERSATION_MODES = {
    "math": {
        "system_prompt": "Please reason step by step, and put your final answer within \\boxed{}.",
        "name": "Math Assistant"
    },
    "cpp": {
        "system_prompt": (
            "\nYou are a helpful and harmless assistant. You should think step-by-step before responding to the instruction below.\n\n"
            "Please use c++ programming language only.\n"
            "You must use ```cpp for just the final solution code block with the following format:\n"
            "```cpp\n# Your code here\n```\n"
        ),
        "name": "C++ Assistant"
    },
    "python": {
        "system_prompt": (
            "\nYou are a helpful and harmless assistant. You should think step-by-step before responding to the instruction below.\n\n"
            "Please use python programming language only.\n"
            "You must use ```python for just the final solution code block with the following format:\n"
            "```python\n# Your code here\n```\n"
        ),
        "name": "Python Assistant"
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        mode = data.get('mode', 'math')
        conversation_history = data.get('history', [])
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Build messages array
        messages = [
            {
                "role": "system",
                "content": CONVERSATION_MODES[mode]["system_prompt"]
            }
        ]
        
        # Add conversation history
        messages.extend(conversation_history)
        
        # Add current user message
        messages.append({
            "role": "user",
            "content": user_message
        })
        
        # Generate response
        outputs = pipe(
            messages,
            max_new_tokens=8192,
        )
        
        # Extract the assistant's response
        response = outputs[0]["generated_text"][-1]["content"]
        
        return jsonify({
            'response': response,
            'mode': mode
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/modes')
def get_modes():
    return jsonify(CONVERSATION_MODES)

if __name__ == '__main__':
    print("Starting MobileLLM Chat Interface...")
    print("Model loaded: facebook/MobileLLM-R1-950M")
    print("No API key required - using local model")
    app.run(debug=True, host='0.0.0.0', port=5000)
