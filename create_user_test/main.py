# created by Syariffudin Dec 2016 #

# steps/ideas on making the test:
# 1. first check the data source (json server) is it available?
# 2. send a json post with random strings to create a user
# 3. get the json reply ensure that no error
# 4. compare stored json in json server with proposed value

import functions
from functions import json
from functions import sys
import test_script

# assume that this variable below is retrieved from properties file
# https://api.myjson.com/bins
url = functions.get_properties_key("json_service_url")

def main():
    print("Starting test...\n")

    # check services first
    print("Checking JSON Service provider at your network..")
    if test_script.is_service_online(url) is False:
        print("Exiting.. service is offline, is the url valid?")
        sys.exit()
    else:
        print("JSON service is accessible through the network...")
        print("proceeding..\n")

    # prepare data
    try:
        print("Generating random data...\n")
        random_data_dict = functions.generate_json_dictionary()
        data_dict_json = json.dumps(random_data_dict)
        
        # send json data post
        response = functions.send_json_post(url, data_dict_json)
        if response is None:
            print("Response: Error...")
            sys.exit()
            
        print("Response: Data is successfully stored..")
        # convert response to json
        response_json = json.loads(response)

        #get the uri of response
        generated_server_url = response_json['uri']

        # if fail to get the URL from the response, exit
        if generated_server_url is None:
            print("Error.. please ensure proper URL is generated before retrieving")
            sys.exit()

        # get the json data from the sent get url
        res_json_from_url = functions.get_json_from_url(generated_server_url)

        # testing part (assume that there are many test in here below
        print("TESTID_0001: Verify the created user:")
        test_results = test_script.verify_user_is_created(res_json_from_url, random_data_dict)
        if test_results is True:
            print("Tests for TESTID_0001 Verify the created user: PASSED")
        else:
            print("Tests for TESTID_0001 Verify the created user: FAILED")
        
    except Exception as e: #gotta catch them all (error)
            print("ERROR: ", e)

# exection
main()
