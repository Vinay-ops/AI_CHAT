# AI Chat

A simple AI chat application built with Python, featuring a modern GUI using CustomTkinter and powered by Groq's AI API.

## Features

- Clean, modern dark-themed interface
- Real-time chat with AI assistant
- Conversation history maintained during session
- Send messages via button click or Enter key
- Powered by Llama 3.1 8B Instant model via Groq API

## Prerequisites

- Python 3.7 or higher
- Groq API key (get one from [Groq Console](https://console.groq.com/))

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd ai-chat
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`

4. Install the required dependencies:
   ```bash
   pip install customtkinter openai
   ```

## Setup

1. Get your Groq API key from [Groq Console](https://console.groq.com/)

2. Set the API key as an environment variable:
   - Windows: `set GROQ_API_KEY=your_api_key_here`
   - macOS/Linux: `export GROQ_API_KEY=your_api_key_here`

   Or create a `.env` file in the project root with:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Usage

Run the application:
```bash
python main.py
```

- Type your message in the input field
- Click "Send" button or press Enter to send
- Chat with the AI assistant in real-time

## Dependencies

- `customtkinter` - Modern GUI framework for Tkinter
- `openai` - OpenAI Python client (used for Groq API)

## License

This project is open source. Feel free to use and modify as needed.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.