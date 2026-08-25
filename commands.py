import datetime
import os
from speaker import speak


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
        print("Assistant: Hello! How can i help you today? ")
        
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(f"Assistant: The current time is {current_time}")
        
    elif "exit" in command or "quit" in command or "stop" in command:
        print("Assistant: Goodbye!")
        return True
    
    else :
        print(f"Assistant: I heard you say '{text}'")
        
    return False
        