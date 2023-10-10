# Desde esta linea importaremos el JSON de varias
# repositorios de peliculas

import requests
import json

print("¿Qué libro estas buscando?")
ISBN = input()

res = requests.get(f"https://www.goodreads.com/book/review_counts.json", params={"key": "gmaVsowZsITzZGWKQjQ3sQ", "isbns": "{ISBN}"})
print(res)
