import pyttsx3

def speak(text):
    
    """
    Takes a text string and speaks it aloud using the computer's speech engine
    """
    engine = pyttsx3.init()
    
    engine.say(text)
    engine.runAndWait()