import json
from app.fast_fech import FAST_FECH
from requests.auth import HTTPBasicAuth
from colorama import Fore, Style, init
import pyfiglet

# Initialize colorama
init(autoreset=True)

def print_ascii_art():
    ascii_art = pyfiglet.figlet_format("FAST FETCH")
    print(Fore.GREEN + ascii_art)

def prompt_for_data():
    data = {}
    while True:
        key = input(Fore.GREEN + "\nEnter key (or press Enter to stop): ")
        if not key:
            break
        value = input(Fore.GREEN + f"Enter value for '{key}': ")

        # Try to parse the value as JSON; if it fails, keep it as a string
        try:
            parsed_value = json.loads(value)
        except json.JSONDecodeError:
            parsed_value = value

        data[key] = parsed_value
    return data

def prompt_for_auth():
    use_auth = input(Fore.GREEN + "\nDo you need basic auth? (y/n): ").strip().lower()
    if use_auth in ['y', 'yes']:
        username = input(Fore.GREEN + "Enter username: ")
        password = input(Fore.GREEN + "Enter password: ")
        return HTTPBasicAuth(username, password)
    elif use_auth in ['n', 'no']:
        print(Fore.RED + "No authentication will be used.")
    return None

def main():
    print_ascii_art()

    while True:
        url = input(Fore.GREEN + "\nEnter the URL (or type 'quit' to exit): ")
        if url.lower() == 'quit':
            print(Fore.RED + "\nExiting the program.")
            break

        request_type = input(Fore.GREEN + "\nWhat type of request do you want to make? (get/post/put/delete): ").strip().lower()
        
        data = None
        if request_type in ['post', 'put']:
            add_data = input(Fore.GREEN + "\nDo you want to add data? (y/n): ").strip().lower()
            if add_data in ['y', 'yes']:
                data = prompt_for_data()
            elif add_data in ['n', 'no']:
                print(Fore.RED + "No data will be sent.")

        auth = prompt_for_auth()
        
        fetch = FAST_FECH(url, data, auth)
        
        if request_type == 'get':
            fetch.get_request()
        elif request_type == 'post':
            fetch.post_request()
        elif request_type == 'put':
            fetch.put_request()
        elif request_type == 'delete':
            fetch.delete_request()
        else:
            print(Fore.RED + "Invalid request type!")

if __name__ == "__main__":
    main()

