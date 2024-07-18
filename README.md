# Mistral Chatbot Project

This project implements a coding assistant chatbot using the Mistral API and Gradio for the user interface.

## Project Structure

The project is structured as follows:

src/
    features/
        client.py
        interface.py
    models/
        chat.py
    utils/
        config.py

    main.py


## File Descriptions

- **config.py**: Loads environment variables and retrieves the Mistral API key.
- **client.py**: Creates and manages the MistralClient instance.
- **chat.py**: Contains functions to interact with the Mistral API.
- **interface.py**: Creates and launches the Gradio interface.
- **main.py**: Entry point for the application.

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mistral_chatbot.git
   cd mistral_chatbot

Create a .env file in the project root with your Mistral API token:


makefile

""""
MISTRAL_API_KEY=your_mistral_api_key
""""
Install the necessary dependencies:

bash
pip install gradio mistralai python-dotenv
Running the Application
Run the application using:

bash
Copy code
python main.py
Example Usage
Once the application is running, you can interact with the chatbot through the Gradio interface. Here are some example inputs you can try:

"How do I reverse a string in Python?"
"Can you explain the difference between a list and a tuple in Python?"
The chatbot will respond with helpful coding advice and explanations.

Logging
Logging is configured in config.py to output informational messages, which can be useful for debugging and monitoring the application's behavior.

Notes
Ensure your .env file is correctly set up with your Mistral API token.
This project uses the mistralai Python package to interact with the Mistral API.