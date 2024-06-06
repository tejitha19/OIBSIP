import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen and recognize speech."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            query = None
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            query = None
        
        return query

def get_time():
    """Get the current time."""
    now = datetime.datetime.now().strftime("%H:%M")
    speak(f"The current time is {now}")

def open_youtube():
    """Open YouTube in a web browser."""
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")

def open_google():
    """Open Google Chrome."""
    speak("Opening Google Chrome")
    os.system("start chrome") 

def process_command(command):
    """Process the recognized command."""
    if 'time' in command:
        get_time()
    elif 'open youtube' in command:
        open_youtube()
    elif 'open google' in command:
        open_google()
    elif 'stop' in command:
        speak("Goodbye!")
        return False
    else:
        speak("Sorry, I didn't understand the command.")
    return True

if __name__ == "__main__":
    speak("Hello tejitha, how can I help you today?")
    
    while True:
        query = listen()
        
        if query:
            if not process_command(query.lower()):
                break
