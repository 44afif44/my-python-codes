words = ["Donkey","monkey","bad","ugly"]

with open("file.txt", "r") as f:
    content = f.read()
for word in words:
   
   
#    contentNew = content.replace(word, "######")
   content= content.replace(word.capitalize(), "######")

with open("file.txt", "w") as f:
    f.write(content)