# from SEOmozAPISamples.python.mozscape import Mozscape
import requests


class apiMOZ:
    def __init__(self, url, cek):
        self.url = url
        self.cek = cek
        self.headers = {
            'x-rapidapi-key': "97efac4d4bmshc360867e4cc668ap13df32jsn3a2969e89a40",
            'x-rapidapi-host': "moz-da-pa1.p.rapidapi.com",
            'Content-Type': "application/json"
        }
       

        # create a free account on https://moz.com/products/api/pricing
        # get your API key up to 2,500 rows per month
        # or upgrade to premium
        # self.moz_client = Mozscape(self.moz_api_client, self.moz_api_key)

    
    def get_da(self):
        # Parameter untuk API request
        params = {"q": self.url}

        # Kirim request ke API
        response = requests.post(self.cek, headers=self.headers, json=params)

        # Cek apakah responsnya sukses
        if response.status_code == 200:
            data = response.json()

            # Mengakses nilai domain_authority dari hasil API
            if isinstance(data, list) and 'domain_authority' in data[0]:
                domain_power = data[0]['domain_authority']
                return domain_power
            else:
                return "Invalid response format"
        else:
            return f"Request failed with status code {response.status_code}"


    
