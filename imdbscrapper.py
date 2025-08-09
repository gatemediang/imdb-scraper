# Step 1: Import the libraries we will use
import requests  # To make HTTP requests to the webpage
from bs4 import BeautifulSoup  # To parse the HTML and find elements
import pandas as pd  # To structure our data and save it to a CSV

# Step 2: Define the target URL and headers
# The URL is the page we want to scrape.
url = "https://www.imdb.com/chart/top/"

# Some websites block requests that don't look like they're from a real browser.
# This 'User-Agent' header makes our script pretend to be a browser.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Step 3: Make the request and parse the response
# We send a GET request to the URL, including our headers.
response = requests.get(url, headers=headers)

# We use BeautifulSoup to turn the raw HTML text from the response into a structured object.
soup = BeautifulSoup(response.text, "html.parser")

# ... (Steps 1, 2, and 3 are the same) ...

# Step 4: Find the parent container and then all movie items within it
# Find the main container for all movie items
movie_list_container = soup.find("ul", class_="ipc-metadata-list")
# Find all list items inside the container
movie_list_items = movie_list_container.find_all(
    "li", class_="ipc-metadata-list-summary-item"
)

# This is an empty list where we will store the dictionaries of movie data.
movies_data = []

# We loop through each of the 'li' elements we found.
for movie_item in movie_list_items:
    try:
        # Inside each 'li', we find the specific elements holding the data we want.
        title_tag = movie_item.find("h3", class_="ipc-title__text")
        # The title text now includes the number, e.g., "1. The Shawshank Redemption"
        title = (
            title_tag.text.split(". ", 1)[1]
            if ". " in title_tag.text
            else title_tag.text
        )

        metadata_div = movie_item.find("div", class_="cli-title-metadata")
        metadata_spans = metadata_div.find_all("span")
        year = metadata_spans[0].text  # The first span is the year

        rating_div = movie_item.find("div", class_="cli-ratings-container")
        rating = rating_div.find("span", class_="ipc-rating-star").text.split()[
            0
        ]  # The first part of the text is the rating number

        # We append a dictionary containing our clean data to the main list.
        movies_data.append(
            {
                "Title": title,
                "Year": year,
                "Rating": float(rating),  # Convert rating to a number
            }
        )
    except Exception as e:
        # If any movie item has a different layout and causes an error, we skip it.
        print(f"Skipping an item due to error: {e}")
        continue

    # Step 5: Convert to a DataFrame and save to CSV
# We convert our list of dictionaries into a pandas DataFrame for easy handling.
df = pd.DataFrame(movies_data)

# Print the first 5 rows of our data to check it.
print("--- Top 5 Movies Scraped ---")
print(df.head())

# Save the complete DataFrame to a CSV file in the same folder.
# 'index=False' prevents pandas from writing row numbers into the file.
df.to_csv("imdb_top_25_movies.csv", index=False)

print("\n✅ Data successfully saved to imdb_top_25_movies.csv")
