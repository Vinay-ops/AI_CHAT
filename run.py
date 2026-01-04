#!/usr/bin/env python3
"""
AI Chat Pro Launcher
Quick launcher script for AI Chat Pro
"""

import os
import sys
from pathlib import Path

def check_requirements():
    """Check if required packages are installed"""
    try:
        import customtkinter
        import openai
        print("✅ All requirements satisfied!")
        return True
    except ImportError as e:
        print(f"❌ Missing requirement: {e}")
        print("Run: pip install -r requirements.txt")
        return False

def check_api_key():
    """Check if GROQ_API_KEY is set"""
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("❌ GROQ_API_KEY environment variable not set!")
        print("Get your key from: https://console.groq.com/")
        print("Set it with: export GROQ_API_KEY=your_key_here")
        return False
    print("✅ API key found!")
    return True

def main():
    print("🚀 Starting AI Chat Pro...")

    if not check_requirements():
        sys.exit(1)

    if not check_api_key():
        sys.exit(1)

    # Import and run the main app
    try:
        from main import AIChatApp
        app = AIChatApp()
        app.run()
    except Exception as e:
        print(f"❌ Error starting app: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()