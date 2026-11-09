import requests

print("Testing our sandbox environment...")
response = requests.get("https://github.com")
print(f"Success! Connection Status: {response.status_code}")
