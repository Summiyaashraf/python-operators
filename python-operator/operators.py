# Arithmetic Operators
x = 10
y = 3
print('Addition:', x + y)
print('Subtraction:', x - y)
print('Multiplication:', x * y)
print('Division:', x / y)
print('Floor Division:', x // y)
print('Modulus:', x % y)
print('Exponentiation:', x ** y)

# Assignment Operators
a = 5
a += 3  # Equivalent to a = a + 3
print('Assignment +=:', a)
a -= 2  # Equivalent to a = a - 2
print('Assignment -=:', a)

# Comparison Operators
print('Equal:', x == y)
print('Not Equal:', x != y)
print('Greater Than:', x > y)
print('Less Than:', x < y)

# Logical Operators
p = True
q = False
print('Logical AND:', p and q)
print('Logical OR:', p or q)
print('Logical NOT:', not p)

# Identity Operators
print('Identity is:', x is y)
print('Identity is not:', x is not y)

# Membership Operators
lst = [1, 2, 3, 4, 5]
print('Membership in:', 3 in lst)
print('Membership not in:', 6 not in lst)

# Bitwise Operators
m = 5  # 0101 in binary
n = 3  # 0011 in binary
print('Bitwise AND:', m & n)
print('Bitwise OR:', m | n)
print('Bitwise XOR:', m ^ n)
print('Bitwise NOT:', ~m)
print('Left Shift:', m << 1)
print('Right Shift:', m >> 1)
