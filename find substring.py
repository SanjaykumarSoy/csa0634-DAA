def find_substrings(words):
    return [word for word in words if any(word in other for other in words if word != other)]
words = ["mass", "as", "hero", "superhero"]
output = find_substrings(words)
print(output) 

