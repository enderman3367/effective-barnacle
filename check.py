import requests

url = "https://api.elevenlabs.io/v1/voices"

headers = {
  "Accept": "application/json",
  "xi-api-key": "bb73cb3343b6c5408e2c9bb1cdc881bb"
}

response = requests.get(url, headers=headers)

print(response.text)
