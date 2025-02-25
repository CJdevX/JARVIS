import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
import webbrowser
import os

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Speed of speech
engine.setProperty('voice', engine.getProperty('voices')[0].id)  # Choose voice


def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen for a command"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            speak("I'm having trouble connecting to the internet.")
            return None


def respond(command):
    """Process the command and perform actions"""
    if command is None:
        return
    
    if "hello" in command:
        speak("Hello! How can I assist you?")
    
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    
    elif "date" in command:
        today_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today's date is {today_date}")
    
    elif "search" in command:
        speak("What do you want to search for?")
        query = listen()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {query}")
    
    elif "wikipedia" in command:
        speak("What do you want to know about?")
        query = listen()
        if query:
            try:
                summary = wikipedia.summary(query, sentences=2)
                speak(summary)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("I couldn't find any information on that topic.")
    
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    
    elif "play music" in command:
        music_dir = "D:\IDM\Music"  # Change this to your music folder
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Playing music")
        else:
            speak("No music found in the folder.")
    
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()
    
    else:
        speak("I'm not sure how to help with that.")


# Run the assistant
if __name__ == "__main__":
    speak("Hello, I am Jarvis. How can I assist you?")
    while True:
        command = listen()
        if command:
            respond(command)