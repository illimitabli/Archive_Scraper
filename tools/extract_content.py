from bs4 import BeautifulSoup
import sys

def extract_paragraphs(html_file):
    with open(html_file, 'r') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            print(paragraph.text)

if __name__ == "__main__":
    html_file = sys.argv[1]
    extract_paragraphs(html_file)
