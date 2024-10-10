import speech_recognition as sr
import pyttsx3
import re
import requests
from nltk.corpus import wordnet
import keyboard
from googletrans import Translator
import openai
import pygame as py
import wikipediaapi
import random
import time
import datetime
import feedparser
from bs4 import BeautifulSoup
# Initialize the recognizer with noise cancellation
recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = True

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust the speech rate (words per minute)
engine.setProperty('volume', 1.0)  # Adjust the volume (0.0 to 1.0)
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.daniel.premium')  # Change voice to a male voice

# Create a message queue
message_queue = []
# Function to add a message to the queue
def add_to_queue(text):
    message_queue.append(text)

# Function to speak messages from the queue
def speak_messages():
    while message_queue:
        message = message_queue.pop(0)
        engine.say(message)
        engine.runAndWait()

# Function for the robot to speak
def speak(text):
    add_to_queue(text)

# Function to listen and recognize speech
def listen():
    with sr.Microphone() as source:
        print("Robot: Hello, I am your festival anchor. What would you like to know or hear?")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            user_query = recognizer.recognize_google(audio)
            return user_query
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "I am having trouble with my speech recognition service. Please try again."

# Function to fetch WordNet definitions for the user's query




def play_music():
    py.init()
    py.mixer.init()
    py.mixer.music.load("output.mp3")
    py.mixer.music.play()
    while py.mixer.music.get_busy():
        pass
    py.mixer.quit()


def speak_pyttsx3(text, language):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def define_word(word):
    synsets = wordnet.synsets(word)

    if synsets:
        for synset in synsets:
            print(f"Synset: {synset.name()}, Definition: {synset.definition()}")
        # Take the definition from the first synset
        definition = synsets[0].definition()
        speak_pyttsx3(f"Definition of '{word}': {definition}", 'en')
    else:
        speak_pyttsx3(f"Sorry, no definition found for '{word}'.", 'en')# Function to get the current weather condition
def get_weather(city):
    api_key = '5cdb89e3e6991f4827d2f225f0acb41f'  # Replace with your OpenWeatherMap API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(base_url)
    data = response.json()

    if data["cod"] == 200:
        weather_info = data["weather"][0]["description"]
        temperature = data["main"]["temp"] - 273.15  # Convert temperature to Celsius
        return f"The weather in {city} is {weather_info}. The temperature is {temperature:.2f}°C."
    else:
        return f"Sorry, I couldn't fetch the weather information at the moment."

# Function to tell a random joke
def tell_joke():
    joke = pyjokes.get_joke()
    return "Here's a joke for you: " + joke

# Updated weather patterns with improved regular expressions
weather_patterns = [
    r'weather\s+in\s+(.+)',  # Pattern 1: "weather in [location]"
    r'what\s+is\s+the\s+weather\s+in\s+(.+)',  # Pattern 2: "what is the weather in [location]"
    r'weather\s+for\s+(.+)',  # Pattern 3: "weather for [location]"
    r'forecast\s+for\s+(.+)'  # Pattern 4: "forecast for [location]"
]

# Function to handle weather queries
def handle_weather_query(query):
    location = None
    for pattern in weather_patterns:
        location_match = re.search(pattern, query, re.IGNORECASE)
        if location_match:
            location = location_match.group(1)
            break

    if location:
        weather_response = get_weather(location)
        if speaking_language == 'en':
            speak_pyttsx3(weather_response, speaking_language)
    else:
        speak("I'm sorry, I couldn't determine the location from your query.")

def speak_on_key_press(e):
    if e.event_type == keyboard.KEY_DOWN:
        key_to_trigger = 'space'
        if e.name == key_to_trigger:
            speak_pyttsx3("Hello! I am here to assist you. Please ask your question or give a command.", speaking_language)

# Function to fetch and speak one random Wikipedia article summary
# Function to fetch and speak one random Wikipedia article summary
def fetch_and_speak_random_wikipedia_fact(language):
    # Specify a valid user agent
    user_agent = "YourAppName/1.0 (your@email.com)"

    wiki_wiki = wikipediaapi.Wikipedia(user_agent=user_agent)

    # You can change the category to get articles on different topics
    categories = ["History", "Science", "Geography", "Technology", "Art", "Culture"]
    random_category = random.choice(categories)

    # Get a random article title from the selected category
    category_page = wiki_wiki.page(f"Category:{random_category}")
    category_articles = category_page.categorymembers.values()
    random_article = random.choice(list(category_articles))

    # Fetch the summary of the random article
    page = wiki_wiki.page(random_article.title)
    article_summary = page.summary

    if article_summary:
        print(f"Title: {page.title}")
        print("Summary:")
        print(article_summary)
        if language =='en':
            speak_pyttsx3("Here's a random fact from Wikipedia:", language)
            speak_pyttsx3(article_summary, language)
        elif language == 'ml' or language == 'hi':
            speak_gttts("Here's a random fact from Wikipedia:", language)
            speak_gttts(article_summary, language)
    else:
        print("Failed to fetch an article. Please try again.")


def recognize_and_calculate():
    with sr.Microphone() as source:
        print("Listening to your math expression...")
        audio = recognizer.listen(source)

    try:
        expression = recognizer.recognize_google(audio)
        print(f"You said: {expression}")

        # Replace "x" with "*" in the expression
        expression = expression.replace("x", "*")

        # Ensure that the expression contains only allowed characters
        if not re.match(r'^[\d\s\+\-\/.()]$', expression):
            raise ValueError("Invalid characters in the expression")

        result = eval(expression)

        # Convert the result to a string
        result_str = str(result)

        # Output the answer as speech
        return result_str

        # Print the answer as text
        print(f"Answer: {result_str}")

    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
# Function to translate text to Hindi

def get_current_time():
    current_time = time.strftime("%I:%M %p")
    return "The current time is " + current_time

def get_current_date():
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    return "The current date is " + current_date

def get_current_day():
    current_day = datetime.datetime.now().strftime("%A")
    return "Today is " + current_day

def datetimefun(usr):
    while True:
            try:
                response = None
                if "date and time " in usr:
                    #speak(get_current_time())
                    #speak(get_current_date())
                    response = get_current_date() + get_current_time()


                elif " time" in usr :
                    response = get_current_time()

                elif "day" in usr:

                    response = get_current_day()

                elif "date" in usr:
                    response = get_current_date()


                if response:
                    print(response)
                    return response
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))


news_sources = [
        {"name": "BBC News", "type": "website", "url": "https://www.bbc.co.uk/news"},
        {"name": "CNN", "type": "website", "url": "https://edition.cnn.com/"},
        {"name": "TechCrunch", "type": "rss", "url": "https://techcrunch.com/rss"},
    ]

news_source = [
        {"name": "Malayalam News", "url": "https://www.kvartha.com/"},
    ]
def get_articles_from_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = []
        for article in soup.find_all('article'):
            title = article.find('h3').get_text()
            link = article.find('a')['href']
            articles.append({'title': title, 'link': link})
        return articles
    else:
        print(f"Failed to fetch articles from {url}")
        return []
def get_articles_from_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = []

        # Define a list of common HTML elements and class names for news content
        news_elements = ['article', 'div.article', 'div.post', 'div.content', 'div.story', 'div.entry-content', 'div.text', 'div.article-body']

        for element in news_elements:
            news_items = soup.select(element)
            for news_item in news_items:
                # Extract the text from the selected element
                text = news_item.get_text().strip()
                if text:  # Check if the text is not empty
                    articles.append({'text': text})
        return articles
    else:
        print(f"Failed to fetch articles from {url}")
        return []

def get_articles_from_rss_fed(feed_url):
    feed = feedparser.parse(feed_url)
    articles = [{'title': entry.title, 'link': entry.link} for entry in feed.entries]
    return articles

def read_news_articles(news_source,usr):
    print(f"Fetching news from {news_source['name']}...\n")
    if news_source['type'] == 'website':
        articles = get_articles_from_website(news_source['url'])
    elif news_source['type'] == 'rss':
        articles = get_articles_from_rss_fed(news_source['url'])

    if not articles:
        print(f"No articles found for {news_source['name']}.")
        return

    random.shuffle(articles)

    print("Say 'read the news' to start reading. Say 'stop' to stop reading.")
    command = usr
    if "read" in command:
        for article in articles:
            print(f"Title: {article['title']}")
            print(f"Link: {article['link']}")
            speak_pyttsx3(article['title'], 'en')
            comand = listen()
            if comand == "next":
                read_news_articles(news_source, usr)
            if comand == "stop" or "enough":
                speak_pyttsx3("Exiting the news section", 'en')
                break



#jarvis activation branch
openai.api_key = 'YOUR KEY GOES HERE'

def chat_with_gpt3(prompt):
    # Send a prompt to GPT-3.5 Turbo using the chat completions endpoint
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )

    # Extract and return the model's response
    return response.choices[0].message['content'].strip()

    # Get the generated response
    return response.choices[0].text.strip()

print("Jarvis: Hello! Ask me anything or type 'exit' to end the conversation.")

def jarvis():
    speak_pyttsx3("Jarvis activated",'en')
    while True:
        user_input = listen()

        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            speak_pyttsx3("Jarvis Deactivated",'en')
            print("Jarvis: Goodbye!")
            break

        else:
            # Generate a response from ChatGPT
            prompt = f"You: {user_input}\nChatGPT Bot:"
            response = chat_with_gpt3(prompt)

            speak_pyttsx3(f" {response}",'en')

# Function for the festival anchor robot
def festival_anchor():
    global speaking_language
    global use_gtts
    speaking_language = 'en'  # Default language is English
    use_gtts = False

    while True:
        keyboard.hook(speak_on_key_press)
        user_query = listen()
        print("User: " + user_query)

             # Check if the user mentioned "Jarvis"
        if "jarvis" in user_query.lower():
            jarvis()  # Call the Jarvis function
            continue  # Skip the rest of the loop for this iteration


if __name__ == "__main__":
    festival_anchor()
