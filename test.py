#!/usr/bin/env python3
"""
AI Chat Pro Test Script
Test the AI Chat Pro installation and API connection
"""

import os
import sys

def test_imports():
    """Test if all required packages can be imported"""
    print("Testing imports...")
    try:
        import customtkinter as ctk
        print("✅ CustomTkinter imported successfully")
        import openai
        print("✅ OpenAI imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False

def test_api_connection():
    """Test connection to Groq API"""
    print("\nTesting API connection...")
    api_key = os.environ.get("GROQ_API_KEY")

    if not api_key:
        print("❌ GROQ_API_KEY not found in environment variables")
        return False

    try:
        from openai import OpenAI
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.groq.com/openai/v1"
        )

        # Test with a simple message
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": "Hello, just testing the API connection. Please respond with 'API test successful!'"}],
            max_tokens=50
        )

        reply = response.choices[0].message.content.strip()
        if "API test successful" in reply:
            print("✅ API connection successful!")
            print(f"Response: {reply}")
            return True
        else:
            print(f"❌ Unexpected response: {reply}")
            return False

    except Exception as e:
        print(f"❌ API test failed: {e}")
        return False

def main():
    print("🧪 AI Chat Pro Test Suite")
    print("=" * 30)

    success = True

    if not test_imports():
        success = False

    if not test_api_connection():
        success = False

    print("\n" + "=" * 30)
    if success:
        print("🎉 All tests passed! AI Chat Pro is ready to run.")
        print("Launch with: python main.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()