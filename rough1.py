import sys
import subprocess

def install_dotenv():
    try:
        import dotenv
        print("python-dotenv is already installed.")
    except ImportError:
        print("Installing python-dotenv...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'python-dotenv'])
            print("Successfully installed python-dotenv!")
        except Exception as e:
            print(f"Error installing python-dotenv: {e}")
            print("Please try manual installation:")
            print("1. Open command prompt")
            print("2. Run: pip install python-dotenv")
            return False
    return True

def test_dotenv():
    try:
        from dotenv import load_dotenv
        import os
        
        # Load environment variables
        load_dotenv()
        
        # Try to read an environment variable
        api_key = os.getenv("OPENAI_API_KEY")
        
        if api_key:
            print("Environment variable loaded successfully!")
        else:
            print("No OPENAI_API_KEY found in .env file")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Run installation check
if install_dotenv():
    # Test dotenv functionality
    test_dotenv()