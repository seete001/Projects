# get to know how decorators work i found out that we call decorator and it returns  the function we wanna run, i thought the fuction will be compiled by itssef...


def evenMinutes(f):
    def wrapper():
        import datetime
        now = datetime.datetime.now()
        if now.minute % 2 == 0:
            return f()
    return wrapper


def def_duration(f):
    def wrapper(n):
        from datetime import datetime
        start = datetime.now()
        result = f(n)
        end = datetime.now()
        duration = end - start
        print(f"Function executed in: {duration}")
    return wrapper


#@evenMinutes
#def say_hello():
 #   print("Hello, World!")


#say_hello() # decorator will check if the current minute is even before executing the function


@def_duration
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(int(input("Enter a number: "))) # decorator will measure the execution time of the function
