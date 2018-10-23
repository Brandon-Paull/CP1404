import wikipedia

search_phrase = input("Enter Query: ")
while search_phrase != "".strip():
    print()
    try:
        page = wikipedia.page(search_phrase)
        print(page.title)
        print(page.summary)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as error:
        print(error)
    print()
    search_phrase = input("Enter Query: ")
