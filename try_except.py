def skyline(*args):
    if not args:
        return 0
    return max(args)

user_input = input("Enter numbers separated by spaces: ")
numbers = [int(num) for num in user_input.split()]
print(skyline(*numbers))



def tavan_2(x):
    return x ** 2

tavan_a = map(tavan_2, numbers)
print(list(tavan_a))

lambda x: x**3
map(lambda x: x**3, numbers)

def divisin(a,b):
    try :
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception as e:
        return f"An error occurred: {e}"
    else:
        pass
    finally:
        pass
    
print(divisin("s", 0))

