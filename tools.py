class ContentGenerationTool:
    def __init__(self, llm):
        self.llm = llm

    def run(self, topic):
        # Use the LLM to generate content based on the topic
        content = self.llm.generate_content(topic)
        return content

# Define other tools here