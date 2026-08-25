import datetime
import os
from speaker import speak
from app_launcher import open_application


def handle_command(text):
    
    """
    Takes the transcribed text string, converts it to lowercase.
    and matches it against known commands.
    """
    if not text:
        return
    
    command = text.lower()
    print(f"\n [ROUTER] Analyzing command: '{command}'")
    
    if "hello" in command or "hi" in command:
        response =  "Hello! How can i help you today? "
        print(f"Assistant: {response}")
        speak(response)
        
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        response = f"Assistant: The current time is {current_time}"
        print(f"Assistant: {response}")
        speak(response)
        
    elif "exit" in command or "quit" in command or "stop" in command:
        response = "Assistant: Goodbye!"
        print(f"Assistant: {response}")
        speak(response)
        return True
    
    elif "youtube" in command:
        response = "Opening YouTube"
        print(f"Assistant: {response}")
        speak(response)
        open_application("youtube")
        
    elif "github" in command:
        response = "Opening GitHub."
        speak(response)
        open_application("github")
    
    else :
        response = f"Assistant: I heard you say {text}, but I don't know how to handle that yet."
        print(f"Assistant: {response}")
        speak(response)
        
    return False
        