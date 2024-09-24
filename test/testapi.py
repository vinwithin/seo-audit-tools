import requests


class apiMOZ:
    def __init__(self, domain):
        self.domain = domain
        self.url = "https://moz-da-pa1.p.rapidapi.com/v1/getDaPa"
        self.headers = {
            "x-rapidapi-key": "d2007360f3mshb6455ce0da53b1bp1d4a1fjsn85182304884d",
            "x-rapidapi-host": "moz-da-pa1.p.rapidapi.com",
            "Content-Type": "application/json"
        }

    def get_da(self):
        # Parameter untuk API request
        # payload = {"domain": self.domain}

        # Kirim request ke API
        response = requests.post(self.url, headers=self.headers, json=self.domain)

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



# Contoh penggunaan
api_moz = apiMOZ({ "q": "example.com" })
domain_power = api_moz.get_da()
print(f"Domain Power: {domain_power}")
