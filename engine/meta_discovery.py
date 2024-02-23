from config import *

class MetaDiscovery:
    """
    A class to interact with the meta discovery API.
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
        
# # Instantiate MetaDiscovery class
# meta_discovery_api = MetaDiscovery()

# # Generate discovery
# response = meta_discovery_api.generate_discovery('/path/to/documents_folder', '/path/to/output_csv.csv')
# print(response)
