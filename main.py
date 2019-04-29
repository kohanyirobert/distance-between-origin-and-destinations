import requests
import json
import sys
import os

API_KEY = os.env['API_KEY']

def get_distance(source, dest):
    url = f'https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={source}&destinations={dest}&key={API_KEY}'
    json = requests.get(url).json()

    rows = json['rows']

    # TODO: only happy case is covered.
    if len(rows) >= 1:
        row = rows[0]
        elements = row['elements']

        if len(elements) >= 1:
            element = elements[0]

            if 'distance' in element:
                return element['distance']['value'] / 1000

    return sys.maxsize

source = sys.stdin.readline().strip()
limit = int(sys.stdin.readline().strip())
for line in sys.stdin.readlines():
    dest = line.strip()
    distance = get_distance(source, dest)
    if distance < limit:
        print(dest)
