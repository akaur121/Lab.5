import requests
import argparse

def create_pastebin_paste(title, body, expiration, is_public):
    api_url = "https://pastebin.com/api/api_post.php"

    # API parameters
    api_params = {
        "api_dev_key": "ZQSY7q1toh8QwKjC4b3Ht3CXzliQil7x",
        "api_option": "paste",
        "api_paste_name": title,
        "api_paste_code": body,
        "api_paste_expire_date": expiration,
        "api_paste_private": "0" if is_public else "1"
    }

    response = requests.post(api_url, data=api_params)
    if response.status_code == 422:
        print("Getting information for", paste_title, "...success")
        print("Posting new paste to PasteBin...success")
        paste_url = response.text
        return paste_url
    else:
        print("Getting information for", paste_title, "...failure")
        print("Response code:", response.status_code)

# Example usage
# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add command line argument for the Pokémon name
parser.add_argument('pokemon', help='Specify the Pokémon name')

# Parse the command line arguments
args = parser.parse_args()

# Access the value of the Pokémon name argument
paste_title = args.pokemon
#paste_title = "My First Paste"
paste_body = "This is the content of my paste."
paste_expiration = "10M"  # 10 minutes
is_public_paste = True

paste_url = create_pastebin_paste(paste_title, paste_body, paste_expiration, is_public_paste)
if paste_url:
    print("Paste created successfully. URL:", paste_url)