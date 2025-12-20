# import gradio as gr
# from fastapi import FastAPI
# from backend.api import app as fastapi_app
# import requests

# def generate(query):
#     if not query.strip():
#         return "Please enter a query."

#     response = requests.post(
#         "http://localhost:7860/query",
#         json={"query": query}
#     )

#     data = response.json()

#     if "answer" in data:
#         return data["answer"]

#     return str(data)

# gradio_app = gr.Interface(
#     fn=generate,
#     inputs=gr.Textbox(label="Ask something"),
#     outputs=gr.Textbox(label="Answer"),
#     title="Physical AI Backend"
# )

# app = FastAPI()
# app.mount("/", gradio_app)
# app.mount("/api", fastapi_app)


import gradio as gr
from backend.api import retriever  # async function

import asyncio

def generate(query):
    if not query.strip():
        return "Please enter a query."
    # Directly call async retriever
    return asyncio.run(retriever.retrieve(query))

gradio_app = gr.Interface(
    fn=generate,
    inputs=gr.Textbox(label="Ask something"),
    outputs=gr.Textbox(label="Answer"),
    title="Physical AI Backend"
)

gr.Interface(
    fn=generate,
    inputs=gr.Textbox(label="Ask something"),
    outputs=gr.Textbox(label="Answer"),
    title="Physical AI Backend"
).launch(server_name="0.0.0.0", server_port=7860)
