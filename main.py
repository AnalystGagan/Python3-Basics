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
name = 'Gagan'
age = 27
# print('Hi ' + name + '!!\n' 'You are ' + str(age) +' year old.')
#instead of using above method. we can use formatted string and this is a feature of python3
# print(f'Hi {name} !! \n You are {age} year old.')
# # or 
# print ('Hi {} !! \n You are {} year old.'.format('Gagan','27'))
#print ('Hi {} !! \n You are {} year old.'.format(name,age))
# print ('Hi {1} !! \n You are {0} year old.'.format(name,age))
# print ('Hi {name} !! \n You are {age} year old.'.format(name='Raavi',age='27'))

