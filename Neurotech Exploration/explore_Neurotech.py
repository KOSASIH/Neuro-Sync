import requests
from bs4 import BeautifulSoup

def exploreNeurotech():
    url = "https://www.arxiv-vanity.com/search/?q=neurotechnology&search_type=all&start=0&max_results=10"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', class_='result')

    print("Exploring advancements in neurotechnology:")
    for result in results:
        title = result.find('span', class_='title mathjax').text
        authors = result.find('span', class_='authors').text
        abstract = result.find('span', class_='abstract').text
        link = result.find('a', class_='title mathjax')['href']

        print("\nTitle:", title)
        print("Authors:", authors)
        print("Abstract:", abstract)
        print("Link:", link)
