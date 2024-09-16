# Comments are denoted by the pound sign  
# Python is case sensitive 
# Naming Conventions : 
#   - Camel Case = studentId 
#   - Snake Case = student_id 
#   - Scream Snake Case = STUDENT_ID // Usually used for constants 
#   - PascalCase = StudentId

# Naming Rules 
#   - can contain a-z, A-Z, 0-9, _ 
#   - must not start with a number
#   - must not use any of the reserved words = print, input, type, etc. 
#   - must put descriptive names for readability of code


# Block Statement 
#   - indentation is used instead of { } in if statements and while loops  
# 
# The cases that would need a semicolon but not reccomended because it 
# sacrifices readability
#   >  message = "Hello World!"; print(message)

# Declaration / Variable Declaration 
#   - Python has no need for dataType. 



# Type keyword will declare the type of the variable at the time
# a = 4
# k = 0.5 
# i = "UD"

# print(type(a))
# print(type(k))
# print(type(i))

# Be Sure of the type of the variable 
# > a = input("First Number ")
# > k = input("Second Number ")

# > res = int(a) + int(k)

# Cannot put together string and int so change the type to string.
# > print("Result " + str(res))




#Flow Controls 
# if, else, elif


#grade = int(input('Grade: '))

# if  grade >= 70: 
#    print("Pass")

# else: 
#    print('Fail')


#Loops 
# for , while, do 

#range(start, end, increment by)
# > for i in range(0, 10, 21): 
# >     print(i)


# List , Tuple, Set / Acts more like a structure than an array. Multiple data types are allowed
# - [List] = Ordered-List, Mutable ( changeable ), Non-Unique ( duplicates allowed )
# - (Tuple) = Ordered-List, Non-Mutable ( not changeable ), Non-Unique ( duplicates allowed )
# - {Set}  = Un-Ordered-List, Mutable ( changeable ), Unique ( no duplicates allowed )
#        - Only allows unique values, If a duplicate is involved compiler will ignore

# > colors = {'red', 'blue', 'green', 'red'}
# > print(colors)






