Festival Anchor Voice Assistant
Image: A voice-controlled smart speaker (Google Home Mini) representing the voice interface of the Festival Anchor Assistant. The Festival Anchor Voice Assistant is a Python-based program that acts as an interactive event “anchor” or personal assistant. It integrates speech recognition and text-to-speech to listen and respond to voice commands. Users can ask about the weather, get word definitions, hear jokes, listen to news, perform math calculations, and even chat with a GPT-4 powered “Jarvis.” The assistant processes the spoken query, performs the requested task, and replies out loud, simulating a friendly on-stage festival host.
Features
Speech Recognition & TTS: Listens to the user through the microphone using speech_recognition, and responds with spoken output via pyttsx3. The assistant greets the user and prompts for input.
Word Definitions: Provides dictionary definitions using NLTK’s WordNet (define_word(word) function). For example, asking “What is serendipity?” will fetch and speak the definition.
Weather Updates: Fetches current weather information from the OpenWeatherMap API (get_weather(city)). The user can say “What is the weather in [City]?” or “Weather for [City],” and the assistant will report the description and temperature in Celsius.
Jokes: Tells a random joke using the pyjokes library. The user can simply ask the assistant to tell a joke, and it will reply with a humorous one-liner.
Music Playback: Plays a predefined audio file (output.mp3) via the pygame library. This simulates playing a song or background music when requested (e.g., “Play music”).
Random Facts (Wikipedia): Fetches and speaks a random article summary from Wikipedia in English (or other supported languages) using wikipediaapi. It selects a random category (like History, Science, etc.) and reads a brief fact aloud.
Math Calculations: Recognizes and evaluates simple spoken math expressions (recognize_and_calculate()). For example, if you say “three plus four times two,” the assistant computes the result and answers verbally.
Date/Time Info: Reports the current date, time, and day of the week. Asking “What is the date and time?” or “What day is it?” will prompt a spoken response with that information.
News Reader: Fetches and reads news headlines from configured sources. It can parse RSS feeds (e.g., TechCrunch) and websites (e.g., BBC News) using feedparser and BeautifulSoup. On hearing “Read the news,” it will start reading article titles aloud until the user says “stop.”
ChatGPT (“Jarvis” Mode): Integrates with OpenAI’s GPT-4 for conversational chat. If the user says “Jarvis,” the assistant enters an open-ended dialogue mode via the openai.ChatCompletion API.
Image: A friendly AI robot symbolizing the GPT-powered “Jarvis” conversational mode. In Jarvis Mode, the assistant forwards the user’s input to OpenAI’s GPT-4 model and speaks the AI’s response. This allows for natural, free-form conversations and answers to questions beyond the built-in functions. The user can say “exit” at any time to leave Jarvis Mode and return to the standard assistant functions.
Installation
Install Python 3.7+: Ensure you have Python 3.7 or newer.
Install Dependencies: Use pip to install the required packages. For example:
bash
Copy
Edit
pip install SpeechRecognition pyttsx3 requests nltk keyboard googletrans==4.0.0-rc1 openai pygame wikipedia-api feedparser beautifulsoup4 pyjokes
Download NLTK Data: In a Python shell or script, run:
python
Copy
Edit
import nltk
nltk.download('wordnet')
This installs the WordNet corpus needed for definitions.
API Keys:
OpenWeatherMap Key: Replace the placeholder API key in get_weather(city) with your own from openweathermap.org.
OpenAI Key: Obtain an API key from OpenAI and set openai.api_key = 'YOUR_KEY'. This enables the Jarvis (GPT) feature.
Hardware: Make sure you have a working microphone and speakers. The assistant listens and speaks in real time.
Platform Note: The default voice in pyttsx3 is set to a macOS voice (daniel.premium). You may need to change the engine.setProperty('voice', ...) setting to a voice available on your system (Windows or Linux).
Usage
Run the Program: Execute the Python script (e.g. python festival_anchor.py or python main.py, depending on your file). The assistant will initialize and prompt you via console.
Activate Greeting: Press the space bar to have the assistant say the welcome prompt. You can then speak your command when prompted.
Speak Commands: Ask questions or give commands aloud. Examples include:
“What is the weather in New York?” — The assistant will reply with the current weather.
“Define algorithm.” — It will speak the dictionary definition of “algorithm.”
“Tell me a joke.” — A joke will be spoken back.
“Play music.” — It will play the output.mp3 file.
“Give me a random fact.” — It will fetch and read a Wikipedia summary.
“What is 15 divided by 3?” — The assistant will calculate and answer.
“What time is it?” or “What’s today’s date?” — It will announce the current time/date.
“Read the news.” — It will start reading news headlines. Say “stop” to end.
“Jarvis” — Enters the GPT-4 chat mode. You can then talk freely (type or say) and the assistant will respond using ChatGPT. Say “exit” to leave this mode.
Terminate: In any mode, saying “exit” or pressing Ctrl+C will end the program.
Contributing & License
Contributions, feedback, and suggestions are welcome! Feel free to fork the repository and submit pull requests. This project is released under the MIT License. Enjoy building and enhancing your Festival Anchor Assistant!
