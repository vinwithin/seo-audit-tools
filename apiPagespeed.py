import requests
import json


class apiPagespeed:
    def __init__(self, url, pagespeed_api_key):
        self.url = url
        # use your gmail to get a key from https://developers.google.com/speed/docs/insights/v5/get-started
        # there are limitations have to take into consideration
        self.key = pagespeed_api_key  # The PageSpeed API will slow down the script

    def get_speed(self):
        url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=" + self.url + "&key=" + self.key

        response = requests.get(url)

        # r = response.json()['lighthouseResult']['audits']['speed-index']['displayValue']
        # r = r.replace('\xa0s', '')  # remove the space + s. I only want the number
        # return r
        if response.status_code == 200:
            data = response.json()
                    
                    # Extract the speed index value from the response
            r = data['lighthouseResult']['audits']['speed-index']['displayValue']
                    
                    # Clean up the speed index value (remove any non-numeric characters)
            r = r.replace('\xa0s', '')  # Remove the space + "s" (seconds)

            return r
        else:
            return f"Error: Received status code {response.status_code} from API."

