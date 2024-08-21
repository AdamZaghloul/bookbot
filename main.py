def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    report(file_contents)
    #print(count_chars(file_contents))

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

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

def report(file_contents):
    chars = count_chars(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")
    print("")

    for char in chars:
        #print(char)
        print(f"The '{char['letter']}' character was found {char['count']} times")

    print("--- End report ---")

def sort_on(dict):
    return dict["count"]

main()