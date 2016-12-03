# created by Syariffudin Dec 2016 #

import urllib.request

def verify_user_is_created(respond_json, original_data):
    # check data
    count = 0
    failed_at = None
    print("comparing server's updated value and original proposed value..\n")
    for key, value in respond_json.items():
        print("checking value for " + key + " at stored json")
        if value == original_data[key]:
            print(key + " is MATCHED with original proposed value\n")
            count+=1
        else:
            print(key + " is NOT MATCHED with original proposed value\n")
            print("stoping tests...")
            failed_at = key

    if count == 5:
        return True
    else:
        print("Test fail at: " + key + " property\n")
        return False

def is_service_online(url):
    response = urllib.request.urlopen(url).getcode()
    if response == 200:
        return True
    else:
        return False
