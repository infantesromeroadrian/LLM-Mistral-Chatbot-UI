from utils.config import get_api_key
from features.interface import create_gradio_interface

if __name__ == "__main__":
    api_key = get_api_key()
    create_gradio_interface(api_key)
