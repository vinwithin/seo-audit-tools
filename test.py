import requests

url = "https://domain-authority1.p.rapidapi.com/seo-tools/get-domain-info"

querystring = {"domain":"learnwithhasan.com"}

headers = {
	"x-rapidapi-key": "8473d4142amsh2564d5b0704b815p119312jsn3a37bb0ffcba",
	"x-rapidapi-host": "domain-authority1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()
print(data["result"]['domain_power'])