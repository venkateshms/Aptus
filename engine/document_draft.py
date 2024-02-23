from config import *

class DocumentDraft:
    """
    A class to interact with the document draft API.
    """

    def generate_discovery(self, folder_path, output_csv_path):
        """
        Initiates the discovery generation process.

        Parameters:
        - folder_path (str): The path to the folder containing documents for discovery.
        - output_csv_path (str): The path to save the output CSV file.

        Returns:
        - dict: A dictionary containing the response message.
        """
        url = f"{BASE_URL}/generate_discovery/"
        payload = {
            "folder_path": folder_path,
            "output_csv_path": output_csv_path
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to initiate discovery generation: {response.text}")

    def generate_draft(self, directory_path, output_file_path, append_directory_path):
        """
        Initiates the draft generation process.

        Parameters:
        - directory_path (str): The path to the directory containing documents for draft generation.
        - output_file_path (str): The path to save the output file.
        - append_directory_path (str): The path to the directory where additional documents are stored.

        Returns:
        - dict: A dictionary containing the response message.
        """
        url = f"{BASE_URL}/generate_draft/"
        payload = {
            "directory_path": directory_path,
            "output_file_path": output_file_path,
            "append_directory_path": append_directory_path
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to initiate draft generation: {response.text}")
        
        
# document_draft_api = DocumentDraft()
# # Generate discovery
# discovery_response = document_draft_api.generate_discovery('/path/to/documents_folder', '/path/to/output_csv.csv')
