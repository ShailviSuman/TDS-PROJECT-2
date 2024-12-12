import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve API key
api_key = os.getenv("OPENAI_API_KEY")