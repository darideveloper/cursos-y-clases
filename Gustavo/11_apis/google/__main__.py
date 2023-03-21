

import pandas as pd
from tqdm import tqdm
import api
import data

# Conection to API
service = api.connect()

results = []

# Get data from each url
urls = data.get_urls()
for url in tqdm(urls):

    url_data = api.get_data_url(url, service)

    # todo: process data
    url_cliks = 1231356
    url_impressions = 763
    url_position = 51236
    row = [url_cliks, url_impressions, url_position]
    results.append(row)

print(results)

# for row in results['page']:
#     results['clicks'].append(row(int(['clicks'])))
#     results['impressions'].append(row['impressions'])
#     results['ctr'].append(row['ctr'])
#     results['position'].append(row['position'])
#     print(results)

# print(results)


# df.to_csv('url_results.csv', encoding='utf-8')
