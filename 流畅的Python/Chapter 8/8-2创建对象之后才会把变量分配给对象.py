class Gizmo:
    def __init__(self):
        print("Gizom id: %d" % id(self))


x = Gizmo()
print(dir())
y = Gizmo() * 10

# Gizom id: 6140720
# Gizom id: 31592784
# Traceback (most recent call last):
#   File "E:/Python/流畅的Python/Chapter 8/8-2创建对象之后才会把变量分配给对象.py", line 7, in <module>
#     y = Gizmo() * 10
# TypeError: unsupported operand type(s) for *: 'Gizmo' and 'int'