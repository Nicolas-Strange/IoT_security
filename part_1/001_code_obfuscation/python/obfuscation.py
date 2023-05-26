# Original Python code
def calculate_sum(a, b):
    result = a + b
    return result


# Obfuscated Python code
a = 1
b = 2

# Executing the obfuscated code
"""
The sequence of character is the obfuscated version of the calculate_sum function.
I f you print obfuscated_function you will find:
calculate_sum=a + b
result = a + b
print(result)
"""
obfuscated_function = chr(99) + chr(97) + chr(108) + chr(99) + chr(117) + chr(108) + chr(97) + chr(116) + chr(
    101) + chr(95) + chr(115) + chr(117) + chr(109) + chr(61) + chr(97) + chr(32) + chr(43) + chr(32) + chr(98) + chr(
    10) + chr(114) + chr(101) + chr(115) + chr(117) + chr(108) + chr(116) + chr(32) + chr(61) + chr(32) + chr(97) + chr(
    32) + chr(43) + chr(32) + chr(98) + chr(10) + chr(112) + chr(114) + chr(105) + chr(110) + chr(116) + chr(40) + chr(
    114) + chr(101) + chr(115) + chr(117) + chr(108) + chr(116) + chr(41)

exec(obfuscated_function)

# Executing the original code
print(calculate_sum)
