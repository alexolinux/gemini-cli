import google.generativeai as genai
import os
import sys

# Configuration
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("Error: GOOGLE_API_KEY environment variable not found.")
    sys.exit(1)

genai.configure(api_key=api_key)
MODEL_NAME = 'models/gemini-1.5-flash'

# System Instruction: Define the AI's behavior and personality
SYSTEM_INSTRUCTION = (
    "You are a Senior Linux System Administrator and Expert Software Developer. "
    "Your answers should be technical, precise, and favor CLI-based solutions. "
    "When providing code or commands, always explain briefly what they do."
)

def get_single_response(prompt):
    """Sends a single prompt to the model with system instructions."""
    try:
        # Initializing model with system instructions
        model = genai.GenerativeModel(
            model_name=MODEL_NAME,
            system_instruction=SYSTEM_INSTRUCTION
        )
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

def start_interactive_session():
    """Starts a continuous chat session with system instructions."""
    try:
        model = genai.GenerativeModel(
            model_name=MODEL_NAME,
            system_instruction=SYSTEM_INSTRUCTION
        )
        chat = model.start_chat(history=[])
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
