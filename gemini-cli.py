from google import genai
from google.genai import types
import os
import sys

# Configuration
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("Error: GOOGLE_API_KEY environment variable not found.")
    sys.exit(1)

client = genai.Client(api_key=api_key)
MODEL_NAME = 'gemini-2.5-flash'

# System Instruction: Define the AI's behavior and personality
SYSTEM_INSTRUCTION = (
    "You are a Linux System Administrator, DevOps Engineer and Expert Software Developer. "
    "Your answers should be technical, precise, and favor CLI-based solutions. "
    "When providing code or commands, always explain briefly what they do."
)

def get_single_response(prompt):
    """Sends a single prompt to the model with system instructions."""
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION
            )
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

def start_interactive_session():
    """Starts a continuous chat session with system instructions."""
    try:
        chat = client.chats.create(
            model=MODEL_NAME,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION
            )
        )
        print(f"--- Gemini Interactive Mode ({MODEL_NAME}) ---")
        print(f"Role: {SYSTEM_INSTRUCTION[:60]}...") # Shows a preview of the role
        print("Type 'exit' or 'quit' to end the session.\n")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', 'sair']:
                print("Goodbye!")
                break
            
            response = chat.send_message(user_input)
            print(f"\nGemini: {response.text}\n")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  gem 'your question'       - Single prompt")
        print("  gem --interactive         - Start a chat session")
        sys.exit(1)

    if sys.argv[1] == "--interactive":
        start_interactive_session()
    else:
        prompt = " ".join(sys.argv[1:])
        print(get_single_response(prompt))

if __name__ == "__main__":
    main()
