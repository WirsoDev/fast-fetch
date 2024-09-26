import requests
from requests.auth import HTTPBasicAuth
import json

class FAST_FECH:
    def __init__(self, url, data=None, auth=None):
        self.url = url
        self.data = data
        self.auth = auth

    def _print_formatted_json(self, json_data):
        formatted_json = json.dumps(json_data, indent=4, sort_keys=True)
        print(formatted_json)

    def get_request(self):
        try:
            response = requests.get(self.url, auth=self.auth)
            response.raise_for_status()
            print('Status Code:', response.status_code)
            try:
                self._print_formatted_json(response.json())
            except ValueError:
                print('Response Text:', response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def post_request(self):
        try:
            response = requests.post(self.url, json=self.data, auth=self.auth)
            response.raise_for_status()
            print('Status Code:', response.status_code)
            try:
                self._print_formatted_json(response.json())
            except ValueError:
                print('Response Text:', response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def put_request(self):
        try:
            response = requests.put(self.url, json=self.data, auth=self.auth)
            response.raise_for_status()
            print('Status Code:', response.status_code)
            try:
                self._print_formatted_json(response.json())
            except ValueError:
                print('Response Text:', response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def delete_request(self):
        try:
            response = requests.delete(self.url, auth=self.auth)
            response.raise_for_status()
            print('Status Code:', response.status_code)
            try:
                self._print_formatted_json(response.json())
            except ValueError:
                print('Response Text:', response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None




