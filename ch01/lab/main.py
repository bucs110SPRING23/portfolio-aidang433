#Part A
import random
weeks = 16
print(weeks, type(weeks))
classes = 5
print(classes, type(classes))
tuition = 6000
print(tuition, type(tuition))
cost_per_week = ((tuition / classes) / weeks)
print(cost_per_week, type)
print("Cost per week:", cost_per_week)
classes_per_week = 5
print(classes_per_week, type(classes_per_week))
cost_per_class = ((cost_per_week/classes_per_week))
print(cost_per_class, type(cost_per_class))
print("Cost per class :):", cost_per_class)
#Part B
numbers = 1,2,16,46,200,81
random.choice(numbers)
my_number = random.choice(numbers)
print("Your random number is...", my_number)