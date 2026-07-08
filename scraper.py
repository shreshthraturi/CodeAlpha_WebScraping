import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target Website
url = "https://books.toscrape.com/"

# Send HTTP Request
response = requests.get(url)

# Check request status
if response.status_code == 200:
    print("Website Loaded Successfully!")
else:
    print("Failed to Load Website")
    exit()

# Parse HTML
soup = BeautifulSoup(response.text, "lxml")

# Find all books
books = soup.find_all("article", class_="product_pod")

# Empty list to store data
book_data = []

# Loop through each book
for book in books:

    # Book Title
    title = book.h3.a["title"]

    # Price
    price = book.find("p", class_="price_color").text

    # Availability
    availability = book.find("p", class_="instock availability").text.strip()

    # Rating
    rating = book.find("p")["class"][1]

    # Product Link
    link = "https://books.toscrape.com/catalogue/" + book.h3.a["href"].replace("../", "")

    # Store data
    book_data.append({
        "Title": title,
        "Price": price,
        "Availability": availability,
        "Rating": rating,
        "Product Link": link
    })

# Create DataFrame
df = pd.DataFrame(book_data)

# Display Data
print(df)

# Save to CSV
df.to_csv("books_data.csv", index=False)

print("\nData Successfully Saved as books_data.csv")