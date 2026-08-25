import speech_recognition as sr

def transcribe_audio_frames(frames, rate=16000):
    
    """ Takes raw audio frames, combines them, and converts them into speech."""
    try :
        print("[INFO] Combining audio frames...")
        
        audio_data_bytes = b''.join(frames)
        
        # Initialize the Speech recognition Engine.
        recognizer = sr.Recognizer()
        audio_file = sr.AudioData(audio_data_bytes, rate, 2)
        
        print("[INFO] Sending audio to Google Speech Recognition.")
        
        text = recognizer.recognize_google(audio_file)
        
        return text
        
        
    except sr.UnknownValueError:
        print("\n[WARNING] Google could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"\n [ERROR] Could not request results from Google service; {e}")
        return None
    except Exception as e:
        print(f"\n [ERROR] An error occured: {e}")
        return None