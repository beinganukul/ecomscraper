from bs4 import BeautifulSoup

# Load the HTML file
with open('sub_subcategory.html', 'r') as f:
    html = f.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')
title_div = soup.find('div', {'class': 'title-name'})

# Find the h1 tag inside the title_div
h1_tag = title_div.find('h1')

# Extract the text inside the h1 tag
h1_text = h1_tag.text

# Print the extracted text
print(h1_text)
isbimg_divs = soup.find_all('div', {'class': 'isbimg'})

# Extract the text inside the a tag of each isbimg_div
for div in isbimg_divs:
    a_tag = div.find('a', {'class': 's-tile'})
    a_text = a_tag.text
    print(a_text)