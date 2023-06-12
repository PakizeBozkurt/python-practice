# String Interpolation
#The most used f-string feature by far is string interpolation. 
# #All you need to do is wrap the value or variable in curly braces({}) and you're good to go.

str_val = 'apples'
num_val = 42

print(f'{num_val} {str_val}')  # 42 apples

#Variable names
#Apart from getting a variable's value, you can also get its name alongside the value. 
# #This can be especially useful when debugging and can be easily accomplished by adding an equals sign(=) after the variable name inside the curly braces.

#Bear in mind that whitespace inside the curly braces is taken into account, so adding spaces around the equals sign can make for a more readable result.

str_val = 'apples'
num_val = 42

print(f'{str_val=}, {num_val = }')  # str_val='apples', num_val = 42
