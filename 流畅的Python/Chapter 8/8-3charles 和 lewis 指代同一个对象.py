charles = {"name": "Charles L. Dodgson", "born": 1832}
lewis = charles
print(lewis is charles)
print(id(lewis), id(charles))
lewis['balance'] = 950
print(charles)
