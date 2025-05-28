import requests
import pandas as pd

# Make the request to Gazamaps API
url = "https://gazamaps.com/api/v1/displacement"
response = requests.get(url)

# Check response status
if response.status_code == 200:
    data = response.json()

    # Check if data is a list of records
    if isinstance(data, list):
        displacement = pd.DataFrame(data)

        # Save all the API data to a CSV file
        displacement.to_csv("data/displacement.csv", index=False)
        print("Data successfully saved to data/displacement.csv")
    else:
        print("Unexpected data format:", type(data))
else:
    print(f"Request failed: {response.status_code}")
    print(response.text)