from config import *

class EmbedSearch:
    """
    A class to interact with the embedded search API.
    """

    def search(self, query):
        """
        Performs a search operation.

        Parameters:
        - query (str): The search query string.

        Returns:
        - dict: A dictionary containing the search answer or message.
        """
        url = f"{BASE_URL}/search/"
        payload = {"query": query}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to perform search: {response.text}")
