from bs4 import BeautifulSoup
import requests
import csv

# Step 1: Send a GET request to the Hacker News homepage
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

# Step 2: Parse the HTML content
soup = BeautifulSoup(yc_web_page, "html.parser")

# Step 3: Extract article titles, links, and upvotes
articles = soup.find_all("span", class_="titleline")
article_data = []

for article_tag in articles:
    # Get the <a> tag within each <span class="titleline"> to extract title and link
    link_tag = article_tag.find("a")
    if link_tag:
        title = link_tag.get_text()
        link = link_tag.get("href")

        # Find the corresponding upvote count
        score_tag_container = article_tag.find_next_sibling("td")
        score_tag = score_tag_container.find("span", class_="score") if score_tag_container else None
        upvotes = int(score_tag.get_text().replace(" points", "")) if score_tag else 0

        # Append the data to the list
        article_data.append({
            "title": title,
            "link": link,
            "upvotes": upvotes
        })

# Step 4: Sort the articles by upvotes in descending order
sorted_articles = sorted(article_data, key=lambda x: x["upvotes"], reverse=True)

# Step 5: Print the top 5 articles by upvotes
print("Top 5 Articles by Upvotes:")
for article in sorted_articles[:5]:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Upvotes: {article['upvotes']}")
    print()

# Bonus: Save the article data to a CSV file
with open("hacker_news_articles.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["title", "link", "upvotes"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(sorted_articles)

print("Data saved to hacker_news_articles.csv")
