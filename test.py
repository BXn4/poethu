import poethu

poet = poethu.API(username="your_name", password="your_key")


def synonym_test():
    word: str = input("Please enter a word: ")

    synonyms = poet.get_szinonima(word, "asc", max=5)

    for i in range(len(synonyms)):
        synonym = synonyms[i]
        print(f"{i}: {synonym}")


def poems_category_test():
    category: str = input("Please enter a poem category: ")

    poems = poet.get_versek(category=category, order_by="id", order="desc", continue_from=1, max=2)

    for i in range(len(poems)):
        title = poet.get_title(poems)[i]
        poem = poet.get_text(poems)[i]
        author = poet.get_author(poems)[i]
        category = poet.get_category(poems)[i]
        favs = poet.get_favs(poems)[i]
        id = poet.get_id(poems)[i]
        url = poet.get_url(poems)[i]

        print("")
        print(f"Title: {title}")
        print(f"Poem text: \n{poem}")
        print(f"Author: {author}")
        print(f"Category: {category}")
        print(f"Favs: {favs}")
        print(f"ID: {id}")
        print(f"URL: {url}")


def search_poem_by_author_test():
    poem_author: str = input("Please enter a author: ")

    poem_from_author = poet.get_versek(author=poem_author, order_by="veletlen")

    title = poet.get_title(poem_from_author)
    poem = poet.get_text(poem_from_author)
    author = poet.get_author(poem_from_author)
    category = poet.get_category(poem_from_author)
    favs = poet.get_favs(poem_from_author)
    id = poet.get_id(poem_from_author)
    url = poet.get_url(poem_from_author)

    print("")
    print(f"Title: {title}")
    print(f"Poem text: \n{poem}")
    print(f"Author: {author}")
    print(f"Category: {category}")
    print(f"Favs: {favs}")
    print(f"ID: {id}")
    print(f"URL: {url}")


synonym_test()
poems_category_test()
search_poem_by_author_test()
