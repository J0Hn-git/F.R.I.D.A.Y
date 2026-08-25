import pyttsx3

def speak(text):
    
    """
    Takes a text string and speaks it aloud using the computer's speech engine
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    engine.setProperty('voice', voices[1].id)
    
    engine.say(text)
    engine.runAndWait()
    
if __name__ == "__main__":
    speak("Hello! I am your assistant, powered by Zira.")
    
