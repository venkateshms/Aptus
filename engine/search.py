import requests

class SearchClient:
    def __init__(self, aptus_token):
        self.base_url = "http://aptus.bio" 
        self.aptus_token = aptus_token

    def search(self, text_file_path, user_inquiry):
        url = f"{self.base_url}/search"
        payload = {
            "text_file_path": text_file_path,
            "aptus_token": self.aptus_token,  #
            "user_inquiry": user_inquiry
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json()["answer"]
        else:
            raise Exception(f"Search request failed with status {response.status_code}: {response.text}")

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
                result = client.search(text_file_path, user_inquiry)
                print("Answer:", result)
            except Exception as e:
                print(f"An error occurred: {e}")
                
class RepoSearchClient:
    def __init__(self, aptus_token):
        self.base_url = "http://aptus.bio"  # fixed
        self.aptus_token = aptus_token

    def search(self, folder_path, user_inquiry):
        url = f"{self.base_url}/repo_search"
        payload = {
            "folder_path": folder_path,
            "aptus_token": self.aptus_token,  # Using aptus_token 
            "user_inquiry": user_inquiry
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json()["answer"]
        else:
            raise Exception(f"Search request failed with status {response.status_code}: {response.text}")

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
                result = client.search(folder_path, user_inquiry)
                print("Answer:", result)
            except Exception as e:
                print(f"An error occurred: {e}")
                
if __name__ == "__main__":
    # Initialize the SearchClient with the API token
    aptus_token = "your_aptus_token_here"
    text_file_path = "/path/to/your/text_file.txt"
    
    # Start an interactive session where the user can ask questions
    # The answers will be based on the content of the specified text file
    SearchClient.interactive_session(aptus_token, text_file_path)

if __name__ == "__main__":
    # Initialize the RepoSearchClient with the API token
    aptus_token = "your_aptus_token_here"
    folder_path = "/path/to/your/folder_with_text_files"
    
    # Start an interactive session where the user can ask questions
    # The answers will be based on the content of the text files within the specified folder
    RepoSearchClient.interactive_session(aptus_token, folder_path)
