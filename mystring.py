# class MyString

class MyString:
    def __init__(self, s):
        self.s = s

    def __truediv__(self, other):
        return self.s.split(other)

    def __add__(self, other):
        print('22')
        return self.s + other

    def __radd__(self, other):
        return other + self.s   # 거꾸로 주의

    def __mul__(self, other):
        return self.s * other

    def __neg__(self):
        return self.s[::-1]

s = MyString('Python Programming is Good')
t = s / ' '
print(t)

print(s + ' Job' + '1')

print('Hello' + ' ' + MyString('World'))    # radd없으면 error

print(MyString('Python') * 3)

print(-MyString('python'))