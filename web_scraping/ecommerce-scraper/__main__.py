import os
from dotenv import load_dotenv
from chrome_dev.chrome_dev import ChromDevWrapper

# read .env file
load_dotenv ()
MAX_PRODUCTS = int(os.getenv ("MAX_PRODUCTS"))
CHROME_PATH = os.getenv ("CHROME_PATH")

START_PRODUCT_INDEX = 6

print ("(Amazon) Searching products...")

selectors = {
    'product': '[data-asin][data-uuid]',
    'image': 'img',
    'title': 'h2',
    'rate_num': 'span[aria-label]:nth-child(1)',
    'reviews': 'span[aria-label]:nth-child(2)',
    'sponsored': '[aria-label~="Sponsored"]',
    'best_seller': '.a-row.a-badge-region',
    'price': 'a.a-size-base .a-offscreen',
    'last_month_sales': 'div > span.a-size-base.a-color-secondary:only-child',
    'link': 'a',
}

# Open chrome and load results page
scraper = ChromDevWrapper(chrome_path=CHROME_PATH, start_killing=False)
scraper.set_page ("https://www.amazon.com/s?k=protein&s=review-rank")

# get the results in the page
results_num = scraper.count_elems (selectors['product'])

# Validate if there are results
if results_num == 0:
    print ("No results found")
    quit ()

current_index = START_PRODUCT_INDEX
extracted_products = 0

print ("(Amazon) Extracting data...")

products_data = []
while True:
    
    # Generate css selectors
    selector_product = selectors["product"] + f":nth-child({current_index})"
    selector_image = f'{selector_product} {selectors["image"]}'
    selector_title = f'{selector_product} {selectors["title"]}'
    selector_rate_num = f'{selector_product} {selectors["rate_num"]}'
    selector_reviews = f'{selector_product} {selectors["reviews"]}'
    selector_sponsored = f'{selector_product} {selectors["sponsored"]}'
    selector_best_seller = f'{selector_product} {selectors["best_seller"]}'
    selector_price = f'{selector_product} {selectors["price"]}'
    selector_last_month_sales = f'{selector_product} {selectors["last_month_sales"]}'
    selector_link = f'{selector_product} {selectors["link"]}'
    
    # Incress product counter
    current_index += 1
    
    # Validate if there are not more products in the page
    if current_index - START_PRODUCT_INDEX > results_num:
        print ("(Amazon) No more products")
        break
    
    # Skip products without price
    price = scraper.get_text (selector_price)
    if not price:
        continue
    
    # Skip sponsored products
    sponsored = scraper.get_text (selector_sponsored)
    if sponsored:
        continue
    
    # Extract text from selectors
    image = scraper.get_attrib (selector_image, "src")    
    title = scraper.get_text (selector_title)
    rate_num = scraper.get_text (selector_rate_num)
    reviews = scraper.get_attrib (selector_reviews, "aria-label")
    best_seller = scraper.get_text (selector_best_seller)
    last_month_sales = scraper.get_text (selector_last_month_sales)
    link = scraper.get_attrib (selector_link, "href")
        
    # Clean data 
    price = float(price.replace("$", ""))
    
    if rate_num:
        rate_num = float(rate_num[0:3])
    
    if reviews:
        reviews = int(reviews.replace(",", ""))
        
    if best_seller:
        best_seller = True
    else:
        best_seller = False
        
    if last_month_sales:
        last_month_sales = last_month_sales.split(" ")[0]
    
    # TODO: add referral link
    link = f"https://www.amazon.com{link}"
    
    # Incress counter of extracted products
    extracted_products += 1
    
    # Save data
    products_data.append ({
        "image": image, 
        "title": title,
        "rate_num": rate_num,
        "reviews": reviews,
        "price": price,
        "best_seller": best_seller,
        "last_month_sales": last_month_sales,
        "link": link,
    })
    
    
    # End loop when extract al required products
    if extracted_products >= MAX_PRODUCTS: 
        break
        
print (f"(Amazon) {extracted_products} products extracted")