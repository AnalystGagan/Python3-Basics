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
