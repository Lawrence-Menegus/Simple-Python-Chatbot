# Simple-Python-Chatbot


<p> This Python program creates a user-friendly chatbot interface designed to assist with programming-related questions. Leveraging the power of OpenAI's GPT model (specifically "text-davinci-003" in this instance), it processes user inquiries related to programming and provides insightful responses.

At the core of the program is the CustomChat function, which takes a user's input (referred to as Programmer within the function) and sends it to the OpenAI API. The function is tailored with specific parameters such as temperature, max_tokens, and penalties to optimize the response quality and relevance to the user's question. The response from the OpenAI API is then cleaned up to remove any unnecessary whitespace before being presented to the user.

The program utilizes Gradio, an open-source library, to create a simple yet effective web interface for the chatbot. This interface includes a single text input where users can type their programming questions and a text output to display the chatbot's advice or solutions. The interface is titled "Programming Assistant" and comes with a brief description that guides the users on how to use it effectively.

To deploy the chatbot, the program initiates the Gradio interface with the interface.launch() command, making the chatbot accessible through a web page. This setup is particularly useful for programmers seeking quick help with coding problems, understanding programming concepts, or even getting coding tips and best practices.

This program stands out as a practical tool for coding enthusiasts, students, and professionals alike, offering on-demand programming assistance through an intuitive chat interface. </p>


# Setup 

<p> install the required libraries using pip, Python's package installer. The main libraries you need are openai for accessing OpenAI's API and gradio for the web interface. Run the following command <p> </p>

## pip install openai gradio 

<p> do this in your terminal for the Python environment</p>

### Obtain OpenAI API Key
<p> To use OpenAI's API, you need an API key. If you don't already have one, sign up at OpenAI's website and follow the instructions to obtain your API key. You will need to insert this API key into your code where it says "APi Key" </p>
