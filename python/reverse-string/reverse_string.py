def reverse(text):
    result = list()
    for char in text:
        result.insert(0,char)
    return "".join(result)
