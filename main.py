from agent import Agent
from tools import ContentGenerationTool
from tasks import BlogPostGenerationTask

# Assuming llm is defined and imported
llm = ...

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

# Add tools to the agent
content_generation_tool = ContentGenerationTool(llm)
blog_writer.tools.append(content_generation_tool)

# Define a task
example_task = BlogPostGenerationTask(
    title="The Power of Mindfulness for Stress Relief",
    mindset_technique="Mindfulness meditation",
    target_audience="Professionals in stressful fields",
    seo_keywords=["mindfulness", "meditation", "stress relief", "mental health"]
)

# Perform the task
blog_post_content = blog_writer.perform_task(example_task)
print(blog_post_content)