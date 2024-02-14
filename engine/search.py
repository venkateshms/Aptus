import requests

class SearchClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def search(self, text_file_path, azure_deployment_embed, azure_deployment_llm, user_inquiry):
        url = f"{self.base_url}/search"
        payload = {
            "text_file_path": text_file_path,
            "azure_deployment_embed": azure_deployment_embed,
            "azure_deployment_llm": azure_deployment_llm,
            "user_inquiry": user_inquiry
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json()["answer"]
        else:
            raise Exception(f"Search request failed with status {response.status_code}: {response.text}")

    @classmethod
    def interactive_session(cls, base_url, text_file_path, azure_deployment_embed, azure_deployment_llm):
        client = cls(base_url)
        print("Enter your questions. Type 'quit' to exit.")
        while True:
            user_inquiry = input("Your question: ")
            if user_inquiry.lower() == 'quit':
                print("Exiting...")
                break

            try:
                result = client.search(text_file_path, azure_deployment_embed, azure_deployment_llm, user_inquiry)
                print("Answer:", result)
            except Exception as e:
                print(f"An error occurred: {e}")
# Simplified usage
# if __name__ == "__main__":
#     base_url = "http://localhost:5035"
#     text_file_path = "/Users/mvenkatesh/Desktop/aptus/synthea_sample_data_fhir_latest/Abby752_Rowe323_b728d428-0526-5fcb-bdd7-04bb48323b9f.txt"
#     azure_deployment_embed = "aptus_embed_demo"
#     azure_deployment_llm = "aptus35"
#     SearchClient.interactive_session(base_url, text_file_path, azure_deployment_embed, azure_deployment_llm)

# SearchClient.interactive_session("http://localhost:5035", "/path/to/text_file.txt", "azure_deployment_embed_name", "azure_deployment_llm_name")


import requests

class RepoSearchClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def search(self, folder_path, azure_deployment_embed, azure_deployment_llm, user_inquiry):
        """
        Performs a search operation by sending a POST request to the /repo_search endpoint.

        :param folder_path: Path to the folder containing text files to be analyzed.
        :param azure_deployment_embed: Azure deployment name for embeddings.
        :param azure_deployment_llm: Azure deployment name for language model operations.
        :param user_inquiry: The user's inquiry/question.
        :return: The search result.
        """
        url = f"{self.base_url}/repo_search"
        payload = {
            "folder_path": folder_path,
            "azure_deployment_embed": azure_deployment_embed,
            "azure_deployment_llm": azure_deployment_llm,
            "user_inquiry": user_inquiry
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json()["answer"]
        else:
            raise Exception(f"Search request failed with status {response.status_code}: {response.text}")

    @classmethod
    def interactive_session(cls, base_url, folder_path, azure_deployment_embed, azure_deployment_llm):
        """
        Starts an interactive session that allows the user to ask questions in a loop.

        :param base_url: The base URL of the application providing the search functionality.
        :param folder_path: Path to the folder containing text files to be analyzed.
        :param azure_deployment_embed: Azure deployment name for embeddings.
        :param azure_deployment_llm: Azure deployment name for language model operations.
        """
        client = cls(base_url)
        print("Enter your questions. Type 'quit' to exit.")
        while True:
            user_inquiry = input("Your question: ")
            if user_inquiry.lower() == 'quit':
                print("Exiting...")
                break

            try:
                result = client.search(folder_path, azure_deployment_embed, azure_deployment_llm, user_inquiry)
                print("Answer:", result)
            except Exception as e:
                print(f"An error occurred: {e}")

# # Example usage
# if __name__ == "__main__":
#     base_url = "http://localhost:5036
#     folder_path = "/Users/mvenkatesh/Desktop/aptus/study_materials_dir"
#     azure_deployment_embed = "aptus_embed_demo"
#     azure_deployment_llm = "aptus35"
#     RepoSearchClient.interactive_session(base_url, folder_path, azure_deployment_embed, azure_deployment_llm)
