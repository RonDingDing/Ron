fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
def reverse(word):
    return word[::-1]
print(reverse('testing'))
#'gnitset'
print(sorted(fruits, key=reverse))
#['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']
