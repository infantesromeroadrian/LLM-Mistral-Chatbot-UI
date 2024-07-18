import logging
from mistralai.client import MistralClient

def create_mistral_client(api_key):
    """
    Creates a MistralClient instance.
    Args:
    api_key (str): The API key for authentication.
    Returns:
    MistralClient: The MistralClient instance.
    """
    try:
        return MistralClient(api_key=api_key)
    except Exception as e:
        logging.error(f"Error creating MistralClient: {e}")
        raise
