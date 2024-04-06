import os
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent, Task, Crew, Process
from langchain.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv

load_dotenv()
Google_API_KEY= os.getenv("Google_API_KEY")
Hugging_Face_Token= os.getenv("Hugging_Face_Token")

#Set gemini pro as llm
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class ChatGoogleGenerativeAI:
    def __init__(self, model, verbose, temperature, Google_API_KEY, Hugging_Face_Token):
        self.model = model
        self.verbose = verbose
        self.temperature = temperature
        self.Google_API_KEY = Google_API_KEY
        self.Hugging_Face_Token = Hugging_Face_Token

# Retrieve the Hugging Face token from the environment variables
Hugging_Face_Token = os.getenv("Hugging_Face_Token")

# create an instance of the ChatGoogleGenerativeAI class
# Assuming llm is an instance of a language model class
llm = ChatGoogleGenerativeAI(
    model="gemini-1.0-pro",
    verbose=True,
    temperature=0.5,
    Google_API_KEY=os.getenv("Google_API_KEY"),
    Hugging_Face_Token=os.getenv("Hugging_Face_Token")
)

# Define the blog_writer agent
blog_writer = Agent(
    role="AI Programming Assistant",
    goal="To create high-quality S.E.O. Articles and Blogs related to Mindset Transformation",
    backstory="Blog writer was born out of a need to assist with programming and computer science related queries.",
    verbose=True,
    allow_delegation=True,
    llm=llm,
    tools=[]  # Initially, the agent has no tools
)

#task to perform 