import requests
import json
import time

api_key = 'api_key=7bf7bfea8b95dd5b15d4563327eeccea'
base_url = 'https://apidata.mos.ru/v1/datasets/1903/'

def hypotenuse(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def load_data(filepath):
    json_file = open(filepath)
    return json.load(json_file)

def get_biggest_cafe():
    r = requests.get('https://apidata.mos.ru/v1/datasets/1903/rows?api_key=7bf7bfea8b95dd5b15d4563327eeccea&$orderby=SeatsCount+Desc&$top=1')
    return r.json()[0]['Cells']['Name']

def get_smallest_cafe():
    r = requests.get('https://apidata.mos.ru/v1/datasets/1903/rows?api_key=7bf7bfea8b95dd5b15d4563327eeccea&$orderby=SeatsCount+Asc&$top=1')
    return r.json()[0]['Cells']['Name']

def get_closest_cafe(data, lat, long):
    closest_gip = hypotenuse(lat, long, data[0]['geoData']['coordinates'][0], data[0]['geoData']['coordinates'][1])
    closest_name = data[0]['Name']
    for n in range(1, 12648):
        coord = data[n]['geoData']['coordinates']
        length = hypotenuse(lat, long, coord[0], coord[1])
        if length < closest_gip:
            closest_gip = length
            closest_name = data[n]['Name']
    return closest_name

if __name__ == '__main__':
    x1, y1 = list(map(float, input().split()))
    start = time.time()
    table = load_data('data.json')
    closest_cafe = get_closest_cafe(table, x1, y1)
    end = time.time()
    print(closest_cafe, 'time = ', end-start)
