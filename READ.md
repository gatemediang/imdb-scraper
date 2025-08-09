
# 🎬 IMDb Top 25 Movies Scraper
A simple and efficient Python script that scrapes the titles, release years, and ratings of the top 25 movies from IMDb's chart. The collected data is then saved into a clean CSV file for easy use in data analysis or other projects.

This project is an excellent beginner-friendly example of web scraping using Python's most popular libraries.

### ✨ Features
**Scrapes Key Data:** Extracts the movie title, year of release, and user rating.

**Polite Scraping:** Uses a User-Agent header to identify the script to the web server.

**Error Handling:** Gracefully skips over any list items that don't match the expected format.

**Structured Output:** Saves the data into a well-formatted imdb_top_25.csv file using the pandas library.

### 🚀 Getting Started
Follow these instructions to get a local copy up and running.

**Prerequisites**
Make sure you have Python 3 installed on your system.

**Installation & Usage**
Clone the repository:

```git clone https://github.com/gatemediang/imdb-scraper.git```  
```cd imdb-scraper```

**Create and activate a virtual environment (recommended):**

**Windows:**

`python -m venv venv`  
`.\venv\Scripts\activate`

**macOS / Linux:**

`python3 -m venv venv`  
`source venv/bin/activate`

Install the required packages:
(using requirements.txt or install separately listed libraries in the requirements.txt file).

`pip install -r requirements.txt`

Run the scraper:

`python imdbscrapper.py`

After running, the imdb_top_25_movies.csv file will be created in the project directory.

📂 Project Structure
imdbscrapper/
├── .gitignore  
├── imdbscrapper.py  
├── imdb_top_25.csv  
└── README.md  
|__requirements.tx