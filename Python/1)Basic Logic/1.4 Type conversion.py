
# Integer
num = 25
print("Integer:", num)
print("int -> float:", float(num))
print("int -> str:", str(num))
print("int -> bool:", bool(num))
print()

# Float
decimal = 15.75
print("Float:", decimal)
print("float -> int:", int(decimal))
print("float -> str:", str(decimal))
print("float -> bool:", bool(decimal))
print()

# String
text = "100"
print("String:", text)
print("str -> int:", int(text))
print("str -> float:", float(text))
print("str -> bool:", bool(text))
print()

# Boolean
flag = True
print("Boolean:", flag)
print("bool -> int:", int(flag))
print("bool -> float:", float(flag))
print("bool -> str:", str(flag))
print()

# List
numbers = [10, 20, 30]
print("List:", numbers)
print("list -> tuple:", tuple(numbers))
print("list -> set:", set(numbers))
print("list -> str:", str(numbers))
print()

# Tuple
t = (1, 2, 3)
print("Tuple:", t)
print("tuple -> list:", list(t))
print("tuple -> set:", set(t))
print("tuple -> str:", str(t))
print()

# Set
s = {5, 6, 7}
print("Set:", s)
print("set -> list:", list(s))
print("set -> tuple:", tuple(s))
print("set -> str:", str(s))
print()

# Dictionary
student = {"name": "Priyanka", "age": 21}
print("Dictionary:", student)
print("dict -> list:", list(student))          # Keys only
print("dict -> tuple:", tuple(student))        # Keys only
print("dict -> set:", set(student))            # Keys only
print("dict -> str:", str(student))
print()

# Character conversions using ASCII
ch = 'A'
print("Character:", ch)
print("char -> ASCII:", ord(ch))

ascii_value = 66
print("ASCII -> char:", chr(ascii_value))
print()

# Binary, Octal and Hexadecimal
n = 25
print("Number:", n)
print("Binary:", bin(n))
print("Octal:", oct(n))
print("Hexadecimal:", hex(n))
print()

# String to List, Tuple and Set
word = "Python"
print("String:", word)
print("str -> list:", list(word))
print("str -> tuple:", tuple(word))
print("str -> set:", set(word))