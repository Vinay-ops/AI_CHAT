import os
import customtkinter as ctk
from openai import OpenAI

# Create the API client using Groq
# API key is taken from environment variable
client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

# Set dark mode
ctk.set_appearance_mode("dark")

# Set color theme
ctk.set_default_color_theme("blue")

# Create main window
app = ctk.CTk()
app.title("AI Chat")
app.geometry("500x500")
app.resizable(False, False)

# This list will store all chat messages
messages = []

# Text box to display chat
chat_box = ctk.CTkTextbox(app, width=460, height=380)
chat_box.pack(pady=10)
chat_box.configure(state="disabled")

# Entry box for user input
user_entry = ctk.CTkEntry(app, width=360)
user_entry.pack(side="left", padx=10, pady=10)

# Button to send message
send_button = ctk.CTkButton(app, text="Send")
send_button.pack(side="right", padx=10, pady=10)

# Function to send message
def send_message():
    user_text = user_entry.get().strip()

    # If user did not type anything
    if not user_text:
        return

    # Show user message in chat box
    chat_box.configure(state="normal")
    chat_box.insert("end", "You: " + user_text + "\n")
    chat_box.see("end")

    # Clear input box
    user_entry.delete(0, "end")

    # Store user message
    messages.append({
        "role": "user",
        "content": user_text
    })

    # Call AI API
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    # Get AI reply
    reply = response.choices[0].message.content

    # Show AI reply
    chat_box.configure(state="normal")
    chat_box.insert("end", "Bot: " + reply + "\n\n")
    chat_box.configure(state="disabled")
    chat_box.see("end")

    # Store AI reply
    messages.append({
        "role": "assistant",
        "content": reply
    })

# Button click sends message
send_button.configure(command=send_message)

# Press Enter key to send message
app.bind("<Return>", lambda event: send_message())

# Start the app
app.mainloop()
