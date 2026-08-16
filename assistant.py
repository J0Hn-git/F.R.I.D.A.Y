import pyaudio

def verify_microphone():
    
    #Initialize PyAudio
    p = pyaudio.PyAudio()
    
    #Audio parameters
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    
    try :
        print("[INFO] Attempting to access the default microphone...")
        
        # Open an input stream to accept audio bytes.
        stream = p.open(
            channels= CHANNELS,
            rate= RATE,
            format= FORMAT,
            input= True,
            frames_per_buffer= CHUNK
        )
        print("\n [SUCCESS] MIcrophone is successfully accessed and ready to accept audio bytes!")
        
        # Clean up stream
        stream.stop_stream()
        stream.close()
        p.terminate()
        
    except Exception as e:
        print(f"\n[ERROR] Failed to access microphone: {e}")
        print("[TIP] Check your operating system microphone permissions or default input device settings.")
        
if __name__ == "__main__":
    print("=== Step 1: Microphone Hardware Test ===")
    verify_microphone()