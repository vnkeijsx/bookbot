chars = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z",

    "!","@","#","$","%","^","&","*","(",")",
    "-","_","=","+",
    "[","]","{","}",
    "\\","|",
    ";",":",
    "'","\"",
    ",",".",
    "<",">",
    "/","?",
    "`","~"
]


def get_book_txt(file_path):
    with open(file_path) as book:
        file_contents = book.read()
        count = len(file_contents.split())
        print(f"Found {count} total words")
        return f"Found {count} total words"
    
def char_count(text):
    with open(text) as words:
        contents = words.read().lower()
        dict = {}
        for word in contents:
            for char in chars:   
                if word == char:
                    dict[word] = dict.get(word, 0) + 1
        return dict    
    
def sort_on(items):
    return items["num"]

def sorted_list(dict):
    new_dict = []
    for entry in dict:
        new_dict.append({
            "char": entry,
            "num": dict[entry]
        })
    new_dict.sort(reverse=True, key=sort_on)
    for count in new_dict:
        print(f"{count["char"]}: {count["num"]}")


            
    