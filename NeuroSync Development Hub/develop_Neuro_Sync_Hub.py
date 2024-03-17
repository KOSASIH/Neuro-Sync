import requests
from bs4 import BeautifulSoup

def developNeuroSyncHub():
    # Define the URL of the NeuroSync website
    url = "https://www.neurosync.com/"
    
    # Send a GET request to the URL and store the response
    response = requests.get(url)
    
    # Check if the GET request was successful
    if response.status_code == 200:
        # Parse the HTML content of the response
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the relevant information from the parsed HTML content
        description = soup.find('div', {'class': 'description'}).text.strip()
        objectives = soup.find('div', {'class': 'objectives'}).text.strip()
        user_reviews = soup.find_all('div', {'class': 'user-review'})
        user_review_texts = [review.text.strip() for review in user_reviews]
        
        # Return the extracted information
        return description, objectives, user_review_texts
    else:
        # Return an error message if the GET request was not successful
        return "Error: Unable to retrieve information from the NeuroSync website."
