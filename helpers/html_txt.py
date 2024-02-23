from bs4 import BeautifulSoup
import os

def html_to_text(html_file, output_dir):
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract text
    plain_text = soup.get_text()

    # Define output file path
    file_name = os.path.splitext(os.path.basename(html_file))[0] + ".txt"
    output_file = os.path.join(output_dir, file_name)

    # Write plain text to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(plain_text)

    print(f"HTML content successfully converted and saved as plain text in {output_file}")

# Example usage:
if __name__ == "__main__":
    html_file = "example.html"  # Path to the HTML file
    output_dir = "output"  # Desired output directory

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Convert HTML to text and save to the specified directory
    html_to_text(html_file, output_dir)
