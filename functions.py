# Functions
#----------
# # Creating a Function
# def my_function():
#     print('Hello from a function!')

# # Calling a Function
# my_function()

# # Parameters and Arguments
# def my_function(fname):
#     print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# Arbitrary Arguments
def my_function(*args):
    print("The youngest child is " + args[1])


my_function("Mohamed", "Ahmed")
