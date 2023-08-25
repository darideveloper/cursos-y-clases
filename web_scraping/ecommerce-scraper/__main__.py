from scraping.web_scraping import WebScraping

scraper = WebScraping()

producto = "protein"

scraper.set_page ("https://www.amazon.com/s?k=protein")

# https://www.amazon.com/s?k=protein&s=review-rank

print ("Done")