import requests
import pandas as pd

def fetch_displacement_data(save_path, api_url="https://gazamaps.com/api/v1/displacement"):
    """Fetch displacement data from Gaza Maps API and save it to a CSV file."""
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        if isinstance(data, list):
            displacement = pd.DataFrame(data)
            displacement.to_csv(save_path, index=False)
            print(f"Data successfully saved to {save_path}")
            return displacement
        else:
            print(f"Unexpected data format: {type(data)}")
            return None
    else:
        print(f"Request failed: {response.status_code}")
        print(response.text)
        return None
