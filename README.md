# Festival Anchor Voice Assistant



The **Festival Anchor Voice Assistant** is a Python-based program that acts as an interactive event “anchor” or personal assistant. It integrates speech recognition and text-to-speech to listen and respond to voice commands. Users can ask about the weather, get word definitions, hear jokes, listen to news, perform math calculations, and even chat with a GPT-4 powered “Jarvis.” The assistant processes the spoken query, performs the requested task, and replies out loud, simulating a friendly on-stage festival host.

## Features

- **Speech Recognition & TTS:** Listens to the user through the microphone using `speech_recognition`, and responds with spoken output via `pyttsx3`.
- **Word Definitions:** Provides dictionary definitions using NLTK’s WordNet. Example: “What is *serendipity*?”
- **Weather Updates:** Fetches current weather information from OpenWeatherMap API. Example: “Weather in *[City]*”
- **Jokes:** Tells a random joke using the `pyjokes` library.
- **Music Playback:** Plays a predefined audio file (`output.mp3`) via `pygame`.
- **Random Facts (Wikipedia):** Fetches and speaks a random Wikipedia summary using `wikipediaapi`.
- **Math Calculations:** Recognizes and evaluates simple spoken math expressions.
- **Date/Time Info:** Reports current date, time, and day of the week.
- **News Reader:** Fetches and reads news from BBC, CNN, TechCrunch, and Malayalam sources.
- **ChatGPT (“Jarvis” Mode):** Conversations powered by OpenAI’s GPT-4. Say “Jarvis” to activate.

## Installation

1. **Install Python 3.7+**
2. **Install Dependencies**:
   ```bash
   pip install SpeechRecognition pyttsx3 requests nltk keyboard googletrans==4.0.0-rc1 openai pygame wikipedia-api feedparser beautifulsoup4 pyjokes
   ```
3. **Download NLTK Data**:
   ```python
   import nltk
   nltk.download('wordnet')
   ```
4. **API Keys**:
   - OpenWeatherMap: replace placeholder in `get_weather(city)`
   - OpenAI GPT: set `openai.api_key = 'YOUR_KEY'`
5. **Hardware**: Ensure a working microphone and speakers.
6. **Voice Setting**: Update `engine.setProperty('voice', ...)` to match OS voice.

## Usage

- **Run the Program**:
  ```bash
  python festival_anchor.py
  ```
- **Trigger Greeting**: Press the spacebar.
- **Example Commands**:
  - “What is the weather in New York?”
  - “Define algorithm.”
  - “Tell me a joke.”
  - “Play music.”
  - “Give me a random fact.”
  - “What is 15 divided by 3?”
  - “What time is it?”
  - “Read the news.”
  - “Jarvis” (to enter GPT-4 mode)
- **Exit**: Say “exit” or press `Ctrl+C`

## Contributors & License

This project is released under the [MIT License](LICENSE). Contributions are welcome via pull requests!

---

*Built with ❤️ for interactive festival experiences.*
