import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = []
    authors = []

    for item in soup.find_all("div", class_="quote"):
        quote = item.find("span", class_="text").text
        author = item.find("small", class_="author").text

        quotes.append(quote)
        authors.append(author)

    data = pd.DataFrame({
        "Quote": quotes,
        "Author": authors
    })

    # Save to CSV
    data.to_csv("quotes.csv", index=False)

    print("Data successfully saved to quotes.csv")

else:
    print("Failed to fetch data.")
