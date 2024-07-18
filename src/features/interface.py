import gradio as gr
from src.models.chat import chat_with_mistral

def create_gradio_interface(api_key):
    """
    Creates and launches the Gradio interface.
    """
    def wrapped_chat_with_mistral(user_input):
        return chat_with_mistral(api_key, user_input)

    ui = gr.Interface(
        fn=wrapped_chat_with_mistral,
        inputs=gr.components.Textbox(label="Enter Your Message"),
        outputs=gr.components.Markdown(label="Chatbot Response"),
        title="Mistral Coding Assistant",
        description="Get coding help and advice from the Mistral API. Enter your programming questions or code snippets below.",
        examples=[
            ["How do I reverse a string in Python?"],
            ["Can you explain the difference between a list and a tuple in Python?"]
        ],
        allow_flagging="never"
    )
    ui.launch()
