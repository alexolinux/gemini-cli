# gemini-cli

------------

🚀 Gemini AI for Terminal CLI

A high-performance Command Line Interface (CLI) to interact with Google's latest Gemini models (2.0+) directly from your Linux terminal.

## 🌟 Features

- **Modern Architecture**: Optimized for `gemini-2.5-flash`.
- **System Instructions**: Pre-configured as a Linux System Administrator, DevOps Engineer and Expert Software Developer.
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
# Install dependencies from requirements.txt
pip install -r requirements.txt
```

## Shell Configuration

```shell
# Add your GOOGLE_API_KEY to your $SHELL (`~/.bashrc` or `~/.zshrc`, etc) for persistence.
export GOOGLE_API_KEY="[GOOGLE_API_KEY_HERE]"
```

```shell
# Create an alias for easy access
#(replace '${HOME}/.local/' with your actual clone directory)
alias gemini="${HOME}/.local/gemini-cli/.venv/bin/python /home/alexmbarbosa/.local/gemini-cli/gemini-cli.py"
```

## Usage

- Quick Question: `gemini "How to check opened ports on Linux?"`

- Interactive Chat: `gemini --interactive` (or `gemini -i`)

### Extra Shell Configuration

Instead of creating an aliases, you might create a shell function to use this script as a command.

```shell
# Add to your ~/.bashrc or ~/.zshrc
_gemini_setup() {
    local default_pkg="$HOME/pkg"
    PKG="${PKG:-$default_pkg}"
    GEMINI_PYTHON="$PKG/gemini-cli/.venv/bin/python"
    GEMINI_SCRIPT="$PKG/gemini-cli/gemini-cli.py"
}

gemini() {
    _gemini_setup

    if [ ! -f "$GEMINI_PYTHON" ]; then
        echo "Error: Python interpreter not found. Check PKG environment variable." >&2
        return 1
    fi

    if [ "$1" = "-i" ]; then
        "$GEMINI_PYTHON" "$GEMINI_SCRIPT" -i "${@:2}"
    else
        "$GEMINI_PYTHON" "$GEMINI_SCRIPT" "$@"
    fi
}
```

Then, you can call this script running `gemini` or `gemini --interactive | -i`.

## 🧠 System Instruction (Persona)

The CLI is programmed to behave as a Linux SysAdmin and DevOps Engineer. You can modify this behavior by editing the SYSTEM_INSTRUCTION variable in gemini-cli.py.

## 📝 License

MIT License

## Author

https://alexolinux.com
