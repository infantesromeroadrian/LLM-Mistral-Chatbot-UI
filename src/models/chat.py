import logging
from mistralai.models.chat_completion import ChatMessage

def get_chat_response(client, user_input, model="codestral-mamba-latest"):
    """
    Gets the chat response from the Mistral API.

    Args:
    client (MistralClient): The MistralClient instance.
    user_input (str): The input message from the user.
    model (str): The model name.

    Returns:
    str: The response message from the Mistral API.
    """
    try:
        messages = [ChatMessage(role="user", content=user_input)]
        chat_response = client.chat(model=model, messages=messages)
        return chat_response.choices[0].message.content
    except Exception as e:
        logging.error(f"Error interacting with the Mistral API: {e}")
        return "An error occurred while interacting with the Mistral API. Please try again later."

def chat_with_mistral(api_key, user_input):
    """
    Function to interact with the Mistral API.
    Args:
    user_input (str): The input message from the user.
    Returns:
    str: The response message from the Mistral API.
    """
    from src.features.client import create_mistral_client
    try:
        client = create_mistral_client(api_key)
        return get_chat_response(client, user_input)
    except ValueError as e:
        return str(e)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return "An unexpected error occurred. Please try again later."
