import requests
from bs4 import BeautifulSoup
import csv
import time

# Target website (replace with ShadowFox or your site)
URL = "https://www.shadowfax.in/"  

def scrape_data(url):
    """Scrape data from given URL and return results as a list of dictionaries."""
    try:
        # Send request
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad status
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Example: Extract all article titles and links (customize for your ShadowFox site)
    data_list = []
    articles = soup.find_all("a")  # Example: get all <a> tags
    for article in articles:
        title = article.get_text(strip=True)
        link = article.get("href")
        if title and link:
            data_list.append({
                "title": title,
                "link": link
            })

    return data_list


def save_to_csv(data, filename="scraped_data.csv"):
    """Save scraped data into CSV file."""
    if not data:
        print("No data to save.")
        return

    keys = data[0].keys()
    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data saved successfully to {filename}")
    except Exception as e:
        print(f"Error saving data: {e}")


if __name__ == "__main__":
    print("Starting Web Scraper...")

    # Scrape one page (can loop for multiple)
    scraped_data = scrape_data(URL)

    # Save results
    save_to_csv(scraped_data)

    print("Scraping completed.")





import requests
from bs4 import BeautifulSoup
import csv
import time

# Base URL (replace with ShadowFox site)
BASE_URL = "https://www.shadowfax.in/"

def scrape_data(url):
    """Scrape data from a given URL and return results as a list of dictionaries."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # Example: Extract all article titles and links (customize as needed)
    data_list = []
    articles = soup.find_all("a")
    for article in articles:
        title = article.get_text(strip=True)
        link = article.get("href")
        if title and link:
            data_list.append({
                "title": title,
                "link": link
            })
    return data_list


def save_to_csv(data, filename="scraped_data.csv"):
    """Save scraped data into CSV file."""
    if not data:
        print("⚠️ No data to save.")
        return

    keys = data[0].keys()
    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        print(f"✅ Data saved successfully to {filename}")
    except Exception as e:
        print(f"❌ Error saving data: {e}")


if __name__ == "__main__":
    print("🚀 Starting Multi-Page Web Scraper...")

    all_data = []
    max_pages = 5  # Change this to the number of pages you want to scrape

    for page in range(1, max_pages + 1):
        url = BASE_URL.format(page)
        print(f"🔎 Scraping page {page}: {url}")
        page_data = scrape_data(url)
        if not page_data:  # Stop if no data found (end of pages)
            print("⚠️ No more data found. Stopping.")
            break
        all_data.extend(page_data)
        time.sleep(2)  # polite delay to avoid overloading server

    save_to_csv(all_data)

    print("🎉 Scraping completed.")
