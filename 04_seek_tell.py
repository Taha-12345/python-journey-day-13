file = open("sample.txt", "r")

print("Cursor position:", file.tell())
file.seek(10)
print("After seek:", file.read())

file.close()
