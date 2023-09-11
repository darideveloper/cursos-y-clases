import os
from time import sleep
from dotenv import load_dotenv
from chrome_dev.chrome_dev import ChromDevWrapper

# read .env file
load_dotenv ()
MAX_PRODUCTS = int(os.getenv ("MAX_PRODUCTS"))
CHROME_PATH = os.getenv ("CHROME_PATH")

class Scraper (ChromDevWrapper):
    
    def __init__ (self, keyword:str, referral_link:str):
        """ Start scraper

        Args:
            keyword (str): product to search
            referral_link (str): platform referral link
        """
        
        # Scraper settings
        self.keyword = keyword
        self.referral_link = referral_link
        
        # Css self.selectors
        self.selectors = {
            "amazon": {
                'product': '[data-asin][data-uuid]',
                'image': 'img',
                'title': 'h2',
                'rate_num': 'span[aria-label]:nth-child(1)',
                'reviews': 'span[aria-label]:nth-child(2)',
                'sponsored': '[aria-label~="Sponsored"]',
                'best_seller': '.a-row.a-badge-region',
                'price': 'a.a-size-base .a-offscreen',
                'sales': '.a-row.a-size-small > span:nth-child(2)',
                'link': 'a',
            },
            "aliexpress": {
                'product': '#card-list > a',
                'image': 'img',
                'title': 'h1',
                'rate_num': '[class*="evaluation"]',
                'reviews': '[class*="evaluation"]',
                'sponsored': 'img + span',
                'best_seller': 'img[width="44.53125"]',
                'price': '[class*="price-sale"]',
                'sales': '[class*="trade-"]',
                'link': '',
            },
        }
        
        # Open chrome
        super().__init__ (chrome_path=CHROME_PATH, start_killing=False)
        
    def __get_search_link__ (self, product:str) -> str:
        # TODO: docs
        
        # REFACTOR
        if self.store == "amazon":
            return f"https://www.amazon.com/s?k={product}&s=review-rank"
        elif self.store == "aliexpress":
            product_clean = product.replace (" ", "-")
            return f"https://www.aliexpress.com/w/wholesale-{product_clean}.html?g=y&trafficChannel=main&isMall=y"
        else:
            return ""
        
    def __clean_text__ (self, text:str, chars:list) -> str:
        
        for char in chars:
            text = text.replace (char, "")
            
        return text
    
    def __get_is_sponsored__ (self, text:str) -> str:
        
        if self.store == "amazon":
            return text != ""
        elif self.store == "aliexpress":
            return text.lower() == "ad"
        else:
            return ""
        
    def __get_sales_num__ (self, sales:str) -> int:
        
        if self.store == "amazon":
            return int(sales.split(" ")[0])
        elif self.store == "aliexpress":
            return int(self.__clean_text__(sales, [",", " ", "+", "sold"]))
        else:
            return 0
        
    def get_results (self, store:str, start_product:int=1):
        
        # Save store as class variable
        self.store = store.lower ()
        
        product = self.keyword.lower ()
        
        # Get selectors and validate them
        selectors = self.selectors.get (self.store, {})
        if not selectors:
            print (f"({self.store}) self.store not supported")
            return []
        
        print (f"({self.store}) Searching products...")

        # Open chrome and load results page
        search_link = self.__get_search_link__ (product)
        self.set_page (search_link)
        self.set_zoom (0.2)
        self.go_down ()

        # get the results in the page
        results_num = self.count_elems (selectors['product'])

        # Validate if there are results
        if results_num == 0:
            print (f"({self.store}) No results found")
            return []

        current_index = start_product
        extracted_products = 0

        print (f"({self.store}) Extracting data...")

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
            selector_sales = f'{selector_product} {selectors["sales"]}'
            selector_link = f'{selector_product} {selectors["link"]}'
            
            # Incress product counter
            current_index += 1
            
            # Validate if there are not more products in the page
            if current_index - start_product > results_num:
                print (f"({self.store}) No more products")
                break
            
            # Skip products without price
            price = self.get_text (selector_price)
            if not price:
                continue
            
            # Skip sponsored products
            sponsored = self.get_text (selector_sponsored)
            sponsored = self.__get_is_sponsored__ (sponsored)
            if sponsored:
                continue
            
            # Extract text from selectors
            image = self.get_attrib (selector_image, "src")    
            title = self.get_text (selector_title)
            rate_num = self.get_text (selector_rate_num)
            reviews = self.get_attrib (selector_reviews, "aria-label")
            best_seller = self.get_text (selector_best_seller)
            sales = self.get_text (selector_sales)
            link = self.get_attrib (selector_link, "href")
                
            # Clean data 
            price = self.__clean_text__ (price, ["$", "US "])
            price = float(price)
            
            if not image.startswith ("https"):
                image = "https:" + image
            
            if rate_num:
                rate_num = float(rate_num[0:3])
            
            if reviews:
                reviews = self.__clean_text__ (reviews, [",", " ", "+"])
                reviews = float(reviews)
                
            if best_seller:
                best_seller = True
            else:
                best_seller = False
                
            if sales:
                # TODO: clean sale (check __get_sales_num__)
                sales = self.__get_sales_num__ (sales)
                            
            # TODO: add referral link
            
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
                "sales": sales,
                "link": link,
            })
            
            # End loop when extract al required products
            if extracted_products >= MAX_PRODUCTS: 
                break
                
        print (f"({self.store}) {extracted_products} products extracted")
        
        # TODO: return scraped data
        
scraper = Scraper ("ssd 1 tb", "")
scraper.get_results ("amazon", 6)
scraper.get_results ("aliexpress", 1)

