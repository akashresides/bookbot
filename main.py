def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    words = count_words(file_contents)
    sorted_list = sort_chars(count_chars(file_contents))
    print(f"--- Begin report of {f.name} ---")
    print(f"{words} words found in the document")
    print("\n")
    for s in sorted_list:
        print(f"The '{s['letter']}' character was found '{s['count']}' times")
    print("--- End report ---")

def sort_on(dict):
    return dict["count"]

def sort_chars(dict):
    list_dict = []
    for l in dict:
        if l.isalpha():
            list_dict.append({"letter":l,"count":dict[l]})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict

def count_chars(input):
    char_freq = {}
    for char in input.lower():
        if char in char_freq:
            char_freq[char]+=1
        else:
            char_freq[char]=1
    return char_freq

def count_words(input):
    return len(input.split())

main()
