"""scarping scrapethissite.com to extract data 
 saving them in database 
 using machine learning to predict the area via population"""


import requests
from bs4 import BeautifulSoup
import pymysql 
from sklearn import tree
import numpy as np

#connecting to mariadb and reaching database
conn = pymysql.connect(
    host = 'localhost',
    user = 'sepehretemadi',
    password = 'yourpassword',
    database = 'my_db'
)

#creating a cursor 
cursor = conn.cursor()

url = 'https://www.scrapethissite.com/pages/simple/'

#get request to scrap 
r = requests.get(url=url, headers = {}, timeout = 10)

soup = BeautifulSoup(r.text, 'html.parser')

#extracing information
lands = soup.find_all('div', class_="col-md-4 country")

for land in lands:
    land_name = land.find('h3', class_='country-name').get_text(strip=True)
    land_capital = land.find('span', class_='country-capital').get_text(strip=True)
    land_population = land.find('span', class_='country-population').get_text(strip=True)
    land_area = land.find('span', class_='country-area').get_text(strip=True)

    #saving in database
    cursor.execute(
            "INSERT INTO lands (name , capital, population, area) VALUES(%s, %s, %s, %s)", 
            (land_name, land_capital, int(land_population), float(land_area))
            )


cursor.execute("SELECT * FROM lands")

#starting machine learning process
data = cursor.fetchall()

x = []
y = []
for item in data:
    population = item[3]
    area = item[4]
    if population > 0:
        x.append([population])
        y.append(area)

x = np.array(x)
y = np.array(y)
clf = tree.DecisionTreeRegressor()
clf = clf.fit(x,y)

n = int(input("Enter the Population to predict the Area:  "))
new_data = np.array([n]).reshape(-1,1)
answer = clf.predict(new_data)
print(f"Predicted Area ---> {answer[0]}")

conn.commit()
cursor.close()
conn.close()
