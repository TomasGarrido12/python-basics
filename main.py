# List comprehensions
def list_examples():
    names = ['Louise', 'Peter', 'Anne', 'Judith']
    first_letter = [name[0] for name in names]
    pair_numbers = [n for n in [1, 2, 3, 4, 5] if n % 2 == 0]
    max_number = max([n for n in [2, 45, 6, 89, 34, 7, 51]])
    # dictionary with numbers as keys and their power as values
    square_dict = { n: n*n for n in [1, 2, 3, 4, 5] }

    print(first_letter) # ['A', 'L', 'P', 'A', 'J']
    print([n*n for n in range(10)]) # [0, 1, 4, 9, 16...]
    print(pair_numbers) # [2, 4]
    print(f"Max number is {max_number}") # 89
    print(f"Max is {max(['a', 'b', 'c'])}") # 'c'
    print(square_dict) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# The problem with list comprehensions is that lists are built in memory
# and that is inefficient. That is where generators come in.

# Generators are lazily evaluated
def generator_examples():
    print("Generators example")
    nums = (n for n in [1, 2, 3, 4, 5])
    print(list(nums))

def slicing_lists():
    letters = ['a','b','c','d','e']
    second_to_last = letters[1:]
    all_but_last = letters[:-1]
    copy_of_letters = letters[:]
    backwards = letters[::-1]
    print(f'slicing - second to last: {second_to_last}')
    print(f'slicing - all to last: {all_but_last}')
    print(f'copy of list: {copy_of_letters}')
    print(f'backwards: {backwards}')

# https://www.learnpython.dev/03-intermediate-python/20-advanced-looping/90-exercise/

def main():
    print("Hello world!")

if __name__ == "__main__":
    print("we are at main")
    list_examples()
    generator_examples()
    slicing_lists()
