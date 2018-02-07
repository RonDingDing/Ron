charles = {"name": "Charles L. Dodgson", "born": 1832}
lewis = charles

lewis['balance'] = 950
alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
print(alex == charles)
print(alex is not charles)