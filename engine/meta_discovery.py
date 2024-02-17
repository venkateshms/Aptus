import requests
import csv
import os
import json

class RepoEmbedClient:
    BASE_URL = "http://aptus.bio"

    def __init__(self, aptus_token):
        self.aptus_token = aptus_token

    def fetch_meta_data(self, subject_id):
        """
        Fetches metadata for a given subject ID from the /meta endpoint.
        """
        url = f"{self.BASE_URL}/meta"
        headers = {"Authorization": f"Bearer {self.aptus_token}"}
        params = {"subject_id": subject_id}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve meta data for subject {subject_id}: {response.text}")
            return {}

    def generate_cohort_csv(self, annotated_folder_path, csv_output_path, headers):
        """
        Generates a CSV file from metadata fetched for each subject using the /meta endpoint.
        """
        with open(csv_output_path, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()

            # Assuming annotated documents contain subject IDs to fetch metadata
            for filename in os.listdir(annotated_folder_path):
                if filename.endswith(".json"):
                    # Extract subject ID from filename
                    with open(os.path.join(annotated_folder_path, filename), 'r') as f:
                        doc = json.load(f)
                        subject_id = doc.get('subject_id')

                    if subject_id:
                        meta_data = self.fetch_meta_data(subject_id)
                        row = {header: meta_data.get(header, "") for header in headers}
                        writer.writerow(row)
                    else:
                        print(f"Subject ID not found in {filename}")

        print(f"CSV file successfully generated at {csv_output_path}")

# Example Usage
if __name__ == "__main__":
    aptus_token = "your_aptus_token"  # Replace with your actual token
    annotated_folder_path = "/path/to/annotated/documents"  # Folder with annotated JSON documents
    csv_output_path = "/path/to/output/metadata.csv"  # Output CSV file path
    headers = ["subject_id", "attribute1", "attribute2"]  # Define headers based on the expected metadata

    client = RepoEmbedClient(aptus_token)
    client.generate_cohort_csv(annotated_folder_path, csv_output_path, headers)
