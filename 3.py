def check(text):
    reversed_text = text[::-1]
    return text == reversed_text

text = input()
print(check(text))