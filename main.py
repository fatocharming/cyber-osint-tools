import requests
from bs4 import BeautifulSoup
import argparse

def fetch_page(url):
    """
    Fetch the content of a webpage given its URL.
    Returns the HTML content of the page.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_metadata(html_content):
    """
    Extract metadata from the HTML content of a webpage.
    Returns a dictionary with title and meta description.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.title.string if soup.title else 'No title found'
    description = soup.find('meta', attrs={'name': 'description'})
    description_content = description['content'] if description else 'No description found'
    
    return {
        'title': title,
        'description': description_content
    }

def display_metadata(metadata):
    """
    Display the extracted metadata in a readable format.
    """
    print("Page Title: ", metadata['title'])
    print("Meta Description: ", metadata['description'])

def main(url):
    """
    Main function to orchestrate the fetching and extraction of metadata.
    """
    html_content = fetch_page(url)
    if html_content:
        metadata = extract_metadata(html_content)
        display_metadata(metadata)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch and extract metadata from a webpage.')
    parser.add_argument('url', type=str, help='The URL of the webpage to analyze')
    args = parser.parse_args()
    
    main(args.url)
```