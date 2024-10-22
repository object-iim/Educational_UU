def all_variants(text):
    for elem in text:
        yield elem
    for i in range(len(text) - 1):
        yield text[i:i + 2]
    yield text

a = all_variants("abc")
for i in a:
    print(i)