# First the function that will combine all
# the other functions together to create the graph.
# This will give you an idea of the flow of the program.
def generate_frequency_graph(numbers):
  integers = get_only_integers(numbers)
  positive_integers = convert_negatives_to_positives(integers)
  number_frequency = calc_frequency_of_numbers(positive_integers)
  graph = format_graph(number_frequency)
  return graph

# Here we'll use filtering to get rid of the None values


def get_only_integers(numbers):
  integers = []
  for number in numbers:
    if number != None:
      integers.append(number)
  return integers

# Here we'll use mapping to convert negative numbers to
# positive numbers


def convert_negatives_to_positives(numbers):
  positive_integers = []
  for number in numbers:
    if number < 0:
      positive_number = number * -1
      # Note that a negative number multiplied by -1
      # will be its positive equivalent
      positive_integers.append(positive_number)
    else:
      positive_integers.append(number)
  return positive_integers

# Here we'll use dictionary summarising to create a graph of
# how frequently each number shows up


def calc_frequency_of_numbers(numbers):
  number_frequency = {}
  for number in numbers:
    if number not in number_frequency:
      number_frequency[number] = 1
    else:
      number_frequency[number] += 1
  return number_frequency

# Here we'll use summarising and mapping in the same loop to
# format the graph.


def format_graph(number_frequency):
  graph = ""
  for number in number_frequency:
    # Note the cool use of 'string multiplication' here!
    # 'x' * 3 will give you 'xxx'
    graph += f"{number}: {'x' * number_frequency[number]}\n"
  return graph



print("Final graph:")
print(generate_frequency_graph())
