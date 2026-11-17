from google import genai
from google.genai import types, errors
import os
import re
import sys

# Configuration
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("Error: GOOGLE_API_KEY environment variable not found.")
    sys.exit(1)

client = genai.Client(api_key=api_key)

# Família preferida e override opcional via env (ex.: GEMINI_MODEL=gemini-2.5-flash)
PREFERRED_FAMILY = "flash"
PINNED_MODEL = os.getenv("GEMINI_MODEL")

# Modelos que suportam generateContent mas não servem para chat de texto
EXCLUDE = ("image", "tts", "audio", "live", "embedding", "robotics", "computer-use")

# Erros que justificam tentar o próximo modelo
RETRYABLE = {404, 429, 503}

SYSTEM_INSTRUCTION = (
    "You are a Linux System Administrator, DevOps Engineer and Expert Software Developer. "
    "Your answers should be technical, precise, and favor CLI-based solutions. "
    "When providing code or commands, always explain briefly what they do."
)


def _rank(name):
    """Ordena: família preferida > estável > versão mais nova."""
    m = re.match(r"gemini-(\d+(?:\.\d+)?)-(flash|pro)(-lite)?", name)
    if not m:
        return (9, 1, 0.0)
    version, family, lite = float(m.group(1)), m.group(2), m.group(3)
    family_score = 0 if (family == PREFERRED_FAMILY and not lite) else 1 if lite else 2
    unstable = 1 if re.search(r"preview|exp", name) else 0
    return (family_score, unstable, -version)


def discover_models():
    """Retorna modelos Gemini ativos, ordenados por preferência."""
    names = set()
    for m in client.models.list():
        if "generateContent" not in (m.supported_actions or []):
            continue
        name = m.name.removeprefix("models/")
        if name.startswith("gemini-") and not any(x in name for x in EXCLUDE):
            names.add(name)
    ranked = sorted(names, key=_rank)
    if PINNED_MODEL:
        ranked = [PINNED_MODEL] + [n for n in ranked if n != PINNED_MODEL]
    return ranked


try:
    CANDIDATES = discover_models()
except Exception as e:
    print(f"Error listing models: {e}")
    sys.exit(1)

if not CANDIDATES:
    print("Error: no models with generateContent support available.")
    sys.exit(1)

CONFIG = types.GenerateContentConfig(system_instruction=SYSTEM_INSTRUCTION)


def get_single_response(prompt):
    """Sends a single prompt, falling back through candidate models."""
    last_error = None
    for model in CANDIDATES:
        try:
            response = client.models.generate_content(
                model=model, contents=prompt, config=CONFIG
            )
            return response.text
        except errors.APIError as e:
            last_error = e
            if e.code not in RETRYABLE:
                break
            print(f"[warn] {model} failed ({e.code}), trying next...", file=sys.stderr)
        except Exception as e:
            last_error = e
            break
    return f"Error: {last_error}"


def _new_chat(model, history=None):
    return client.chats.create(model=model, config=CONFIG, history=history or [])


def start_interactive_session():
    """Chat session; on model failure, recreates the chat on the next candidate keeping history."""
    idx = 0
    try:
        chat = _new_chat(CANDIDATES[idx])
        print(f"--- Gemini Interactive Mode ({CANDIDATES[idx]}) ---")
        print(f"Role: {SYSTEM_INSTRUCTION[:60]}...")
        print("Type 'exit' or 'quit' to end the session.\n")

        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit", "sair"]:
                print("Goodbye!")
                break

            while True:
                try:
                    response = chat.send_message(user_input)
                    break
                except errors.APIError as e:
                    if e.code not in RETRYABLE or idx + 1 >= len(CANDIDATES):
                        raise
                    idx += 1
                    print(f"[warn] switching to {CANDIDATES[idx]} ({e.code})", file=sys.stderr)
                    chat = _new_chat(CANDIDATES[idx], chat.get_history())

            print(f"\nGemini: {response.text}\n")
    except Exception as e:
        print(f"Error: {e}")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  gemini 'your question'       - Single prompt")
        print("  gemini --interactive, -i     - Start a chat session")
        print("  gemini --models              - List available models")
        sys.exit(1)

    if sys.argv[1] == "--models":
        print("\n".join(CANDIDATES))
    elif sys.argv[1] in ["--interactive", "-i"]:
        start_interactive_session()
    else:
        print(get_single_response(" ".join(sys.argv[1:])))


if __name__ == "__main__":
    main()
