def load_book(path):
    with open(path) as f:
        return f.read()


def character_appearances(book):
    char_counts = {}
    for c in book.lower():
        if c.isalpha():
            if c not in char_counts:
                char_counts[c] = 1
            else:
                char_counts[c] += 1
        else:
            continue

    return char_counts


def char_counts(dict):
    dicts = []
    for char in dict:
        dicts.append({"char": char, "count": dict[char]})
    return dicts


def words_in_book(book):
    return len(book.split())


def sort_on(dict):
    return dict["count"]


def report(path, book):
    print(f"--- Begin report of {path} ---")
    print(f"{words_in_book(book)} words found in the document\n")

    apps = character_appearances(book)
    counts = char_counts(apps)

    counts.sort(reverse=True, key=sort_on)
    for item in counts:
        print(f"The '{item["char"]}' character was found {item["count"]} times")

    print("--- End report ---")


def main():
    path = "books/frankenstein.txt"
    book = load_book(path)
    report(path, book)


main()
