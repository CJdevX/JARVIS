<h1> Jarvis AI Assistant </h1>
A simple voice-controlled AI assistant built with Python. Jarvis can recognize voice commands, search Wikipedia, open websites, play music, and more.

## Features
- 🎤 Voice recognition using Google Speech API
- 🗣️ Text-to-speech response using pyttsx3
- 🔍 Wikipedia search
- 🌐 Open Google and YouTube
- 🎵 Play local music
- ⏰ Tell the current time and date
- 🔎 Perform a Google search
- 🛑 Exit command

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/CJdevX/JARVIS.git
cd JARVIS
```
You can use Github Desktop App (Alternative)


### 2. Create a Virtual Environment
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
- **Windows**
  ```bash
  venv\Scripts\activate
  ```
- **Linux/macOS**
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

Once started, Jarvis will listen for commands. Try saying:
- "Hello"
- "What time is it?"
- "Search for Python programming"
- "Tell me about Albert Einstein on Wikipedia"
- "Open YouTube"
- "Play music"
- "Exit"

## Requirements
Ensure you have the following installed:
- Python 3.7+
- `pip` (comes with Python)
- `pyaudio` (for voice input, install manually if needed)
  - Windows: `pip install pyaudio`
  - Linux/macOS: `sudo apt install portaudio19-dev && pip install pyaudio`

## Contributions
Feel free to fork this repository and submit pull requests with improvements or new features.

## License
This project is licensed under the MIT License.
