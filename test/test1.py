import requests
import json


class apiPagespeed:
    def __init__(self, url, pagespeed_api_key):
        self.url = url
        # Use your Gmail to get a key from https://developers.google.com/speed/docs/insights/v5/get-started
        # There are limitations that have to be taken into consideration
        self.key = pagespeed_api_key  # The PageSpeed API will slow down the script

    def get_speed(self):
        # Build the API request URL
        url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={self.url}&key={self.key}"

        try:
            # Send the request to the PageSpeed API
            response = requests.get(url)

            # Ensure the response is successful (status code 200)
            if response.status_code == 200:
                data = response.json()
                
                # Extract the speed index value from the response
                speed_index = data['lighthouseResult']['audits']['speed-index']['displayValue']
                
                # Clean up the speed index value (remove any non-numeric characters)
                speed_index = speed_index.replace('\xa0s', '')  # Remove the space + "s" (seconds)

                return speed_index
            else:
                return f"Error: Received status code {response.status_code} from API."

        except KeyError:
            return "Error: Unexpected response structure. Check if the API response format has changed."
        except Exception as e:
            return f"An error occurred: {e}"


# Contoh penggunaan
pagespeed_api_key = "AIzaSyBTVMHCioVHlbspDabq-4NYcgVMwwGH2sk"  # Replace with your actual API key
api_pagespeed = apiPagespeed("https://google.com", pagespeed_api_key)

speed = api_pagespeed.get_speed()
print(f"Speed Index: {speed}")
