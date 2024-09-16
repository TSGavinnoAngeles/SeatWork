# Program must only accept 0-100 grade value and must display an error message.
# Passing grade is 70-100.
# Minimum No. of Enrolled subjects is set to 4.
# Program will allow user to input number of grades based on the total number of enrolled subjects.

# OUTPUT:
# Student No.: []
# Name: []
# Program: []

# Number of Enrolled Subjects: [4]
# Grade for Subject 1: [80]
# Grade for Subject 2: [60]
# Grade for Subject 3: [50]
# Grade for Subject 4: [100]

# List of Passing Grades: 80, 100
# List of Failing Grades: 60, 50
 
passG = []
failG = []

studId = input("Student No.: ")
studName = input("Name: ")
studProg = input("Program: ")

noEnrolled = input("Number of Enrolled Subjects: ")

if int(noEnrolled) < 4: 
    print("ERROR: Student cannot have less than 4 subjects.") 

else:
    intEnrolled  = int(noEnrolled)
    counter = 0 
while intEnrolled is not counter:
    for i in range(intEnrolled): 
        gradeInput = input("Grade for Subject "+ str((i+1)) + " : ")
        if int(gradeInput) > 100 or int(gradeInput) <= 0: 
            print('ERROR: Invalid Grade. Try Again from the start')
            counter = 0 
            passG = []
            failG = []
            break
        else: 
            if 100 <= int(gradeInput): 
                passG.append(gradeInput)
                counter = counter + 1


            elif int(gradeInput) >= 70: 
                passG.append(gradeInput)
                counter = counter + 1

                
            else: 
                failG.append(gradeInput)
                counter = counter + 1

print(" ")
print("List of Passing Grades: " , ', '.join(passG))
print(" ")
print("List of Failing Grades: " , ', '.join(failG))


