# Desde esta linea importaremos el JSON de varias
# repositorios de peliculas

import requests

res = requests.get(f"https://www.goodreads.com/book/review_counts.json")
print(res)
