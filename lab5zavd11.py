words = input("Введіть ваше речення: \n")
words = words.replace(',', '').replace('.', '').replace('...', '').replace(':', '').replace('!', '').replace('?','').replace(';', '').replace('-', '').replace(')', '').replace('(', '').replace('"', '')
words = words.split()
letter_counts = list(map(lambda x: len(x), words))
letter_counts.sort()
c = {i: letter_counts.count(i) for i in letter_counts}
print()
print(c)
input()