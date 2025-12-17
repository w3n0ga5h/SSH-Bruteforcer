## 📝 Description

This script is designed to test the security of an SSH server by attempting to log in with a specific username and a list of passwords provided in a text file. It uses the `paramiko` library for SSH connections and `termcolor` to provide clear, color-coded feedback in the terminal.

## 👤 Author's Note

I am currently **learning Python**, and this is my **very first tool**. 

> [!IMPORTANT]
> **I intentionally did not use AI to write this code.** I wanted to challenge myself to understand every single line, research the documentation manually, and learn from my own logic. 
> 
> I am fully aware that the code is not perfectly optimized yet, but it was a great exercise to master the basics. 
> 
> **I am open to any advice, feedback, or tips!** If you have suggestions on how to make the code cleaner or more efficient, please let me know.

## 🚀 Features

* **SSH Connectivity**: Built using the `paramiko` library.
* **Visual Feedback**: Uses `termcolor` to highlight successful attempts in green.
* **User-Friendly**: Simple CLI prompts for target IP, ports, username and password wordlist path.
* **Auto-Policy**: Automatically handles missing SSH host keys.

## 🛠️ Installation & Requirements

1. **Clone the repository:**
   ```bash
   git clone https://github.com/w3n0ga5h/SSH-Bruteforcer.git
   cd SSH-Bruteforcer
   python3 -m venv SSH-Bruteforcer
   pip install -r requirements.txt
   source SSH-Bruteforcer/bin/activate

## 📋 Usage

To use this tool, run the main script and follow the interactive prompts:
Bash

    python sshbrute.py
    

⚠️ Disclaimer

This tool is for educational and ethical testing purposes only. Never use this script on a system you do not own or have explicit permission to test. Using this tool against targets without prior authorization is illegal. The author is not responsible for any misuse or damage caused by this program.
