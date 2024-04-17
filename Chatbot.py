# Simple Ai Chatbot 
# Lawrence Menegus 
# Program Description: A simple Gui interface which allows the User to ask
# Progarmming questions with fairly accuracte results. Program uses OpenAI's API model for search results. 
 
import openai 
import gradio as gr

openai.api_key = " APi Key "

def CustomChat(Programmer):
    response = openai.Completion.create(

     # Uses OpenAI's Davinci-003 AI modle 
      engine="text-davinci-003",
      prompt=Programmer,
      temperature=0.7,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    message = response.choices[0].text
    return message.strip()

# Define the Gradio interface
interface = gr.Interface(
  CustomChat,
  inputs="text",
  outputs="text",
  title="Programming Assistant ",
  description="Enter a Programming Question and Recieve help",
)

# Launch the interface
interface.launch()
