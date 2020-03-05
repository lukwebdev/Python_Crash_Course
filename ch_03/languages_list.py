languages = ["Dart", "Python", "Go", "Java"]

print(languages)
print(languages[2])
languages[-1] = "JS"
print(languages)
languages.append("Java")
print(languages)
languages.insert(0, "C++")
print(languages)
del languages[1]
print(languages)
last_del = languages.pop()
print(last_del)
print(languages)
languages.remove("Go")
print(languages)

languages.sort()
print(languages)

languages.sort(reverse=True)
print(languages)

print(sorted(languages))
print(languages)

languages.reverse()
print(languages)

print(len(languages))