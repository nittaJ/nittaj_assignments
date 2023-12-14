import json
import os

def load_dictionary():
    if os.path.exists('dictionary.json'):
        try:
            with open('dictionary.json', 'r') as f:
                return json.load(f)
        except:
            print("Error loading dictionary")
    return {"hello": "moi"}

def save_dictionary(dictionary):
    try:
        with open('dictionary.json', 'w') as f:
            json.dump(dictionary, f)
    except:
        print("Error saving dictionary")

def main():
    dictionary = load_dictionary()
    while True:
        word = input("Please give definition or enter to cancel")
        if word == "":
            break
        definition = dictionary.get(word)
        if definition is None:
            print("Word not found. Please give definition or enter to cancel")
            definition = input("Give a word ")
            dictionary[word] = definition
        else:
            print(f"{word}: {definition}")
    save_dictionary(dictionary)

if __name__ == "__main__":
    main()
