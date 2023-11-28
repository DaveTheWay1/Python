# Numbers

# Types

print('--Types--')
print(type(24)) 
# <class 'int'>
print(type(3.9)) 
# <class 'float'>
print(type(3j)) 
# <class 'complex'>
print(" ")
print("--Practice--")

# Conversion

print('--Conversion--')
int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
# 35.0
print(float_to_int)
# 44
print(int_to_complex)
# (35+0j)
print(type(int_to_float))
# <class 'float'>
print(type(float_to_int))
# <class 'int'>
print(type(int_to_complex))
# <class 'complex'>

# Random Number

print('--Random Number--')
import random
print(random.randint(2,5)) # provides a random number between 2 and 5
print(random.randint(-10,0)) # provides a random number between -10 and 0