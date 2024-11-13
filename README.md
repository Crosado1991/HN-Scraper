##HN Scraper is a Python-based project designed to scrape article titles, links, and upvotes from the Hacker News homepage. The program ranks articles by upvotes, displaying the top articles with the highest engagement. It also saves all scraped data to a CSV file, providing an organized and exportable format for further analysis.

#Features
Scrapes Top Articles: Collects article titles, links, and upvote counts from Hacker News.
Ranks by Upvotes: Sorts articles by upvotes to identify the most popular stories.
Exports to CSV: Saves data to a CSV file for further analysis or record-keeping.
Technologies Used
Python: The core language for the script.
BeautifulSoup: For parsing HTML content.
requests: To handle HTTP requests and retrieve webpage data.
csv: To save data in a structured format.
Setup and Installation
Prerequisites
Python 3.x installed on your machine.
Required libraries:
BeautifulSoup from bs4
requests
You can install these libraries via pip:

#bash
Copy code
pip install beautifulsoup4 requests
Clone the Repository
bash
Copy code
git clone https://github.com/Crosado1991/HN-Scraper.git
cd HN-Scraper
Usage
Run the Script:

#bash
Copy code
python main.py

#Output:

The top 5 articles with the highest upvotes will be printed to the console.
A CSV file named hacker_news_articles.csv will be created in the project folder containing titles, links, and upvote counts for all articles on the homepage.

#Project Structure
bash
Copy code
HN-Scraper/
├── main.py                # Main script to run the scraper
├── hacker_news_articles.csv  # CSV file output
└── README.md              # Project documentation
#Notes
URL structure: This scraper only works on the Hacker News homepage (https://news.ycombinator.com/news). Expanding the scope will require additional code for pagination or other page structures.
Error handling: If certain elements are missing (e.g., articles with no upvotes), the script will handle these cases gracefully by assigning zero upvotes.
