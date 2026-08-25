import pyaudio

def verify_microphone():
    
    #Initialize PyAudio
    p = pyaudio.PyAudio()
    
    #Audio parameters
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 3
    
    try :
        print("[INFO] Opening microphone stream...")
        
        # Open an input stream to accept audio bytes.
        stream = p.open(
            channels= CHANNELS,
            rate= RATE,
            format= FORMAT,
            input= True,
            frames_per_buffer= CHUNK
        )
        print(f"\n[LISTENING] Speak into your microphone for {RECORD_SECONDS} seconds.")
        
        frames = []
        #Loop to capture audio chunks for 3 seconds.
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
            
        print("[INFO] Recording finished. Processing audio bytes...")
            
        
        # Clean up stream
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        # Simple verification to check if we collected data bytes.
        total_bytes = sum(len(chunk) for chunk in frames)
        print(f"\n[SUCCESS] Successfully captured {total_bytes} audio bytes from your microphone!")
        print("[VERIFICATION PASSED] Your microphone is actively recording audio data.")
        
        return frames, RATE
        
    except Exception as e:
        print(f"\n[ERROR] Failed to access microphone: {e}")
        print("[TIP] Check your operating system microphone permissions or default input device settings.")
        
if __name__ == "__main__":
    print("=== Step 1: Microphone Hardware Test ===")
    verify_microphone()