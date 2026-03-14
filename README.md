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
- **Linux Environment**: Bash or Zsh (tested on Tilix/Alacritty).

## ⚙️ Installation & Setup

```shell
git clone https://github.com/alexolinux/gemini-cli.git
cd gemini-cli
```

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

```shell
export GOOGLE_API_KEY="[GOOGLE_API_KEY_HERE]"
```

Add your `GOOGLE_API_KEY` to your $SHELL (`~/.bashrc` or `~/.zshrc`, etc) for persistence.

## Usage

- Quick Question: `gem "How to check open ports on Linux?"`

- Interactive Chat: `gemini`

## 🧠 System Instruction (Persona)

The CLI is programmed to behave as a Senior Linux Expert. You can modify this behavior by editing the SYSTEM_INSTRUCTION variable in gemini-cli.py.

## 📝 License

MIT License

## Author

https://alexolinux.com
