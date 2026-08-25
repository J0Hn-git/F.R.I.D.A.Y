import os
import platform

def open_application(app_name):
    
    """
    A single function to handle opening different websites or apps based
    on the name passed to it.
    """
    
    app_name = app_name.lower()
    
    urls = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "github": "https://github.com",
        "leetcode": "https://leetcode.com"
    }
    
    if app_name in urls:
        url = urls[app_name]
        print(f"[INFO] Opening {app_name}...")
        
        system_name = platform.system()
        if system_name == "Windows":
            os.system(f"start {url}")
        else :
            os.system(f"xdg-open {url}")
        return True
            
    else :
        print(f"[WARNING] App or website '{app_name}' not recognized.")
        return False
        
if __name__ == "__main__":
    open_application()
    
    
    
    