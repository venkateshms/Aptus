from config import *

class AnswerMessages:
    """
    A class to interact with the answer messages API.
    """

    def process_questions(self, directory_path, csv_file_path, output_csv_file_path):
        """
        Processes questions using the provided directory path, CSV file path, and output CSV file path.

        Parameters:
        - directory_path (str): The directory path containing question files.
        - csv_file_path (str): The path to the CSV file containing questions.
        - output_csv_file_path (str): The path to save the output CSV file.

        Returns:
        - dict: A dictionary containing the response message.
        """
        payload = {
            "directory_path": directory_path,
            "csv_file_path": csv_file_path,
            "output_csv_file_path": output_csv_file_path
        }
        response = requests.post(f"{BASE_URL}/process_questions", json=payload)
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return {"error": "Failed to decode JSON response", "status_code": response.status_code, "response": response.text}



# # Instantiate AnswerMessages class
# answer_messages_api = AnswerMessages()

# # Process questions
# response = answer_messages_api.process_questions('/path/to/directory', '/path/to/csv_file.csv', '/path/to/output_csv.csv')
# print(response)
