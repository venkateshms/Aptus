import os
import csv
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Function to authenticate and build Gmail service
def authenticate_gmail():
    creds = Credentials.from_authorized_user_file('credentials.json') # Path to your credentials file
    service = build('gmail', 'v1', credentials=creds)
    return service

# Function to retrieve emails
def get_emails(service, user_id='me', query=''):
    try:
        response = service.users().messages().list(userId=user_id, q=query).execute()
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])
        
        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().messages().list(userId=user_id, q=query, pageToken=page_token).execute()
            messages.extend(response['messages'])
        
        return messages
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to retrieve email details
def get_email_details(service, message_id, user_id='me'):
    try:
        message = service.users().messages().get(userId=user_id, id=message_id, format='metadata').execute()
        headers = message['payload']['headers']
        email_data = {}

        for header in headers:
            if header['name'] == 'From':
                email_data['From'] = header['value']
            elif header['name'] == 'To':
                email_data['To'] = header['value']
            elif header['name'] == 'Subject':
                email_data['Subject'] = header['value']
            elif header['name'] == 'Date':
                email_data['Date'] = header['value']
        
        return email_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to save email details to CSV
def save_to_csv(emails, csv_file):
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['From', 'To', 'Subject', 'Date'])
        writer.writeheader()
        for email in emails:
            writer.writerow(email)

def main():
    # Authenticate Gmail service
    service = authenticate_gmail()

    # Define the specific inbox you want to target
    specific_inbox = 'example@example.com'

    # Get emails from the specific inbox
    emails = get_emails(service, user_id=specific_inbox, query='')

    if emails:
        email_details = []
        for email in emails:
            email_id = email['id']
            details = get_email_details(service, email_id, user_id=specific_inbox)
            if details:
                email_details.append(details)

        # Save email details to CSV
        save_to_csv(email_details, 'subject_questions_gmail.csv')
        print("Emails from the inbox scraped successfully and saved to subject_questions_gmail.csv")
    else:
        print(f"No emails found in the inbox: {specific_inbox}")

if __name__ == "__main__":
    main()
