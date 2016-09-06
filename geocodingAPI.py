import json
import csv
import requests

with open('list.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        try:
            print(row[0])
            url = 'https://maps.googleapis.com/maps/api/geocode/json'
            params = {'sensor': 'false', 'address': row[0]}
            r = requests.get(url, params=params)
            results = r.json()['results']
            location = results[0]['geometry']['location']
            print(location['lat'], location['lng'])
            with open(r'names.csv','a') as csvfile:
                fieldnames = ['lat', 'lng']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'lat': location['lat'], 'lng': location['lng']})
        except:
            print("Error")
