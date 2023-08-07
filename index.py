fh = open("list.txt","r")
file_words = fh.read().lower()
fh.close()

search_words = ["PyThon", "C", "OOP", "Hello", "Java"]

for word in (search_words):
    total = (file_words.count(word.lower()))
    print(word ,"->", total)