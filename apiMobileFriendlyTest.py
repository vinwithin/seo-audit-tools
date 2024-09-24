import requests
import json


class apiMobileFriendlyTest:
    def __init__(self, url, mobile_api_key):
        self.url = url
        self.key = mobile_api_key

    def get_responsive_test(self):
        url = 'https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run?key=' + self.key
        data = {
            'url': self.url,
            'requestScreenshot': 'false'
        }

        response = requests.request("POST", url, data=data)
        response_json = response.json()

        # Debug output for response
        print(response_json)

        # Check for errors in response
        if 'error' in response_json:
            print(f"Error: {response_json['error']['message']}")
            return 0  # Return 0 in case of error

        # Check if 'mobileFriendliness' exists in the response
        if 'mobileFriendliness' in response_json:
            return 1 if response_json['mobileFriendliness'] == 'MOBILE_FRIENDLY' else 0
        else:
            print("Key 'mobileFriendliness' not found in the response.")
            return 0
