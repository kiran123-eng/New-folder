import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the content of the webpage
url = 'https://timesofindia.indiatimes.com/entertainment/hindi/bollywood/news'  # Change this to the website you want to scrape
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Page fetched successfully!")
else:
    print("Failed to retrieve the page.")
    exit()

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract the headlines (specific to BBC)
headlines = soup.find_all('h3')  # This will find all <h3> tags, which usually contain headlines

# Step 4: Save the headlines to a file
with open('headlines.txt', 'w') as file:
    for idx, headline in enumerate(headlines):
        file.write(f"{idx+1}. {headline.get_text()}\n")  # Get the text content of the headline

print("Headlines saved to headlines.txt")
