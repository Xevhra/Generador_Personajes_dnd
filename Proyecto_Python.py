# Desde esta linea importaremos el JSON de varias
# repositorios de peliculas

import requests
import json
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "gmaVsowZsITzZGWKQjQ3sQ", "isbns": "0743269268"})
print(res.text)
data=res.json()
print(data)