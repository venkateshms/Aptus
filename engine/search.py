import requests

class BaseSearchClient:
    def __init__(self, aptus_token):
        self.base_url = "http://aptus.bio"
        self.aptus_token = aptus_token

    def post_request(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json()["answer"]
        else:
            raise Exception(f"Request failed with status {response.status_code}: {response.text}")

    @classmethod
    def interactive_session(cls, aptus_token, path):
        raise NotImplementedError("This method should be implemented by subclasses.")
class SearchClient(BaseSearchClient):
    @classmethod
    def interactive_session(cls, aptus_token, text_file_path):
        client = cls(aptus_token)
        print("Enter your questions. Type 'quit' to exit.")
        while True:
            user_inquiry = input("Your question: ")
            if user_inquiry.lower() == 'quit':
                print("Exiting...")
                break
            try:
                result = client.post_request("/search", {
                    "text_file_path": text_file_path,
                    "aptus_token": client.aptus_token,
                    "user_inquiry": user_inquiry
                })
                print("Answer:", result)
            except Exception as e:
                print(f"An error occurred: {e}")

class RepoSearchClient(BaseSearchClient):
    @classmethod
    def interactive_session(cls, aptus_token, folder_path):
        client = cls(aptus_token)
        print("Enter your questions. Type 'quit' to exit.")
        while True:
            user_inquiry = input("Your question: ")
            if user_inquiry.lower() == 'quit':
                print("Exiting...")
                break
            try:
                result = client.post_request("/repo_search", {
                    "folder_path": folder_path,
                    "aptus_token": client.aptus_token,
                    "user_inquiry": user_inquiry
                })
                print("Answer:", result)
            except Exception as e:
                print(f"An error occurred: {e}")
if __name__ == "__main__":
    aptus_token = "your_aptus_token_here"
    
    # Example usage for SearchClient
    text_file_path = "/path/to/your/text_file.txt"
    SearchClient.interactive_session(aptus_token, text_file_path)
    
    # Example usage for RepoSearchClient
    folder_path = "/path/to/your/folder_with_text_files"
    RepoSearchClient.interactive_session(aptus_token, folder_path)
