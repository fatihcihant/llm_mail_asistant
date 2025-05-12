class NotificationAgent:
    def notify(self, email_id, subject, summary, draft_reply):
        # Console notification (extensible to email, Slack, etc.)
        print(f"URGENT EMAIL DETECTED!")
        print(f"Email ID: {email_id}")
        print(f"Subject: {subject}")
        print(f"Summary: {summary}")
        if draft_reply:
            print(f"Suggested Reply: {draft_reply}")
        print("-" * 50)