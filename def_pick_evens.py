def pick_evens(*args):
    return [arg for arg in args if arg % 2 == 0]

user_input = input("Enter numbers separated by spaces: ")
numbers = [int(num) for num in user_input.split()]
print(pick_evens(*numbers))
