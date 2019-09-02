import csv
import json
import time
import requests
import xmltodict
from geopy.geocoders import Nominatim
from pprint import pprint
from tqdm import tqdm

final_response = list()


def find_lat_long(address=None):
    try:
        geolocator = Nominatim(user_agent="my-application")
        location = geolocator.geocode(address)
        detail_address = location.address
        latitude, longitude = location.latitude, location.longitude
        #print(latitude, longitude)
    except Exception as e:
        #print(e)
        detail_address, latitude, longitude = "", "", ""
        return detail_address, latitude, longitude
    else:
        return detail_address, latitude, longitude

def retry(func,*args,sleep_time=1,retry=5,**kwargs):
    retry_count = 0
    while True:
        time.sleep(sleep_time)
        indv_result = func(json_dict, url=url)
        if indv_result['address']:
            break
        else:
            retry_count +=1
            #print('trying........ {}'.format(retry_count))
            if retry_count == retry:
                break
    return indv_result

def parse_dict(input_dict=None, url=None):
    indv_dict = dict()
    if input_dict is None:
        return indv_dict
    else:
        #print("\n#Ref:", input_dict['ref'])
        #print("## input_dict ##", input_dict)
        for element in input_dict.keys():
            if element == "ref":
                indv_dict["ref"] = input_dict[element].replace(',', '-')
            elif "ref" not in indv_dict.keys():
                indv_dict["ref"] = ""

            if element == "price":
                indv_dict["price"] = input_dict[element]
            elif "price" not in indv_dict.keys():
                indv_dict["price"] = ""

            if element == "price_freq":
                indv_dict["price_freq"] = input_dict[element]
            elif "price_freq" not in indv_dict.keys():
                indv_dict["price_freq"] = ""

            if element == "beds":
                indv_dict["beds"] = input_dict[element]
            elif "beds" not in input_dict.keys():
                indv_dict["beds"] = ""
            if element == "baths":
                indv_dict["baths"] = input_dict[element]
            elif "baths" not in indv_dict.keys():
                indv_dict["baths"] = ""
            if element == "pool":
                indv_dict["pools"] = input_dict[element]
            elif "pool" not in input_dict.keys():
                indv_dict["pools"] = ""

            if element == "surface_area":
                if isinstance(input_dict[element], dict):
                    # if 'surface_area' in input_dict[element].keys():
                    if "built" in input_dict[element].keys():
                        indv_dict["built"] = input_dict[element]["built"]
                    else:
                        indv_dict["built"] = ""
                    if "plot" in input_dict[element].keys():
                        indv_dict["plot"] = input_dict[element]["plot"]
                    else:
                        indv_dict["plot"] = ""
                else:
                    indv_dict["built"] = ""
                    indv_dict["plot"] = ""
            elif "surface_area" not in input_dict.keys():
                indv_dict["built"] = ""
                indv_dict["plot"] = ""

            if element == "desc":
                if isinstance(input_dict[element], dict) and "en" in input_dict[element]:
                    indv_dict["desc"] = input_dict[element]["en"].replace(
                        ',', ';').replace('\n', '')
                else:
                    indv_dict["desc"] = ""
            elif "desc" not in indv_dict.keys():
                indv_dict["desc"] = ""

            if element == "images":
                if input_dict[element] and "image" in input_dict[element]:
                    image_list = list()
                    if isinstance(input_dict[element]["image"], list):
                        for img_element in input_dict[element]["image"]:
                            image_info = {
                                'image_url': ''.join(img_element["url"].split())}
                            image_list.append(image_info["image_url"])
                        indv_dict["images"] = image_list
                    elif isinstance(input_dict[element]["image"], dict):
                        img_element = input_dict[element]["image"]
                        image_info = {
                            'image_url': ''.join(img_element["url"].split())}
                        image_list.append(image_info["image_url"])
                        indv_dict["images"] = image_list

            elif "images" not in indv_dict.keys():
                indv_dict["images"] = list()

            if element == "type":
                indv_dict['type'] = input_dict[element]

            elif "type" not in indv_dict.keys():
                indv_dict["type"] = ""

            if "address" not in indv_dict:
                town = input_dict["town"]
                province = input_dict["province"]

                if len(town) or len(province):
                    if len(town):
                        formatted_addr = '{}'.format(town)
                    elif len(province):
                        formatted_addr = '{}'.format(province)
                    else:
                        formatted_addr = '{}, {}'.format(town, province)
                    # print(town, province)
                    #print("formatted_address", formatted_addr)
                    address, lat, lng = find_lat_long(formatted_addr)
                    #print("Address, Latitude and Longitude")
                    #print(address, lat, lng)
                    indv_dict["address"] = address.replace(',', ' ')
                    indv_dict["latitude"] = lat
                    indv_dict["longitude"] = lng
                else:
                    indv_dict["address"] = ""
                    indv_dict["latitude"] = ""
                    indv_dict["longitude"] = ""

            if element == 'features':
                if isinstance(input_dict[element], dict):
                    keys = input_dict[element].keys()
                    if 'feature' in keys:
                        indv_dict['features'] = input_dict[element]['feature']
                    else:
                        indv_dict['features'] = []
                else:
                    indv_dict['features'] = []

            elif 'features' not in indv_dict:
                indv_dict['features'] = []

        return indv_dict


if __name__ == '__main__':
    expected_key_set = ['ref', 'price', 'price_freq', 'type', 'address', 'lat', 'long', 'beds', 'baths', 'pools',
                        'built', 'plot', 'desc', 'features', 'images']
    fp = open('anacasa.csv', 'w')
    w = csv.DictWriter(fp, expected_key_set)
    w.writeheader()
    url = "https://witei.com/pro/interconnection/xml/7560b56c0c4f4042/"

    site = requests.get(url)
    value = site.text
    # accessing the desired list
    dict_items = xmltodict.parse(value)['root']['property']
    #print(len(dict_items))
    with tqdm(total=len(dict_items)) as pbar:
        for i, dict_item in tqdm(enumerate(dict_items)):
            json_str = json.dumps(dict_item)
            json_dict = json.loads(json_str)
            if i%500 == 0 and i != 0:
                #print('resting........ 10 sec')
                time.sleep(10)
            indv_result = retry(parse_dict,json_dict,sleep_time=3,retry=4,url=url)
            w.writerow({'ref': indv_result['ref'], 'price': indv_result['price'],
                        'price_freq': indv_result['price_freq'], 'type': indv_result['type'],
                        'address': indv_result['address'], 'lat': indv_result['latitude'],
                        'long': indv_result['longitude'], 'beds': indv_result['beds'], 'baths': indv_result['baths'],
                        'pools': indv_result['pools'], 'built': indv_result['built'], 'plot': indv_result['plot'],
                        'desc': indv_result['desc'],
                        'features': ';'.join(indv_result['features']),
                        'images': ';'.join(indv_result['images'])
                        })
            pbar.update(1)
        #print('####################### completed successfully ###############################')
        fp.close()
