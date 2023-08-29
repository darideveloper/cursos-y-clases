from chrome_dev.chrome_dev import ChromDevWrapper

MAX_PRODUCTS = 11
START_PRODUCT_INDEX = 6

selectors = {
    'product': '[data-asin][data-uuid]',
    'image': 'img',
    'title': 'h2',
    'rate_num': 'span[aria-label]:nth-child(1)',
    'reviews': 'span[aria-label]:nth-child(2)',
    'sponsored': '[aria-label~="Sponsored"]',
    'best_seller': '.a-row.a-badge-region',
    'price': 'a .a-offscreen',
    'last_month_sales': 'span.a-size-base.a-color-secondary',
    'link': 'a',
}

# Open chrome and load results page
chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
scraper = ChromDevWrapper(chrome_path=chrome_path, start_killing=False)
scraper.set_page ("https://www.amazon.com/s?k=protein&s=review-rank")

# get the results in the page
results = scraper.count_elems (selectors['product'])

# Validate if there are results
if not results:
    print ("No results found")
    quit ()

current_index = START_PRODUCT_INDEX
extracted_products = 0

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
    
    # Extract text from selectors
    image = scraper.get_attrib (selector_image, "src")    
    title = scraper.get_text (selector_title)
    rate_num = scraper.get_text (selector_rate_num)
    reviews = scraper.get_attrib (selector_reviews, "aria-label")
    sponsored = scraper.get_text (selector_sponsored)
    best_seller = scraper.get_text (selector_best_seller)
    price = scraper.get_text (selector_price)
    last_month_sales = scraper.get_text (selector_last_month_sales)
    link = scraper.get_attrib (selector_link, "href")
    
    # Clean data
    if rate_num:
        rate_num = float(rate_num[0:3])
    
    if reviews:
        reviews = int(reviews.replace(",", ""))
        
    if sponsored:
        sponsored = True
    else: 
        sponsored = False
        
    if best_seller:
        sponsored = True
    else:
        sponsored = False
        
    if last_month_sales:
        last_month_sales = last_month_sales.split(" ")[0]
        
    # TODO: skip products without price
    if price:    
        price = float(price.replace("$", ""))
    
    # TODO: add referral link
    link = "https://www.amazon.com{link}"
    
    # Incress product counter
    current_index += 1
    
    # Incress counter of extracted products
    extracted_products += 1
    
    # End loop when extract al required products
    if extracted_products >= MAX_PRODUCTS: 
        break
    
    # TODO: end loop of there isn't more products in the page
    
    




print ("done")