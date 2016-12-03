# created by Syariffudin Dec 2016 #

import string
import random
import urllib.request
import json
import sys

# assume that this function read from property file
def get_properties_key(key_prop):
    if key_prop is "json_service_url":
        return "https://api.myjson.com/bins"

# this one is to generate random strings, make the test more valid
def generate_random_string(size=6, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

# assume you want manual hard coded input, dont want to use random generator
def generate_json_dictionary(uname, password, email, ui_role, label):
    json_d = {
        'label': label,
        'username': uname,
        'ui_password': password,
        'email': email,
        'ui_role': ui_role
        }
    return json_d

# generate json dictionary
def generate_json_dictionary():
    list_of_role = ['admin','user1','user2','user3','user4']
    list_of_label = ['label1','label2','label3','label4','label5']

    label = list_of_label[random.randint(0,len(list_of_label)-1)]  
    username = generate_random_string()
    ui_password = generate_random_string()
    email = generate_random_string() + "@" + generate_random_string() + ".com"
    ui_role = list_of_role[random.randint(0,len(list_of_role)-1)]
    
    json_d = {
        'label': label,
        'username': username,
        'ui_password': ui_password,
        'email': email,
        'ui_role': ui_role
        }
    
    for key, value in json_d.items():
        print(key + ": " + value)

    return json_d

# this is where the data will be stored to the json server
def send_json_post(post_url, json_data):
    headers = {}
    headers['Content-Type'] = 'application/json'
    if json_data and post_url is not None:
        try:
            print("\nPOST sent..")
            post_data = json_data.encode('utf-8')
            req = urllib.request.Request(post_url, post_data, headers)
            print("\nGetting responses..")
            res = urllib.request.urlopen(req)
            
            # check if not getting any 201 response code from server
            if res.code != 201:
                print("fail to create user..")
                print("exiting...")
                sys.exit()
                
            response_decode = res.read().decode('utf-8')
            return response_decode
        except Exception as e: #gotta catch them all (error)
            print("ERROR: ", e)
    else:
        print("json/url cannot be null")
        sys.exit()

def get_print(string1, string2):
    print(string1 + ": " + string2)

# pass the url and try to retrieve the data
def get_json_from_url(url):
    print("\nGetting data from: " + url)
    print("Retrieving...\n")

    try:
        url_res = urllib.request.urlopen(url)
        url_decoded = url_res.read().decode('utf-8')
        result = json.loads(url_decoded)
    
    except Exception as e: #gotta catch them all (error)
        print("ERROR: ", e)
        sys.exit()
    return result
