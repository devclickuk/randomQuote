import requests
import json
import random

def get_quotes():
    response = requests.get("https://type.fit/api/quotes")
    json_data = json.loads(response.text)
    return json_data

def get_random_quote():
    quotes = get_quotes()
    random_quote = random.choice(quotes)
    return random_quote

def print_quote(quote):
    print("Quote: " + quote['text'])
    print("Author: " + quote['author'])


def main():
    quote = get_random_quote()
    print_quote(quote)

if __name__ == "__main__":
    main()
