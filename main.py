# name = input('WHat is your name :')
# print('Helllllooooooo ' + name)

#Fundamental Data Types
int
float
complex
bool
str
list
tuple
set
dict

None

# Above are the fundamental data types. however, we can create a custom datatypes called 'Class'
#Class --> Custom type


#Specialized Data Type--> are not built into python but can be used from packages/ Modules (Extension that you can add-on to the language)

#Example: Int numbers
# print(2+4)
# print(2/4)
# print(type(2*3))
# print(type(2+3))
# print(type(2/3))

# print(2//3) # returns int
# print(2/3) #return float
# print(2%3) #return remander
# print(2**3) #return power 3

# Math Functions - Action performed on data
# print(round(3.9))
# print(abs(-20))

# operator precedence
# print((20-3*4)-2**2)
# order - 
# ()
# **
# */
# +-

# Binary
# print(bin(15))
# print(int('0b1111',2))

# Variables
  # snake_case - user_id not user id
  #Start with lower case or underscore
  #Contains letter,number or underscores
  #Case sensative
  #Donnot overwrite keywords

#constants - represented by Capital name 
# PI = 3.14
# print(PI)

# fast varible assignments 
# a,b,c = 1,2,3
# print(b)


#Agumented assignment operator
# some_value = 5 
# some_value = some_value + 2
# some_value += 2
# some_value -= 2 
# some_value *= 2
# print(some_value)

#String Example
# print(type('my name is Gagan'))
# username = 'gagan'
# password = 'python'
# long_string = '''
# WOW
# o o
#  --
#  '''
# print(long_string)
# user_data = username + " " + password
# print(user_data)

# string Concatenation
# print ('gagan' + ' ' +'multani')

#data type conversion
# print(type(str(100)))
# print(type(int(str(100))))

#Escape Sequence
#Added \t for tab, \n for line change and \ for Escape ' in string
#greet = "\t\tIt\'s my please to meet you.\n I hope you have a good day."
# print(greet)

#formatted String
# name = 'Gagan'
# age = 27
# print('Hi ' + name + '!!\n' 'You are ' + str(age) +' year old.')
#instead of using above method. we can use formatted string and this is a feature of python3
# print(f'Hi {name} !! \n You are {age} year old.')
# # or 
# print ('Hi {} !! \n You are {} year old.'.format('Gagan','27'))
#print ('Hi {} !! \n You are {} year old.'.format(name,age))
# print ('Hi {1} !! \n You are {0} year old.'.format(name,age))
# print ('Hi {name} !! \n You are {age} year old.'.format(name='Raavi',age='27'))

#String Indexing
# selfish = '01234567'
# #[start:stop:stepover]
# print(selfish[1])
# print(selfish[1:5])
# print(selfish[-1])
# print(selfish[::2])
# print(selfish[::-1])


#Methods : methods are set of function that can be only used on specific object . example - .formate() on string object
# https://www.w3schools.com/python/python_ref_string.asp
# name = 'gagandeep singh multani'
# print(name.upper())
# print(name.capitalize())
# print(name.find('m'))
# print(name.replace('multani','Mmultani'))
# print (name)
# #In above print(name) Syntax string has not changed becaseu strings are immutable object


# #Booleans Example
# print(bool(0))
# print(bool(1))
# print(bool('True'))

# #Simple program for Age Calculator
# birth_year = int(input('What year were you born: '))
# age = 2020 - birth_year
# print(f'your age is {age} years')

# #Simple application for password check 
# username = input('Username:')
# password = input('Password:')
# pass_len = len(password)
# hidden_pass = '*' * pass_len
# print(f'{username}, your password {hidden_pass} is {pass_len} character long')


# #List objects
# shopping_cart = [
#   'apple',
#  'oatmeal',
#  'garlic',
#  'toilet papper'
# ]
# shopping_cart[0] = 'laptop' #lists are mutable
# print(shopping_cart[::1])

#Matrix/ 2D list
# matrix = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9],
#   [10,11,12]
#   ]
# print(matrix[0][2]) 

#Methods for list: https://www.w3schools.com/python/python_ref_list.asp
#adding
# matrix.append(100)
# matrix.insert(1,200)
# matrix.extend([120,150])
# print(matrix)

# #removing
# matrix.pop() #takes off the end of the list
# matrix.pop(0)
# matrix.clear()
# print(matrix)

# #Search a list
# print(matrix.index([4,5,6]))
# print([4,5,6] in matrix) #search using python ketwork
# #https://www.w3schools.com/python/python_ref_keywords.asp

# # list creation
# ls = list(range(101))
# print(ls)

# #create string from list
# line = ' '.join(['hi','my','name','is','gagan'])
# print(line)

#unpack list
# a,b,c,* other,d =[1,2,3,4,5,6,7,8,9,10]
# print(a)
# print(other)

# Dictionary is an unordered key value pair 
# dict = {
#   'a':1,
#   'b':2
# }

# print(dict)

# dict = {
#   'a':[1,2,3,4],
#   'b':'gagan',
#   'c': True
# }

# print(dict['c'])

# #Dict methods
# # https://www.w3schools.com/python/python_ref_dictionary.asp
# #use get method to avoide errors in case key is not exist in dict, take a peak 
# print(dict.get('age'))
# print(dict.get('age',50)) #incase age doesn't exist use 50

#Tuple- they are like immutable list
# tup_1 = (1,2,3,4,5)
# print(tup_1[1])

#set
#  set_1 = {1,2,3,4,4,4,5,5,5,8}
# print(set_1) #notice it returns only unique values in set
#usecase- set of emails to make sure no one is sending email address again and again 
#methods in set - https://www.w3schools.com/python/python_ref_set.asp

# #condtional statements
# is_old = True
# has_licence = True

# if is_old:
#   print('you can drive')
# else:
#   print('you should wait few years to drive')

# how_old = input( 'How old are you?')
# has_licence = input('Do you have a license? punch-in 0 for No and 1 for Yes)')
# how_old1 = int(how_old)
# has_licence1 = int(has_licence)

# if how_old1 > 18 and has_licence1 == 1:
#   print('hurryyy! you can drive')
# elif how_old1 > 18 and has_licence1 == 0: 
#   print('Great you are old enough. go get a license!!')
# else:
#   print('you should wait few years to drive')

#https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false

# #Ternary Operator
# #condtion_if_true if condition else condition if else
# #example
# is_friend = True
# can_message = 'message allowed' if is_friend else 'not allowed to message'
# print(can_message)
