from bs4 import BeautifulSoup

# Load the HTML file
with open('content.html', 'r') as f:
    html = f.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all href links
links = soup.find_all('a', href=True)

# Filter out the links that contain "indianexporters"
indian_links = [link['href'] for link in links if 'indianexporters' in link['href']]
unique_links = list(set(indian_links))
print(unique_links)