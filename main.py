import requests
import json
import random

def get_quotes():
    response = requests.get("https://zenquotes.io/api/quotes")
    json_data = json.loads(response.text)
    return json_data

def get_random_quote():
    quotes = get_quotes()
    random_quote = random.choice(quotes)
    return random_quote

def print_quote(quote):
    print("Quote: " + quote['q'])
    print("Author: " + quote['a'])


def main():
    quote = get_random_quote()
    print_quote(quote)

if __name__ == "__main__":
    main()
