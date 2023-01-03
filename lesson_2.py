# -Functions

# # creating a functtion
# def my_function():
#     print("Hello from a function!")

# print("Hello from a function!")

# # calling a function
# my_function()

# # Parameters and Arguments
# def my_function(last_name, first_name):
#     print(first_name, last_name)

# # keyword arguments
# my_function(first_name="Mohamed", last_name="ALi")


# # Arbitrary arguments
# def my_function(*args):
#     print(args[0])

# my_function('Ahmed', "Hassan", "Halima")



# # Arbitrary keyword arguments
# def my_function(**kwargs):
#     print(kwargs['first_name'])
#     print(kwargs['middle_name'])

# my_function(first_name='Ahmed', middle_name="Hassan", last_name="Halima")

# # Void and Value raturning
# def sum(num1, num2):
#     result = num1 + num2
#     return result


# res = sum(2, 6)
# print(res)
#-------------------------------------------------------------















# -Files and Exceptions 

# files
# # create a file and write data to it
# in_file = open(file='names.txt', mode='w')
# in_file.writelines('Mohamed' + '\n')
# in_file.writelines('AHmed' + '\n')
# in_file.writelines('Hassan' + '\n')

# in_file.close()


# # Read file data
# out_file = open(file='names.txt', mode='r')
# names = out_file.readlines()
# for name in names:
#     print(name.rstrip('\n'))
# print()

# out_file.close()


# # Append data to a file
# in_file = open(file='names.txt', mode='a')
# in_file.writelines('Mohamed' + '\n')
# in_file.writelines('Ahmed' + '\n')
# in_file.writelines('Hassan' + '\n')

# in_file.close()

#----------------------------------

# # Exceptions handling

# try:
#     print(2/0)
# except ZeroDivisionError as err:
#     print('Zero division error')


# print('After error')












# -Lists and Tuples
# -Dictionaries and Sets