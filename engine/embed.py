import requests
import json

class RepoEmbedClient:
    def __init__(self, base_url):
        """
        Initializes the client with the base URL of the embedding and annotation service.
        """
        self.base_url = base_url

    def annotate_documents(self, folder_path, azure_deployment_embed, azure_deployment_llm, output_path):
        """
        Annotates documents within the specified folder using embeddings and language model operations.

        Args:
            folder_path (str): The path to the folder containing the documents to be annotated.
            azure_deployment_embed (str): The name of the Azure deployment for embeddings.
            azure_deployment_llm (str): The name of the Azure deployment for language model operations.
            output_path (str): The path where annotated documents should be saved.
        """
        url = f"{self.base_url}/annotate_documents"
        payload = {
            "folder_path": folder_path,
            "azure_deployment_embed": azure_deployment_embed,
            "azure_deployment_llm": azure_deployment_llm,
            "output_path": output_path
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Documents successfully annotated and saved to:", output_path)
        else:
            raise Exception(f"Annotation request failed with status {response.status_code}: {response.text}")

    def annotate_patient(self, folder_path, azure_deployment_embed, azure_deployment_llm, lab_repo, output_path):
        """
        Annotates patient records within the specified folder using embeddings and language model operations,
        incorporating lab repository data.

        Args:
            folder_path (str): The path to the folder containing the patient records to be annotated.
            azure_deployment_embed (str): The name of the Azure deployment for embeddings.
            azure_deployment_llm (str): The name of the Azure deployment for language model operations.
            lab_repo (str): The lab repository to use for additional context in annotations.
            output_path (str): The path where annotated patient records should be saved.
        """
        url = f"{self.base_url}/annotate_patient"
        payload = {
            "folder_path": folder_path,
            "azure_deployment_embed": azure_deployment_embed,
            "azure_deployment_llm": azure_deployment_llm,
            "lab_repo": lab_repo,
            "output_path": output_path
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Patient records successfully annotated and saved to:", output_path)
        else:
            raise Exception(f"Annotation request failed with status {response.status_code}: {response.text}")

    @classmethod
    def interactive_session(cls, base_url):
        """
        Starts an interactive session for annotating documents or patient records.

        Args:
            base_url (str): The base URL of the application providing the annotation functionality.
        """
        print("Interactive session started. Type 'quit' to exit.")
        while True:
            action = input("Choose action (annotate_documents, annotate_patient, quit): ")
            if action.lower() == 'quit':
                print("Exiting...")
                break
            elif action in ['annotate_documents', 'annotate_patient']:
                folder_path = input("Enter folder path: ")
                azure_deployment_embed = input("Enter Azure deployment name for embeddings: ")
                azure_deployment_llm = input("Enter Azure deployment name for language model operations: ")
                output_path = input("Enter output path: ")
                if action == 'annotate_patient':
                    lab_repo = input("Enter lab repository: ")
                    cls(base_url).annotate_patient(folder_path, azure_deployment_embed, azure_deployment_llm, lab_repo, output_path)
                else:
                    cls(base_url).annotate_documents(folder_path, azure_deployment_embed, azure_deployment_llm, output_path)
            else:
                print("Invalid action. Please choose 'annotate_documents', 'annotate_patient', or 'quit'.")

#  usage
if __name__ == "__main__":
    base_url = "http://localhost:5000"
    RepoEmbedClient.interactive_session(base_url)
