import os


def get_words(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words
def get_chars(filename):
    with open(filename, encoding="utf8") as file:
        chars = file.read()
    chars = chars.replace("\n", " ")
    chars = chars.lower()
    return chars

def get_chars_nospace(filename):
    with open(filename, encoding="utf8") as file:
        chars1 = file.read()
    chars1 = chars1.replace("\n", " ")
    chars1 = chars1.lower()
    chars1 = chars1.replace(" ", "")
    return chars1

def get_words_dict(words):
    words_dict = dict()
 
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict
 
 
def main(): 
    filename = input("Введіть шлях до файлу: ")
    if not os.path.exists(filename):
        print("Вказаного файлу не існує")
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words)
        characters = get_chars(filename)
        characters1 = get_chars_nospace(filename) 
        print("Кі-сть символів без пробілів: %d" % len(characters1))
        print("Кі-сть символів: %d" % len(characters))
        print("Кі-сть слів: %d" % len(words))
        print("Кі-сть унікальних слів: %d" % len(words_dict))
    
if __name__ == "__main__":
        main()
input()