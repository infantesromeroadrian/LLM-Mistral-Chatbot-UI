import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_api_key():
    """
    Retrieves the Mistral API key from environment variables.
    Returns:
    str: The API key.
    """
    api_key = os.getenv("MistralAI_API_TOKEN")
    if not api_key:
        logging.error("MISTRAL_API_KEY environment variable not found.")
        raise ValueError("API key not found. Please set the MISTRAL_API_KEY environment variable.")
    return api_key
