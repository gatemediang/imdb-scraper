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

```git clone https://github.com/your-username/imdb-scraper.git
cd imdb-scraper```

**Create and activate a virtual environment (recommended):**

**Windows:

python -m venv venv
.\venv\Scripts\activate

macOS / Linux:

python3 -m venv venv
source venv/bin/activate

Install the required packages:
(It's good practice to create a requirements.txt file by running pip freeze > requirements.txt and then installing from it).

pip install requests beautifulsoup4 pandas

Run the scraper:

python scraper.py

After running, the imdb_top_250.csv file will be created in the project directory.

📂 Project Structure
imdb-scraper/
├── .gitignore         # Tells Git which files to ignore
├── scraper.py         # The main Python scraping script
├── imdb_top_250.csv   # The output data file (after running the script)
└── README.md          # You are here!

⚠️ Disclaimer
This script is intended for educational purposes only. Please be respectful of IMDb's terms of service and use this scraper responsibly. Do not send too many requests in a short period. The structure of websites changes frequently, so this script may need updates to continue working correctly in the future.