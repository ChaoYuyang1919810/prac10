"""
CP1404/CP5632 Practical
Started 5/4/2015
"""

import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

print("Welcome to the Wikipedia query tool by Chao Yuyang 2025!")

while True:
    query = input("\nEnter page title: ").strip()
    if not query:
        print("Thank you.")
        break

    try:
        # Fetch the page with auto_suggest enabled to find best match
        page = wikipedia.page(query, auto_suggest=True)
        print(f"\n{page.title}")
        print(page.summary)
        print(page.url)
    except DisambiguationError as e:
        print(f"\nWe need a more specific title. Try one of the following, or a new search:")
        # Display up to 10 options to avoid overwhelming the user
        print(", ".join(e.options[:10]))
    except PageError:
        print(f"\nPage id \"{query}\" does not match any pages. Try another id!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")