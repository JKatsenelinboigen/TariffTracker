import requests
import json

def fetch_tariff_data():
    url = "https://hts.usitc.gov/reststop/exportList?from=0&to=20000&format=JSON&styles=true"
    # url = "https://hts.usitc.gov/api/search?query=copper"
    response = requests.get(url)
    
    if response.status_code == 200:
        # print(response.content)
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

def save_data_to_file(data, filename="tariff_data.json"):
    with open(filename, 'w') as file:
        json.dump(data, file)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    data = fetch_tariff_data()
    if data:
        save_data_to_file(data)
    