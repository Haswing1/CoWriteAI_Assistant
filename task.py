class BlogPostGenerationTask:
    def __init__(self, title, mindset_technique, target_audience, seo_keywords):
        self.title = title
        self.mindset_technique = mindset_technique
        self.target_audience = target_audience
        self.seo_keywords = seo_keywords

    def describe_task(self):
        return f"Generate a blog post titled '{self.title}' about the mindset technique '{self.mindset_technique}', aimed at the '{self.target_audience}', with SEO keywords: {self.seo_keywords}."

# Define other tasks here