
def palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

word = input("Enter a word or phrase to check palindrome: ")
if palindrome(word):
    print(f"'{word}' is a palindrome")
else:
    print(f"'{word}' is not a palindrome")
