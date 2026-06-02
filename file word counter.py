# Task 2 — File Word Counter

# Count:

# lines
# words
# characters

with open("sample.txt","r")as file:
    data=file.read()
lines = data.splitlines()
words=data.split()

print("characters:", len(data))
print("words:", len(words))
print("lines:", len(lines))