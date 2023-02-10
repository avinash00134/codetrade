# Say we stored our course grades in a list, but some of the grades were on a four-point scale and others were on a 100-point scale. To get all the grades on the same scale, try using a lambda function with the map() function to multiply just the grades on the four-point scale by 25 to get all of the grades on the same 100-point-scale.

# Hint
# The format for including an if/else statement within a lambda function is:
# lambda arguments : (return value if condition is True) if (condition) else (return value if condition is False)

grade_list = [3.5, 3.7, 2.6, 95, 87]

# Your code below:

# assign the result of your map function to the variable grades_100scale

grades_100scale = map(lambda grade: grade*25 if grade <= 4.0 else grade, grade_list)

# convert grades_100scale to a list and save it as updated_grade_list 

updated_grade_list = list(grades_100scale)

# print updated_grade_list

print(updated_grade_list)