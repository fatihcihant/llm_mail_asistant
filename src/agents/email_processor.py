from src.utils.gemini_api import GeminiClient

class EmailProcessorAgent:
    def __init__(self, api_key):
        self.gemini = GeminiClient(api_key)

    def summarize_email(self, content):
        prompt = f"Summarize the following email in 2-3 sentences:\n{content}"
        return self.gemini.generate_content(prompt)

    def detect_urgency(self, content):
        prompt = f"Determine if this email is urgent. Return 'True' or 'False':\n{content}"
        return self.gemini.generate_content(prompt).strip() == "True"

    def analyze_sentiment(self, content):
        prompt = f"Analyze the sentiment of this email (positive, negative, neutral):\n{content}"
        return self.gemini.generate_content(prompt).strip()

    def generate_draft_reply(self, content):
        prompt = f"Generate a polite draft reply for this urgent email:\n{content}"
        return self.gemini.generate_content(prompt)