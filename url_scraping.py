import urllib.request
import requests
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Inputs
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))


for i in range(count):
    print("Retrieving:", url)
    
    # Read and parse the HTML
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Find all the anchor tags
    tags = soup('a')
    
    # Get the URL at the desired position
    url = tags[position - 1].get('href')

# Final retrieval
print("Retrieving:", url)

# You can also extract the name at the end like this:
name = url.split('_')[-1].split('.')[0]
print("Last name in sequence:", name)