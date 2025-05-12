import os
import yaml
from dotenv import load_dotenv
from src.agents.email_fetcher import EmailFetcherAgent
from src.agents.email_processor import EmailProcessorAgent
from src.agents.notification_agent import NotificationAgent
from src.utils.config import load_config

def main():
    # Load environment variables and configuration
    load_dotenv()
    config = load_config("settings.yaml")

    # Initialize agents
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY not found in .env")

    fetcher = EmailFetcherAgent(credentials_path="credentials.json")
    processor = EmailProcessorAgent(api_key=gemini_api_key)
    notifier = NotificationAgent()

    # Fetch emails
    max_emails = config.get("max_emails", 10)
    emails = fetcher.fetch_emails(max_results=max_emails)

    # Process emails
    for email in emails:
        summary = processor.summarize_email(email["content"])
        is_urgent = processor.detect_urgency(email["content"])
        sentiment = processor.analyze_sentiment(email["content"])
        draft_reply = processor.generate_draft_reply(email["content"]) if is_urgent else None

        # Notify for urgent emails
        if is_urgent:
            notifier.notify(
                email_id=email["id"],
                subject=email["subject"],
                summary=summary,
                draft_reply=draft_reply
            )

        # Log email details
        print(f"Email ID: {email['id']}")
        print(f"Subject: {email['subject']}")
        print(f"Summary: {summary}")
        print(f"Urgency: {'Urgent' if is_urgent else 'Not Urgent'}")
        print(f"Sentiment: {sentiment}")
        if draft_reply:
            print(f"Draft Reply: {draft_reply}")
        print("-" * 50)

if __name__ == "__main__":
    main()