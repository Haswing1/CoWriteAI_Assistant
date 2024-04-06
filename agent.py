import os
from dotenv import load_dotenv
import llama  # Assuming you have llama-index installed
from langchain.llms import HuggingFaceLLM
from langchain import LLMChain
# ... other imports for Gemini API interactions (if needed)

# Load environment variables
load_dotenv(Hugging_Face_Token)  

# Access API keys 
hf_token = os.getenv("HUGGINGFACE_API_KEY")

gemini_api_key = os.getenv("GEMINI_API_KEY")


class Agent:
    def __init__(self, role, goal, backstory, verbose, allow_delegation, llm, tools):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.verbose = verbose
        self.allow_delegation = allow_delegation
        self.llm = llm
        self.tools = tools

    def perform_task(self, task):
        # Logic to perform the task using the tools and LLM
        pass


if __name__ == "__main__":
    # ...  Get user input ...
    user_question = input("Ask a question: ")
    answer = process_user_query(user_question)
    print(answer) 
