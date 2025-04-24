#Getting the Links from Giithub

# Not a fix, but helps debug:
import socket
import requests
from bs4 import BeautifulSoup



url = input("Enter the Site url (example.com): ")
#print(socket.gethostbyname('https://jadi.net'))
response = requests.get('https://'+ url, timeout = 10)
try:
    soup = BeautifulSoup(response.text, 'html.parser')
    tags = soup('a')
    for tag in tags:
        print(tag.get('href', None))
except Exception as e:
    print(f"Error occured : {e}")




