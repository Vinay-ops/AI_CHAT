import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
import customtkinter as ctk
from openai import OpenAI
import threading
import time

class AIChatApp:
    def __init__(self):
        # Initialize API client
        try:
            self.client = OpenAI(
                api_key=os.environ["GROQ_API_KEY"],
                base_url="https://api.groq.com/openai/v1"
            )
        except KeyError:
            messagebox.showerror("Error", "Please set GROQ_API_KEY environment variable")
            exit(1)

        # Configure appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Initialize variables
        self.messages = []
        self.is_typing = False
        self.current_model = "llama-3.1-8b-instant"

        # Available models
        self.models = {
            "Llama 3.1 8B": "llama-3.1-8b-instant",
            "Llama 3.1 70B": "llama-3.1-70b-versatile",
            "Mixtral 8x7B": "mixtral-8x7b-32768"
        }

        self.setup_ui()

    def setup_ui(self):
        # Create main window
        self.app = ctk.CTk()
        self.app.title("🤖 AI Chat Pro - Powered by Groq")
        self.app.geometry("700x600")
        self.app.resizable(True, True)

        # Create menu bar
        self.create_menu_bar()

        # Create main frame
        main_frame = ctk.CTkFrame(self.app)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Title
        title_label = ctk.CTkLabel(main_frame, text="AI Chat Pro", font=("Arial", 20, "bold"))
        title_label.pack(pady=(10, 5))

        # Model selector
        model_frame = ctk.CTkFrame(main_frame)
        model_frame.pack(fill="x", padx=10, pady=(0, 10))

        model_label = ctk.CTkLabel(model_frame, text="Model:", font=("Arial", 12))
        model_label.pack(side="left", padx=(10, 5))

        self.model_var = ctk.StringVar(value="Llama 3.1 8B")
        model_menu = ctk.CTkOptionMenu(model_frame, variable=self.model_var,
                                     values=list(self.models.keys()),
                                     command=self.change_model)
        model_menu.pack(side="left", padx=(0, 10))

        # Typing indicator
        self.typing_label = ctk.CTkLabel(model_frame, text="", text_color="gray")
        self.typing_label.pack(side="right", padx=10)

        # Chat display frame
        chat_frame = ctk.CTkFrame(main_frame)
        chat_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        # Chat textbox with scrollbar
        self.chat_box = ctk.CTkTextbox(chat_frame, wrap="word", font=("Arial", 11))
        self.chat_box.pack(fill="both", expand=True, padx=10, pady=10)
        self.chat_box.configure(state="disabled")

        # Input frame
        input_frame = ctk.CTkFrame(main_frame)
        input_frame.pack(fill="x", padx=10, pady=(0, 10))

        # User input entry
        self.user_entry = ctk.CTkEntry(input_frame, placeholder_text="Type your message here...",
                                     font=("Arial", 11))
        self.user_entry.pack(side="left", fill="x", expand=True, padx=(10, 5), pady=10)

        # Send button
        self.send_button = ctk.CTkButton(input_frame, text="📤 Send", command=self.send_message,
                                       font=("Arial", 11, "bold"))
        self.send_button.pack(side="right", padx=(0, 10), pady=10)

        # Bind Enter key
        self.app.bind("<Return>", lambda event: self.send_message())
        self.app.bind("<Control-Return>", lambda event: self.user_entry.insert("end", "\n"))

        # Status bar
        self.status_label = ctk.CTkLabel(main_frame, text="Ready to chat! 🚀",
                                       font=("Arial", 10), text_color="gray")
        self.status_label.pack(pady=(0, 5))

    def create_menu_bar(self):
        # Create menu bar frame
        menu_frame = ctk.CTkFrame(self.app, height=40)
        menu_frame.pack(fill="x", padx=10, pady=(10, 0))

        # Menu buttons
        clear_btn = ctk.CTkButton(menu_frame, text="🗑️ Clear Chat", command=self.clear_chat,
                                width=100, height=30, font=("Arial", 10))
        clear_btn.pack(side="left", padx=(10, 5))

        export_btn = ctk.CTkButton(menu_frame, text="💾 Export", command=self.export_chat,
                                 width=100, height=30, font=("Arial", 10))
        export_btn.pack(side="left", padx=(0, 5))

        settings_btn = ctk.CTkButton(menu_frame, text="⚙️ Settings", command=self.show_settings,
                                   width=100, height=30, font=("Arial", 10))
        settings_btn.pack(side="left", padx=(0, 5))

        about_btn = ctk.CTkButton(menu_frame, text="ℹ️ About", command=self.show_about,
                                width=100, height=30, font=("Arial", 10))
        about_btn.pack(side="right", padx=(0, 10))

    def change_model(self, model_name):
        self.current_model = self.models[model_name]
        self.status_label.configure(text=f"Switched to {model_name} 🤖")

    def send_message(self):
        user_text = self.user_entry.get().strip()
        if not user_text:
            return

        # Disable input while processing
        self.send_button.configure(state="disabled")
        self.user_entry.configure(state="disabled")

        # Display user message
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.display_message(f"👤 You [{timestamp}]\n{user_text}\n", "user")

        # Clear input
        self.user_entry.delete(0, "end")

        # Store user message
        self.messages.append({"role": "user", "content": user_text})

        # Start AI response in separate thread
        threading.Thread(target=self.get_ai_response, daemon=True).start()

    def get_ai_response(self):
        try:
            # Show typing indicator
            self.show_typing_indicator()

            # Get AI response
            response = self.client.chat.completions.create(
                model=self.current_model,
                messages=self.messages
            )

            reply = response.choices[0].message.content

            # Hide typing indicator
            self.hide_typing_indicator()

            # Display AI response
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.display_message(f"🤖 AI [{timestamp}]\n{reply}\n\n", "ai")

            # Store AI message
            self.messages.append({"role": "assistant", "content": reply})

        except Exception as e:
            self.hide_typing_indicator()
            self.display_message(f"❌ Error: {str(e)}\n\n", "error")

        finally:
            # Re-enable input
            self.send_button.configure(state="normal")
            self.user_entry.configure(state="normal")
            self.user_entry.focus()

    def display_message(self, message, msg_type):
        self.chat_box.configure(state="normal")

        # Configure text color based on message type
        if msg_type == "user":
            self.chat_box.insert("end", message, "user")
        elif msg_type == "ai":
            self.chat_box.insert("end", message, "ai")
        else:  # error
            self.chat_box.insert("end", message, "error")

        self.chat_box.configure(state="disabled")
        self.chat_box.see("end")

        # Configure tags for coloring
        self.chat_box.tag_config("user", foreground="#00ff88")
        self.chat_box.tag_config("ai", foreground="#0088ff")
        self.chat_box.tag_config("error", foreground="#ff4444")

    def show_typing_indicator(self):
        self.is_typing = True
        self.typing_label.configure(text="AI is typing...")

    def hide_typing_indicator(self):
        self.is_typing = False
        self.typing_label.configure(text="")

    def clear_chat(self):
        if messagebox.askyesno("Clear Chat", "Are you sure you want to clear the chat history?"):
            self.chat_box.configure(state="normal")
            self.chat_box.delete("1.0", "end")
            self.chat_box.configure(state="disabled")
            self.messages = []
            self.status_label.configure(text="Chat cleared 🗑️")

    def export_chat(self):
        if not self.messages:
            messagebox.showinfo("Export", "No chat history to export!")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("JSON files", "*.json"), ("All files", "*.*")]
        )

        if file_path:
            try:
                if file_path.endswith(".json"):
                    with open(file_path, "w") as f:
                        json.dump({
                            "model": self.current_model,
                            "timestamp": datetime.now().isoformat(),
                            "messages": self.messages
                        }, f, indent=2)
                else:
                    with open(file_path, "w") as f:
                        f.write(f"AI Chat Export - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                        f.write(f"Model: {self.current_model}\n\n")
                        f.write("-" * 50 + "\n\n")

                        for msg in self.messages:
                            role = "👤 You" if msg["role"] == "user" else "🤖 AI"
                            f.write(f"{role}: {msg['content']}\n\n")

                messagebox.showinfo("Export", f"Chat exported to {file_path}!")
                self.status_label.configure(text="Chat exported 💾")

            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to export: {str(e)}")

    def show_settings(self):
        settings_window = ctk.CTkToplevel(self.app)
        settings_window.title("Settings")
        settings_window.geometry("400x300")

        ctk.CTkLabel(settings_window, text="Settings", font=("Arial", 16, "bold")).pack(pady=10)

        # Theme selector
        theme_frame = ctk.CTkFrame(settings_window)
        theme_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(theme_frame, text="Theme:").pack(side="left", padx=10)
        theme_var = ctk.StringVar(value=ctk.get_appearance_mode())
        theme_menu = ctk.CTkOptionMenu(theme_frame, variable=theme_var,
                                     values=["Light", "Dark", "System"],
                                     command=lambda x: ctk.set_appearance_mode(x))
        theme_menu.pack(side="right", padx=10)

        # Color theme selector
        color_frame = ctk.CTkFrame(settings_window)
        color_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(color_frame, text="Color Theme:").pack(side="left", padx=10)
        color_var = ctk.StringVar(value="blue")
        color_menu = ctk.CTkOptionMenu(color_frame, variable=color_var,
                                     values=["blue", "green", "dark-blue"],
                                     command=lambda x: ctk.set_default_color_theme(x))
        color_menu.pack(side="right", padx=10)

    def show_about(self):
        about_text = """
🤖 AI Chat Pro v2.0

A modern AI chat application powered by Groq's fast inference API.

Features:
• Multiple AI models (Llama 3.1, Mixtral)
• Real-time chat with typing indicators
• Export conversations
• Modern dark UI
• Cross-platform compatibility

Built with Python, CustomTkinter, and Groq API

© 2024 AI Chat Pro
        """

        messagebox.showinfo("About AI Chat Pro", about_text.strip())

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    app = AIChatApp()
    app.run()
