raw_ages = [32, 40, None, 1, 32]

clean_ages = []  # This is our accumulator again

for age in raw_ages:  # We go through each age
  # We combine a for with an if to remove 'None' items
  if age != None:
    clean_ages.append(age)

print(raw_ages)
print(clean_ages)
