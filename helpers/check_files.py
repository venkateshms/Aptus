import os
import json

def check_files(folder_path):
    corrupted_files = []
    total_files = 0

    for filename in os.listdir(folder_path):
        # Check only for .json and .txt files
        if filename.endswith('.json') or filename.endswith('.txt'):
            total_files += 1
            file_path = os.path.join(folder_path, filename)

            try:
                if filename.endswith('.json'):
                    # Attempt to parse JSON to check for corruption
                    with open(file_path, 'r') as f:
                        json.load(f)
                else:
                    # Attempt to open text files to check for basic read issues
                    with open(file_path, 'r') as f:
                        pass  # Just opening to check for errors, no need to read content
            except Exception as e:
                print(f"Error opening or parsing file {filename}: {e}")
                corrupted_files.append(filename)

    # Report results
    print(f"Total files checked: {total_files}")
    print(f"Corrupted files: {len(corrupted_files)}")
    if corrupted_files:
        print("Corrupted file names:")
        for name in corrupted_files:
            print(name)

# Example usage
if __name__ == "__main__":
    folder_path = "/path/to/your/folder"  # Replace with the path to your folder
    check_files(folder_path)
