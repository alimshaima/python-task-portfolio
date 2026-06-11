# File Word Counter
filename = input("Enter filename: ")

with open(filename, 'r') as f:
    text = f.read()

for char in ".,!?:;\"'()":
    text = text.replace(char, " ")

words = text.lower().split()
count = {}

for w in words:
    count[w] = count.get(w, 0) + 1

for w in sorted(count):
    print(f"{w}: {count[w]}")
