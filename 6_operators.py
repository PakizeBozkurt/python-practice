def add_one(num):
  return num + 1

# To see the table:

# | Code           | What is it?                                        |
# | -------------- | -------------------------------------------------- |
# | def            | `def` is a keyword that defines a new function     |
# | add_one        | `add_one` is the function name                     |
# | (num)          | `(num)` is the parameter list                      |
# | num            | `num` is a parameter                               |
# | :              | The `:` symbol indicates the body should start now |
# | return num + 1 | `return num + 1` is a statement                    |
# | num + 1        | `num + 1` is an expression                         |
# | num            | `num` here is a variable                           |
# | +              | `+` is an operator                                 |
# | 1              | `1` is a literal number                            |


# Addition
added = 2 + 3
print(f"2 + 3 = {added} (should be 5)")

# Multiplication
multiplied = 2 * 3
print(f"2 * 3 = {multiplied} (should be 6)")

# == Subtraction ==

subtracted = 2 - 3
print(f"2 - 3 = {subtracted} (should be -1)")

# == Division ==

divided = 2 / 3
print(f"2 / 3 = {divided} (should be 0.6666666666666666)")

# == Modulus ==
# Sometimes known as "remainder if we divide 3 by 2"

modulus = 3 % 2
print(f"3 % 2 = {modulus} (should be 1)")

# == Floor division ==
# Sometimes known as "division without remainder"

floor_divided = 2 // 3
print(f"2 // 3 = {floor_divided} (should be 0)")

# == Exponentiation ==
# Sometimes known as "2 to the power of 3"

expr = 2 ** 3
print(f"2 ** 3 = {expr} (should be 8)")
