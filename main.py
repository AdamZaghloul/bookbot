from stats import count_words
import sys

def main():
    args = sys.argv

    if len(args) != 2:
        print("Invalid input. Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    with open(args[1]) as f:
        file_contents = f.read()
    
    report(file_contents, args[1])
    #print(count_chars(file_contents))

def count_chars(file_contents):
    file_contents = file_contents.lower()
    counts = {}

    for char in file_contents:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

    output = []

    for count in counts:
        output.append({"letter": count, "count": counts[count]})   

    output.sort(reverse=True, key=sort_on)
    return output 

def report(file_contents, file_name):
    chars = count_chars(file_contents)

    print(f"--- Begin report of {file_name} ---")
    print("----------- Word Count ----------")
    print(f"{count_words(file_contents)} words found in the document")
    print("")
    print("----------- Character Count ----------")

    for char in chars:
        #print(char)
        print(f"{char['letter']}: {char['count']}")

    print("--- End report ---")

def sort_on(dict):
    return dict["count"]

main()