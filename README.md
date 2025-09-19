# MobileLLM Chat Interface

A beautiful web-based chat interface for Facebook's MobileLLM-R1-950M model. This application allows you to chat with the model in different modes: Math Assistant, C++ Assistant, and Python Assistant.

## Features

- 🎨 Modern, responsive web interface
- 🤖 Three conversation modes:
  - **Math Assistant**: Step-by-step mathematical reasoning
  - **C++ Assistant**: C++ programming help with code formatting
  - **Python Assistant**: Python programming assistance
- 💬 Real-time chat interface
- 🔄 Conversation history maintained during session
- 🚀 No API key required - uses local model

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. The model will be automatically downloaded on first run (approximately 1.8GB)

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Select your preferred conversation mode from the dropdown
4. Start chatting with the model!

## Model Information

- **Model**: facebook/MobileLLM-R1-950M
- **Type**: Local model (no API key required)
- **Size**: ~1.8GB
- **Capabilities**: Text generation, mathematical reasoning, code generation

## API Endpoints

- `GET /` - Main chat interface
- `POST /chat` - Send message to the model
- `GET /modes` - Get available conversation modes

## Conversation Modes

### Math Assistant
- Provides step-by-step mathematical reasoning
- Formats final answers in `\boxed{}` notation
- Ideal for solving mathematical problems

### C++ Assistant
- Specialized in C++ programming
- Provides formatted code blocks with `cpp` syntax highlighting
- Includes step-by-step explanations

### Python Assistant
- Focused on Python programming
- Delivers code with `python` syntax highlighting
- Offers detailed explanations and best practices

## Technical Details

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Model**: Hugging Face Transformers
- **Device**: Auto-detection (CPU/GPU)

## Troubleshooting

- If the model fails to load, ensure you have sufficient disk space (~2GB)
- For GPU acceleration, ensure PyTorch is installed with CUDA support
- If the web interface doesn't load, check that Flask is running on port 5000

## License

This project uses the MobileLLM model from Facebook/Meta. Please refer to the model's license for usage terms.

