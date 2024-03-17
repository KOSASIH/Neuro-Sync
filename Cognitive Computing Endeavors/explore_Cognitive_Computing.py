import requests
from bs4 import BeautifulSoup

def exploreCognitiveComputing():
    """
    Explore cognitive computing concepts.
    """
    # Define the URL for the web search
    url = "https://www.google.com/search?q=cognitive+computing+concepts"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the response
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the search results
        search_results = soup.find_all("div", class_="g")

        # Extract the titles and URLs of the search results
        for result in search_results:
            title = result.find("h3").text
            url = result.find("a")["href"]

            # Print the title and URL
            print(f"Title: {title}\nURL: {url}\n")

    else:
        print("Failed to fetch search results.")
