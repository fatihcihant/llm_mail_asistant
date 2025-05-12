from src.utils.gmail_api import GmailClient

class EmailFetcherAgent:
    def __init__(self, credentials_path):
        self.client = GmailClient(credentials_path)

    def fetch_emails(self, max_results):
        """Fetch emails using GmailClient."""
        return self.client.fetch_emails(max_results=max_results)