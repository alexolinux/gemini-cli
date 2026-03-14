# gemini-cli

------------

🚀 Gemini AI for Terminal CLI

A high-performance Command Line Interface (CLI) to interact with Google's latest Gemini models (2.0+) directly from your Linux terminal. 

## 🌟 Features

- **Modern Architecture**: Optimized for `gemini-2.0-flash`.
- **System Instructions**: Pre-configured as a Senior Linux Admin and Software Developer.
- **Zero Latency**: Lightweight execution using a dedicated Python virtual environment.
- **Interactive Mode**: Full conversational support in the terminal.

## 📋 Prerequisites

- **Python 3.10+**
- **Google AI API Key**: Get it at [Google AI Studio](https://ai.google.dev/).
- **Linux Environment**: Bash or Zsh (tested on Tilix/Alacrity).

## ⚙️ Installation & Setup

Setup virtual environment

```shell
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies

```shell
# Install dependencies
pip install -q -U google-generativeai
```

## Shell Configuration

Add your API key and aliases to your `~/.bashrc` or `~/.zshrc`:

```shell
export GOOGLE_API_KEY="[GOOGLE_API_KEY_HERE]"
```

### Tips

You might add this project in path folder or yout preference.

Example:

```shell
# gemini-cli Alias Example
alias gem="${HOME}/.loca/gemini-cli/venv/bin/python ${HOME}/.loca/gemini-cli/gemini-cli.py"

alias gemini="${HOME}/.loca/gemini-cli/venv/bin/python ${HOME}/.loca/gemini-cli/gemini-cli.py --interactive"
```

*Apply changes with `source ~/.bashrc` or `source ~/.zshrc`.*

## Usage

- Quick Question: `gem "How to check open ports on Linux?"`

- Interactive Chat: `gemini`

## 🧠 System Instruction (Persona)
The CLI is programmed to behave as a Senior Linux Expert. You can modify this behavior by editing the SYSTEM_INSTRUCTION variable in gemini-cli.py.

## 📝 License

MIT License

## Author

https://alexolinux.com

