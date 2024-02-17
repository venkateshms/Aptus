import requests

class RepoEmbedClient:
    BASE_URL = "http://aptus.bio"  # Hardcoded base URL

    def __init__(self, aptus_token):
        """
        Initializes the client with the aptus_token for authentication.
        """
        self.aptus_token = aptus_token

    def annotate(self, folder_path, output_path, lab_repo=None):
        """
        Annotates documents or patient records within the specified folder.

        Args:
            folder_path (str): Path to the folder containing the documents or patient records.
            output_path (str): Path where the annotated documents or patient records should be saved.
            lab_repo (str, optional): The lab repository to use for additional context in patient record annotations. Defaults to None.
        """
        endpoint = "/annotate_patient" if lab_repo else "/annotate_documents"
        payload = {
            "folder_path": folder_path,
            "output_path": output_path,
            "aptus_token": self.aptus_token,  # Use aptus_token for authentication
        }
        if lab_repo:  # Add lab_repo to payload if annotating patient records
            payload["lab_repo"] = lab_repo

        response = requests.post(f"{self.BASE_URL}{endpoint}", json=payload)
        if response.status_code == 200:
            print(f"Success: {response.json().get('message', 'Documents successfully annotated')}")
        else:
            raise Exception(f"Annotation request failed with status {response.status_code}: {response.text}")

    @classmethod
    def interactive_session(cls, aptus_token):
        """
        Starts an interactive session for annotating documents or patient records.
        """
        client = cls(aptus_token)
        print("Interactive session started. Type 'quit' to exit.")
        while True:
            action = input("Choose action (1 for documents, 2 for patient records, quit): ")
            if action.lower() == 'quit':
                print("Exiting...")
                break
            folder_path = input("Enter folder path: ")
            output_path = input("Enter output path: ")
            if action == '2':
                lab_repo = input("Enter lab repository: ")
                client.annotate(folder_path, output_path, lab_repo)
            elif action == '1':
                client.annotate(folder_path, output_path)
            else:
                print("Invalid action. Please choose 1 for documents, 2 for patient records, or type 'quit'.")

# Example usage
if __name__ == "__main__":
    aptus_token = "your_aptus_token_here"
    RepoEmbedClient.interactive_session(aptus_token)
