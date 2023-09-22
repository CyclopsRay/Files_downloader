import argparse
import requests
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver

def download_files_from_website(base_dir, pattern, wait_time):
    driver = webdriver.Chrome()  # or whichever browser driver you prefer
    driver.get(base_dir)

    # Wait for content to load if necessary using WebDriverWait or time.sleep
    time.sleep(wait_time)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # Assuming pattern would be a CSS selector for your anchors.
    slides_links = soup.select(pattern)

    print(slides_links)

    for link in slides_links:
        file_url = base_dir.rstrip("/") + link['href']
        file_name = link['href'].split('/')[-1]
        r = requests.get(file_url, stream=True)
        file_path = os.path.expanduser(f"~/Downloads/{file_name}")
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download files from a website using a specific pattern.')
    parser.add_argument('--website', '-w', required=True, help='Website URL to scrape.')
    parser.add_argument('--pattern', '-p', required=True, help='CSS selector pattern to match links.')
    parser.add_argument('--time', '-t', help = "Time you want the website to wait.",default = 3)

    args = parser.parse_args()
    download_files_from_website(args.website, args.pattern, args.time)
