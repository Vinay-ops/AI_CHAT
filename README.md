# 🤖 AI Chat Pro

<div align="center">

![AI Chat Pro](https://img.shields.io/badge/AI_Chat-Pro-FF6B6B?style=for-the-badge&logo=robot&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.2+-1F77B4?style=for-the-badge&logo=tkinter&logoColor=white)
![Groq](https://img.shields.io/badge/Powered_by-Groq-FF6B6B?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEyIDJDMTMuMSAyIDE0IDIuOSAxNCA0VjIwQzE0IDIxLjEgMTMuMSAyMiAxMiAyMkg0QzIuOSAyMiAyIDIxLjEgMiAyMFY0QzIgMi45IDIuOSAyIDQgMkgxMkMxMy4xIDIgMTQgMi45IDE0IDRWNFoiIGZpbGw9IiNGRjZCNkIiLz4KPC9zdmc+)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/Vinay-ops/AI_CHAT?style=social)](https://github.com/Vinay-ops/AI_CHAT)
[![GitHub forks](https://img.shields.io/github/forks/Vinay-ops/AI_CHAT?style=social)](https://github.com/Vinay-ops/AI_CHAT)

**🚀 The fastest way to chat with AI - Powered by Groq's lightning-fast inference**

[📥 Download](#installation) • [🎯 Features](#features) • [📖 Documentation](#documentation) • [🤝 Contributing](#contributing)

</div>

---

## ✨ What is AI Chat Pro?

AI Chat Pro is a **modern, beautiful, and incredibly fast** AI chat application that brings the power of cutting-edge AI models directly to your desktop. Built with love using Python and powered by [Groq](https://groq.com)'s revolutionary inference technology, it delivers responses in milliseconds rather than seconds.

> **⚡ Why choose AI Chat Pro?** Because waiting for AI responses shouldn't feel like waiting for your coffee to brew!

## 🎯 Features

### 🚀 Core Features
- **⚡ Lightning Fast**: Powered by Groq's ultra-fast inference API
- **🎨 Modern UI**: Beautiful dark-themed interface with smooth animations
- **🤖 Multiple Models**: Choose from Llama 3.1, Mixtral, and more
- **💬 Real-time Chat**: Instant messaging with typing indicators
- **📱 Responsive Design**: Works perfectly on different screen sizes

### 🛠️ Advanced Features
- **💾 Export Conversations**: Save chats as TXT or JSON files
- **🗑️ Clear Chat History**: Start fresh conversations anytime
- **⚙️ Customizable Settings**: Switch themes and color schemes
- **⌨️ Keyboard Shortcuts**: Enter to send, Ctrl+Enter for new lines
- **🎯 Smart Error Handling**: Graceful error messages and recovery
- **🕒 Message Timestamps**: Track when messages were sent
- **🎨 Syntax Highlighting**: Color-coded messages for better readability

### 🎪 User Experience
- **🌙 Dark Mode First**: Eye-friendly dark theme by default
- **🎭 Multiple Themes**: Light, Dark, and System themes
- **🌈 Color Schemes**: Blue, Green, and Dark Blue themes
- **📝 Rich Text Display**: Formatted messages with emojis
- **🔄 Async Processing**: Non-blocking UI during AI responses

## 📸 Screenshots

<div align="center">

### Main Interface
![Main Interface](https://via.placeholder.com/600x400/1a1a1a/00ff88?text=AI+Chat+Pro+Interface)

### Model Selection
![Model Selection](https://via.placeholder.com/600x400/1a1a1a/0088ff?text=Model+Selection)

### Settings Panel
![Settings](https://via.placeholder.com/600x400/1a1a1a/ff4444?text=Settings+Panel)

</div>

## 🛠️ Installation

### Prerequisites
- **Python 3.8 or higher** 🐍
- **Groq API Key** (free at [console.groq.com](https://console.groq.com))

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Vinay-ops/AI_CHAT.git
   cd AI_CHAT
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**
   ```bash
   # Windows
   set GROQ_API_KEY=your_api_key_here

   # macOS/Linux
   export GROQ_API_KEY=your_api_key_here
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

### 🐳 Docker Installation (Coming Soon)
```bash
docker run -e GROQ_API_KEY=your_key vinay-ops/ai-chat-pro:latest
```

## 🚀 Usage

### Basic Chat
1. Launch the application
2. Select your preferred AI model
3. Type your message and press Enter or click Send
4. Enjoy lightning-fast AI responses!

### Advanced Features
- **Export Chat**: Click "💾 Export" to save conversations
- **Clear Chat**: Click "🗑️ Clear Chat" to start fresh
- **Settings**: Click "⚙️ Settings" to customize appearance
- **About**: Click "ℹ️ About" for app information

### Keyboard Shortcuts
- `Enter`: Send message
- `Ctrl + Enter`: New line
- `Ctrl + S`: Export chat (when input focused)

## 📊 Performance

| Model | Response Time | Quality | Use Case |
|-------|---------------|---------|----------|
| Llama 3.1 8B | ⚡ ~0.5s | ⭐⭐⭐⭐⭐ | General chat |
| Llama 3.1 70B | ⚡ ~1.2s | ⭐⭐⭐⭐⭐ | Complex tasks |
| Mixtral 8x7B | ⚡ ~0.8s | ⭐⭐⭐⭐⭐ | Code & math |

## 🏗️ Architecture

```
AI Chat Pro/
├── main.py              # Main application with AIChatApp class
├── requirements.txt     # Python dependencies
├── pyproject.toml       # Modern Python packaging
├── README.md           # This file
├── LICENSE             # MIT License
└── .gitignore         # Git ignore rules
```

## 🤝 Contributing

We love contributions! Here's how you can help:

### Ways to Contribute
- 🐛 **Bug Reports**: Found a bug? [Open an issue](https://github.com/Vinay-ops/AI_CHAT/issues)
- 💡 **Feature Requests**: Have an idea? [Suggest it](https://github.com/Vinay-ops/AI_CHAT/issues)
- 🛠️ **Code Contributions**: Fork, code, and submit a PR
- 📖 **Documentation**: Help improve docs and tutorials
- 🎨 **UI/UX**: Design improvements welcome

### Development Setup
```bash
git clone https://github.com/Vinay-ops/AI_CHAT.git
cd AI_CHAT
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Code Style
- Follow PEP 8
- Use type hints
- Write docstrings
- Test your changes

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Groq** for their amazing inference API
- **CustomTkinter** for the beautiful UI framework
- **OpenAI** for the Python client library
- **The Python Community** for making this possible

## 📞 Support

- 📧 **Email**: support@ai-chat-pro.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/Vinay-ops/AI_CHAT/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Vinay-ops/AI_CHAT/discussions)

## 🎉 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Vinay-ops/AI_CHAT&type=Date)](https://star-history.com/#Vinay-ops/AI_CHAT&Date)

---

<div align="center">

**Made with ❤️ by the AI Chat Pro Team**

[🌟 Star us on GitHub](https://github.com/Vinay-ops/AI_CHAT) • [🐛 Report Issues](https://github.com/Vinay-ops/AI_CHAT/issues) • [💝 Donate](https://www.paypal.me/vinaybhogal)

</div>