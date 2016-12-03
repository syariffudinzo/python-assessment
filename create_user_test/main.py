# 1. first check the data source is it available?
# 2. send a json post with random strings to create a user
# 3. get the json reply ensure that no error and user is created

import string
import random
import urllib.request
import json
import sys

label = ""
username = ""
ui_roles = ""
ui_password = ""
email = ""
url = "https://api.myjson.com/bins"

def generate_json_dictionary(uname, password, email, ui_role):
    json_d = {
        'username': uname,
        'ui_password': password,
        'email': email,
        'ui_role': ui_role
        }
    return json.dumps(json_d)

def generate_random_string(size=6, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def send_json_post(post_url, json_data):
    headers = {}
    headers['Content-Type'] = 'application/json'
    if json_data and post_url is not None:
        try:
            print("\nPOST sent..")
            post_data = json_data.encode('utf-8')
            req = urllib.request.Request(post_url, post_data, headers)
            print("\ngetting responses..")
            res = urllib.request.urlopen(req)
            
            # check if not getting any 201 response code from server
            if res.code != 201:
                print("fail to create user..")
                print("exiting...")
                sys.exit()
                
            response_decode = res.read().decode('utf-8')
            return response_decode
        except Exception as e: #gotta catch them all (error)
            logging.error(traceback.format_exc())
    else:
        print("json/url cannot be null")
        return None

def get_print(string1, string2):
    print(string1 + ": " + string2)

# prepare data
print("Generating random data...\n")
label = generate_random_string();
username = generate_random_string();
ui_roles = "admin"
ui_password = generate_random_string();
email = generate_random_string() + "@" + generate_random_string() + ".com"

#print generation data
get_print("label", label)
get_print("username", username)
get_print("ui_roles", ui_roles)
get_print("ui_password", ui_password)
get_print("email", email)

json_data = generate_json_dictionary(username, ui_password, email, ui_roles)
resonse = send_json_post(url, json_data)
print("User is successfully created.. ")
print(resonse)
