def count_words(file):
    total_word = 0
    for word in file.split():
        total_word += 1
    return total_word

def sort_on(dict):
    return dict["num"]

def count_character(file):
    all_character = {}
    for word in file.split():
        for char in word.lower():
            if char.isalpha():
                if char in all_character:
                    all_character[char] += 1
                else:
                    all_character[char] = 1

    char_list = [{'char': char, 'num': count} for char, count in all_character.items()]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def get_book_text(path):
    with open(path, 'r') as f:
        return f.read()
    
def get_report(file):
    text = get_book_text(file)
    total_word = count_words(text)
    total_character = count_character(text)
    
    print(f"--- Begin report of {file} ---")
    print(f"{total_word} found in the document\n")
    for elem in total_character:
        print(f"The {elem["char"]} character was found {elem["num"]} times")
    print(f"--- End report ---")


def main():
    file = "books/frankenstein.txt"
    get_report(file)

if __name__ == "__main__":
    main()