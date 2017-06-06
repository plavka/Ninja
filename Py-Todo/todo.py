# -*- coding: utf-8 -*-

"""unos taska, ispis taska
pitati želi li još
ako ne završiti"""

todos = {}
while True:
    key = raw_input("Unesite task: ")
    rijesen = raw_input("Task riješen (da/ne): ")
    todos[key] = (rijesen.lower() == "da")
    jos = raw_input("Želite li još: (da/ne): ")
    if jos.lower() != "da":
        break

doc = open("todos.txt", "w+")
print "Završeni taskovi:"
doc.write("Rijeseni\n")
for todo in todos:
    if todos[todo] is True: #može biti i == True """može biti i samo print todo , a todo se može promijeniti i u task
        doc.write(todo + "\n")
        print "- " + todo

print "Nezavršeni taskovi:"
doc.write("\n\nNije rijeseno\n")
for todo in todos:
    if todos[todo] is False: #može i biti i != True: ili #== False: ili if not todos[#todo#]
        print "- " + todo
        doc.write(todo + "\n")
doc.close()
