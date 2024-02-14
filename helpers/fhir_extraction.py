import os
import json
import base64
from html.parser import HTMLParser

class FHIRTextExtractor:
    def __init__(self, fhir_files_dir, output_dir):
        self.fhir_files_dir = fhir_files_dir
        self.output_dir = output_dir
        self.ensure_output_directory()

    def ensure_output_directory(self):
        """Ensure the output directory exists."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    class MyHTMLParser(HTMLParser):
        """Simple HTML parser to extract text from div elements."""
        def __init__(self):
            super().__init__()
            self.data = []

        def handle_data(self, data):
            self.data.append(data)

        def get_data(self):
            return " ".join(self.data)

    def decode_base64(self, data):
        """Decode a base64 encoded string, safely."""
        try:
            decoded_bytes = base64.b64decode(data, validate=True)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None  # Return None if the data is not valid base64

    def extract_text(self, obj):
        """Recursively search and extract natural language text."""
        extracted_texts = []

        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(value, str):
                    if key in ["valueString", "display", "div"]:
                        if key == "div":
                            parser = self.MyHTMLParser()
                            parser.feed(value)
                            extracted_texts.append(parser.get_data())
                        else:
                            extracted_texts.append(value)
                    elif key == "data":
                        decoded_data = self.decode_base64(value)
                        if decoded_data:
                            extracted_texts.append(decoded_data)
                elif isinstance(value, (dict, list)):
                    extracted_texts.extend(self.extract_text(value))

        elif isinstance(obj, list):
            for item in obj:
                extracted_texts.extend(self.extract_text(item))

        return extracted_texts

    def process_files(self):
        """Process each FHIR file in the directory."""
        for filename in os.listdir(self.fhir_files_dir):
            if filename.endswith('.json'):
                file_path = os.path.join(self.fhir_files_dir, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)

                extracted_texts = self.extract_text(data)

                if extracted_texts:
                    output_file_name = os.path.splitext(filename)[0] + '.txt'
                    output_file_path = os.path.join(self.output_dir, output_file_name)
                    with open(output_file_path, 'w', encoding='utf-8') as output_file:
                        output_file.write('\n\n'.join(extracted_texts))
                    print(f"Extracted data saved to {output_file_path}")
                else:
                    print(f"No natural language data found in {file_path}")
        print("Done processing all files.")

 #######
if __name__ == "__main__":
    fhir_files_dir = 'path_to_your_FHIR_files'
    output_dir = 'path_to_your_output_directory'
    extractor = FHIRTextExtractor(fhir_files_dir, output_dir)
    extractor.process_files()
