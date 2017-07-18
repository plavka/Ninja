todos = {}
while True:
    key = raw_input("Unesite task: ")
    rijesen = raw_input("Task risen (da/ne): ")
    todos[key] = (rijesen.lower() == "da")
    jos = raw_input("Zelite li jos: (da/ne): ")
    if jos.lower() != "da":
        break
doc = open("todos.txt", "w+")
print "Rijeseni"
doc.write("Rijeseni\n")
for task in todos:
    if todos[task]:
        doc.write(task + "\n")
        print task
print "Nije rijeseno"
doc.write("\n\nNije rijeseno\n")
for task in todos:
    if not todos[task]:
        print task
        doc.write(task + "\n")
doc.close()