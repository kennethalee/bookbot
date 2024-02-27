def main():
    book_path = "books/frankenstein.txt"
    contents = get_book(book_path)
    num_words = get_words(contents)
    characters = get_letters(contents)
    report = dict_to_list(characters)

    print(f"--- Begin report of book/frankenstein.txt ---")
    print(f"{num_words} words found in document\n")   
    for item in report:
            print(f"The {item["name"]} character was found {item["num"]} times") 
    print("\n--- End of report ---")
    
def get_book(path):
    with open(path) as f:
        return f.read()

def get_words(contents):
    words = contents.split()
    return len(words)

def get_letters(contents):
    characters = {}
    for letter in contents:
        lowered_letters = letter.lower()
        if lowered_letters.isalpha():
            if lowered_letters in characters:
                characters[lowered_letters] += 1
            else:
                characters[lowered_letters] = 1    
    return characters

def dict_to_list(characters):
    list_characters =[
        {"name": name, "num": count} for name, count in characters.items()
    ]
    list_characters.sort(reverse=True, key=lambda x: x["num"])
    return list_characters

main()