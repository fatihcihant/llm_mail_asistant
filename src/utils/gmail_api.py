import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class GmailClient:
    def __init__(self, credentials_path, scopes=None):
        """Initialize Gmail API client with OAuth2 authentication."""
        if scopes is None:
            scopes = ["https://www.googleapis.com/auth/gmail.readonly"]
        self.scopes = scopes
        self.credentials_path = credentials_path
        self.service = self._authenticate()

    def _authenticate(self):
        """Authenticate and build Gmail API service."""
        creds = None
        # Check if token.json exists for stored credentials
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", self.scopes)
        
        # If no valid credentials, prompt user to authenticate
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_path, self.scopes
                )
                creds = flow.run_local_server(port=0)
                # Save credentials for future use
                with open("token.json", "w") as token:
                    token.write(creds.to_json())
        
        try:
            return build("gmail", "v1", credentials=creds)
        except Exception as e:
            raise Exception(f"Failed to build Gmail service: {str(e)}")

    def fetch_emails(self, max_results=10):
        """Fetch emails from the user's inbox."""
        try:
            # Fetch list of email messages
            results = (
                self.service.users()
                .messages()
                .list(userId="me", maxResults=max_results)
                .execute()
            )
            messages = results.get("messages", [])
            if not messages:
                return []

            emails = []
            for message in messages:
                # Get full email details
                msg = (
                    self.service.users()
                    .messages()
                    .get(userId="me", id=message["id"], format="full")
                    .execute()
                )
                
                # Extract headers (e.g., Subject, From)
                headers = {h["name"]: h["value"] for h in msg["payload"]["headers"]}
                subject = headers.get("Subject", "No Subject")
                from_addr = headers.get("From", "Unknown Sender")
                
                # Extract email content (snippet or body)
                content = msg.get("snippet", "")
                
                # Optionally, extract full body - this is simplified
                if "parts" in msg["payload"]:
                    for part in msg["payload"]["parts"]:
                        if part["mimeType"] == "text/plain":
                            content = part.get("body", {}).get("data", content)
                            break
                
                emails.append({
                    "id": msg["id"],
                    "subject": subject,
                    "from": from_addr,
                    "content": content
                })
            
            return emails

        except HttpError as error:
            raise Exception(f"Error fetching emails: {str(error)}")