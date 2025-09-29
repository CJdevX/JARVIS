import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import sys
import requests
import google.generativeai as genai

# ---------------- API KEYS ---------------- #
GOOGLE_API_KEY = "AIzaSyD4heBYuiOUcxmuxWEc7WftGySglpJiLwU"        # Replace with your Google API Key
SEARCH_ENGINE_ID = "427103038d60f4518"    # Replace with your CSE ID
genai.configure(api_key="AIzaSyBsi0V8wJQrvvtQNbpwWMyA0H9m4vcD-cY")    # Replace with your Gemini API key
gemini = genai.GenerativeModel("gemini-2.0-flash")

# ---------------- TTS Setup ---------------- #
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('voice', engine.getProperty('voices')[0].id)

# ---------------- Functions ---------------- #
def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=7)
            command = r.recognize_google(audio).lower()
            print("You said:", command)
            return command
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            speak("I can't connect to the internet.")
            return None

def google_search(query):
    """Fetch live answer from Google Custom Search"""
    try:
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={GOOGLE_API_KEY}&cx={SEARCH_ENGINE_ID}"
        response = requests.get(url).json()
        return response["items"][0]["snippet"]
    except:
        return None

def chat_with_gemini(query):
    """Fallback to Gemini AI"""
    try:
        response = gemini.generate_content(query)
        return response.text
    except:
        return "Sorry, I couldn't get an answer right now."

def respond(command):
    if command is None:
        return

    if "goodbye" in command:
        speak("Goodbye!")
        sys.exit()

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "date" in command:
        today_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today's date is {today_date}")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "play music" in command:
        music_dir = "D:\\IDM\\Music"
        if os.path.exists(music_dir):
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
                speak("Playing music")
            else:
                speak("No music found.")
        else:
            speak("Music folder not found.")

    else:
        # Try Google first
        answer = google_search(command)
        if answer:
            speak(answer)
        else:
            # Fallback to Gemini AI
            ai_reply = chat_with_gemini(command)
            speak(ai_reply)

# ---------------- Main Loop ---------------- #
if __name__ == "__main__":
    speak("Hello, I am Jarvis.")
    while True:
        command = listen()
        if command:
            command = command.replace("jarvis", "").strip()
            respond(command)