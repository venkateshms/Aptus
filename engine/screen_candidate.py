from config import *

class ScreenCandidate:
    """
    A class to interact with the screen candidate API.
    """

    def generate_screening(self, directory_path, output_file_path, append_directory_path):
        """
        Initiates the screening generation process.

        Parameters:
        - directory_path (str): The path to the directory containing documents for screening.
        - output_file_path (str): The path to save the output file.
        - append_directory_path (str): The path to the directory where additional documents are stored.

        Returns:
        - dict: A dictionary containing the response message.
        """
        url = f"{BASE_URL}/generate_screening/"
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
            raise Exception(f"Failed to initiate screening generation: {response.text}")


# # Instantiate ScreenCandidate class
# screen_candidate_api = ScreenCandidate()

# # Generate screening
# response = screen_candidate_api.generate_screening('/path/to/documents_directory', '/path/to/output_file.txt', '/path/to/append_directory')
# print(response)
