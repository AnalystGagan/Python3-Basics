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

# #short circuting using logical operators
# print(True == True)
# print ('a' >'b')
# # <, >, ==,  >=,  <=, != , and, or, not

# #some more example of condtional statement
# is_magican = False
# is_expert = True

# if is_magican and is_expert:
#   print('you are a master magician')
# elif is_magican and not(is_expert):
#   print ('At least you are getting there')
# else:
#   print('you need magic power')

#Loops
# for created_variable in 'iterable':
#example 
#  for item in "gagandeep":
#   print(item)

# for item in [1,2,3,4,5,6]:
#   print(item)

#  for item in {1,2,3,4,5,6}:
#   print(item)

# for item in (1,2,3,4,5,6):
#   print(item)
#for loop can iterate on anything that has collection of items 
#collection of items(iterable) - list, tuple,dict, string, anything)
# iterated - one by one check each item in the collection. 

# for item in [1,2,3,4,5,6]:
#   print(item)
# print('end')

# #Nested loop
# for item in [1,2,3,4,5,6]:
#   for x in ['a','b','c']:
#     print(item , x)

# #iterate over dict
# user = {
#   'name':'gagan',
#   'age' : 27,
#   'can_swim':False
# }
# for item in user:
#   print(item)

#three ways to loop over keys and values of dict 
# user = {
#   'name':'gagan',
#   'age' : 27,
#   'can_swim':False
# }
# for x in user.items():
#   print(x)

# user = {
#   'name':'gagan',
#   'age' : 27,
#   'can_swim':False
# }
# for x in user.values():
#   print(x)

# user = {
#   'name':'gagan',
#   'age' : 27,
#   'can_swim':False
# }
# for x in user.keys():
#   print(x)

# user = {
#   'name':'gagan',
#   'age' : 27,
#   'can_swim':False
# }
# for key,value in user.items():
#   print(f'{key}: {value}')

# #Counter
# mylist = [1,2,3,4,5,6,7,8,9]
# counter = 0
# for item in mylist:
#   counter = counter + item
# print(counter)

# #when looping in python -range function is really hlelpfull 
# range(0,100)
# range(0,100,2) - step over by 2
# #loop over range
# for item in range(0,100):
#   print(item)

# # looping over enumerate function
# for i,char in enumerate(list(range(100))):
#   if char == 50:
#     print(f'index of 50 is: {i}')


# #while loop
# while condtion:
#   do somthing
# i = 0
# while i<50:
#   print(i)
#   break

# i = 0
# while i<50:
#   print(i)
#   i = i + 1


# i = 0
# while i<50:
#   print(i)
#   i = i + 1
# else:
#   print('Done with all the work!!')

#deciding between for and while loop
#use while loop when you are not sure for how long you need to iterate. 
# break, continue and pass on loops

# #My first GUI!
# #Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]

# for row in picture:
#   for pix in row:
#     if (pix == 1):
#       print('*', end = "")
#     else:
#       print(' ', end = "")
#   print('')
    
# #user define functions in python
#def user_gagan():
#   print('hellooo gagan') #it is stored in the memory and can be called by user_gagan()

# user_gagan()

# #create a function from GUI code that I have wrote before. by creating function, it can be used as many time as you want.
# def merry_christmas():
#   picture = [
#      [0,0,0,1,0,0,0],
#      [0,0,1,1,1,0,0],
#      [0,1,1,1,1,1,0],
#      [1,1,1,1,1,1,1],
#      [0,0,0,1,0,0,0],
#      [0,0,0,1,0,0,0]
#    ]

#   for row in picture:
#    for pix in row:
#     if (pix == 1):
#       print('*', end = "")
#     else:
#       print(' ', end = "")
#    print('')

# merry_christmas()
# merry_christmas()
# merry_christmas()
# merry_christmas()
  
# #Parameters
# def say_hello(name, emoji):
#   print(f'Helloo {name}{emoji}')

# #Arguments/call/invoke the function- these are actual given vaules
# say_hello('gagan',' 😘')

# #positional vs keyword argument
# say_hello('😘', 'gagan')# postional
# say_hello(emoji='😘', name='gagan')

# #default parameter 
# def say_hello(name='Raavi', emoji='😍'):
#   print(f'Helloo {name}{emoji}')

# say_hello() #run with default value
# say_hello('gagan','😘') #assign values


#return 
# #our function either modify (as above) somethig or return somthing 
# def sum(num1,num2):
#   return num1+num2

# print(sum(2,3))
#thumb rule - 
#functions should do one thing really well 
#functions should return somthing

#  def sum(num1,num2):
#   def another_function(n1,n2):
#     return n1 + n2
#   return another_function(num1,num2)

# total = sum(5,10)
# print(total)

# #adding docstring inside the function
# def some_fun(value):
#   '''
#   Info:this function retuns the value
#   '''
#   print(value)

# some_fun(1)

# # help(some_fun)
# print(some_fun.__doc__)

#scope - what varible do I have access to ?
#local, parent local and global varible 

class BigObject:
  pass

#Create an object
obj1 = BigObject()
#Class creates objects 
#class instantiate(creates) an instance(object)

print(type(obj1))