def main():
    path = "books/frankenstein.txt" 
    file_contents = get_book(path)
    words_count = count_words(file_contents)
    map = count_letter(file_contents)
    sorted_map = sorted_letter_list(map)

    print(f"--- Begin Report of {path} ---")
    print(f"{words_count} words found in the document")
    print()

    for item in sorted_map:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print(f"--- End Report ---")


def get_book(path):
    with open(path) as f:
        return f.read()

def count_words(text): 
    return len(text.split())

def count_letter(text):
    map = {}

    for c in text:
        c = c.lower()
        if c in map:
            map[c] += 1
        else:
            map[c] = 1
    return map

def sort_on(d):
    return d["num"]

def sorted_letter_list(map):
    list = []
    for c in map:
        list.append({"char": c, "num": map[c]})
    list.sort(reverse=True, key=sort_on)
    return list







main()
