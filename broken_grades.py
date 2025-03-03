# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: ")) # (Mohammed suhayl, M01033117) added the missing int()
exam_3 = int(input("Input exam grade three: ")) # ((Mohammed suhayl, M01033117) instead of str added int()

grades = [exam_one, exam_two, exam_3] # (Mohammed suhayl, M01033117) added missing commas and instead of three added 3

total = sum(grades)
avg = total / len(grades) # (Mohammed suhayl, M01033117) fixed loop errors and spelling mistakes in grades

if avg >= 90:
    letter_grade = "A"
elif avg >= 80: # (Mohammed suhayl, M01033117) added missing semicolons
    letter_grade = "B"
elif avg >= 70: # (Mohammed suhayl, M01033117) instead of 69 to 80 changes to 70
    letter_grade = "C" # (Mohammed suhayl, M01033117) fixed mismatched quote
elif avg >= 60: # (Mohammed suhayl, M01033117) instead of <= 69 and avg >= 65 changed to >=60
    letter_grade = "D"
else: # (Mohammed suhayl, M01033117) instead of elif changes to else
    letter_grade = "F"

# Print results
for grade in grades:
    print("Exam: " + str(grade))

print("Average: " + str(avg))
print("Grade: " + letter_grade)

if letter_grade == "F": # (Mohammed suhayl, M01033117) letter-grade is "F" should be letter_grade == "F"
    print("Student is failing.") # (Mohammed suhayl, M01033117) print "Student is failing." should be print("Student is failing.")
else:
    print("Student is passing.")