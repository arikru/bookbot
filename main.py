def main():
    book_path = "books/frankenstein.txt" 
    text = get_text(book_path)
    word_counts = count_words(text)
    letter_counts = count_letters(text)
    listed_counts = convert_dict(letter_counts)
    listed_counts.sort(reverse = True, key = sort_on)
    
    print("")
    print("--- Begin report of frankenstein.txt ---")
    print(f"{word_counts} words found in the document")
    for char in listed_counts:
        print(f"The letter {char['char']} was counted {char['count']} times.") 
    print("--- End report ---")

def get_text(path): 
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_words(corpus):
    return len(corpus.split())


def count_letters(text):
    letter_dict = {}
    text = list(text.lower())
    for char in text:
        if char not in letter_dict:
            letter_dict[char] = 1
        else:
            letter_dict[char] += 1
    return letter_dict

def sort_on(dict):
    return dict["count"]

def convert_dict(dict):
    lst = []

    for char, count in dict.items():
        if char.isalpha():
            lst.append({"char": char, "count": count})
    return lst

main()
