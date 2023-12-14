import requests
import re

DANGEROUS_WORDS = ["bomb", "kill", "murder", "terror", "terrorist", "terrorists", "terrorism"]

def fetch(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        content_type = response.headers.get('Content-Type')

        if 'text/html' in content_type:
            content = response.text
            count = sum(len(re.findall(r'\b' + word + r'\b', content, re.IGNORECASE)) for word in DANGEROUS_WORDS)
            print(f"Number of dangerous words: {count}")
        else:
            print("Doesn't appear to be an HTML file with utf-8 encoding.")

        return response.content

    except requests.exceptions.RequestException as e:
        print(f"Error opening url: {url}")
        print(f"Exception: {e}")
        return None

def save(content, path):
    try:
        with open(path, 'wb') as f:
            f.write(content)
        print(f"Saving succeeded to: {path}")
    except:
        print("Saving failed.")

def main():
    url = input("Give me a valid URL to download?")
    content = fetch(url)
    if content is None:
        return
    path = input("Give me a valid path to save the contents?")
    save(content, path)

if __name__ == "__main__":
    main()
