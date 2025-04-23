import requests
import bs4

url = "http://books.toscrape.com/"
response = requests.get(url, timeout=5, verify=False)
print("status = ",response.status_code)
try :
    data = response.text
    #print(data)

    soup = bs4.BeautifulSoup(data, features="html.parser")
    searching = soup.select('title')

    book_titles = soup.select(".product_pod h3 a")
    print("\n📚 لیست کتاب‌ها:")
    for book in book_titles:
        print("-", book["title"])

    book_images = soup.select(".product_pod img")
    print("\n🖼 لینک تصاویر:")
    for img in book_images:
        print("-", url + img["src"])

except Exception as e:
    print(f"An error occurred: {e}")