# from SEOmozAPISamples.python.mozscape import Mozscape
import requests


class apiMOZ:
    def __init__(self, url, cek):
        self.url = url
        self.cek = cek
        self.headers = {
            "x-rapidapi-key": "8473d4142amsh2564d5b0704b815p119312jsn3a37bb0ffcba",
	        "x-rapidapi-host": "domain-authority1.p.rapidapi.com"
        }
       

        # create a free account on https://moz.com/products/api/pricing
        # get your API key up to 2,500 rows per month
        # or upgrade to premium
        # self.moz_client = Mozscape(self.moz_api_client, self.moz_api_key)

    
    def get_da(self):
        # Parameter untuk API request
        querystring = {"domain": self.url}

        # Kirim request ke API
        # response = requests.post(self.cek, headers=self.headers, json=params)
        response = requests.get(self.cek, headers=self.headers, params=querystring)

        # Cek apakah responsnya sukses
        if response.status_code == 200:
            data = response.json()

            # Mengakses nilai domain_authority dari hasil API
        
            domain_power = data["result"]['domain_power']
            return domain_power
           
        else:
            return f"Request failed with status code {response.status_code}"


    
