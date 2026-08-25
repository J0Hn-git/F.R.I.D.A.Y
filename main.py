from audio_input import verify_microphone
from transcriber import transcribe_audio_frames
from commands import handle_command

if __name__ == "__main__":
    print("=== Personal Assistant Starting ===")
    
    while True:
        frames, sample_rate = verify_microphone()
        
        if frames:
            spoken_text = transcribe_audio_frames(frames, sample_rate)
            
            if spoken_text:
                print(f"\n-> You said: '{spoken_text}'")
                
                should_exit = handle_command(spoken_text)
                
                if should_exit:
                    break
    
    print("\n=== Session Ended ===")