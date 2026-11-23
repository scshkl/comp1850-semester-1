"""
Task 2: Fetch and display a post Using GET Request
"""

import httpx

url = "https://httpbin.io/json"

response = httpx.get(url)   # httpx object, get() method, returns a response object

# print(response.json())      # response object, json() method
print(response.status_code)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")