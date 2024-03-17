import requests
from bs4 import BeautifulSoup

def synergyDeepLearning():
    # Define the URL of the NeuroSync website
    url = "https://www.neurosync.com/"
    
    # Send a GET request to the URL and store the response
    response = requests.get(url)
    
    # Check if the GET request was successful
    if response.status_code == 200:
        # Parse the HTML content of the response
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the relevant information from the parsed HTML content
        deep_learning_initiatives = soup.find_all('div', {'class': 'deep-learning-initiative'})
        initiative_titles = [initiative.find('h3').text.strip() for initiative in deep_learning_initiatives]
        initiative_descriptions = [initiative.find('p').text.strip() for initiative in deep_learning_initiatives]
        
        # Return the extracted information
        return initiative_titles, initiative_descriptions
    else:
        # Return an error message if the GET request was not successful
        return "Error: Unable to retrieve information from the NeuroSync website."
