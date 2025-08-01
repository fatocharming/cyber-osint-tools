import requests

def fetch_http_headers(url):
    """
    Fetches the HTTP headers from a given URL.

    Args:
        url (str): The URL from which to fetch the headers.

    Returns:
        dict: A dictionary containing the HTTP headers.
    """
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        
        # Return the headers as a dictionary
        return response.headers
    except requests.exceptions.RequestException as e:
        print(f"Error fetching headers: {e}")
        return None

def analyze_headers(headers):
    """
    Analyzes HTTP headers and provides insights.

    Args:
        headers (dict): The HTTP headers to analyze.

    Returns:
        None
    """
    if headers:
        print("HTTP Headers Analysis:")
        # Check for common security headers
        security_headers = ['Strict-Transport-Security', 'Content-Security-Policy', 'X-Content-Type-Options', 'X-Frame-Options', 'X-XSS-Protection']
        
        for header in security_headers:
            if header in headers:
                print(f"{header}: Present")
            else:
                print(f"{header}: Not Present")
        
        # Print the server information
        server_info = headers.get('Server', 'No server information found')
        print(f"Server Information: {server_info}")
    else:
        print("No headers to analyze.")

def main():
    # Example URL for analysis
    url = input("Enter the URL to analyze (e.g., https://example.com): ")
    
    # Fetch and analyze the HTTP headers
    headers = fetch_http_headers(url)
    analyze_headers(headers)

if __name__ == "__main__":
    main()