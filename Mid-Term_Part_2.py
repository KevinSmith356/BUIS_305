import numpy
import math

# Problem 1
width = 20
height = 50
rectangle = width * height
print(rectangle)

# Problem 2
r = 5
circle = math.pi * (math.pow(r, 2))
print(circle)

# Problem 3
input1 = 2
input2 = 4
input3 = 6
input4 = 8
input5 = 0
addition = (input1 + input2 + input3 + input4 + input5)
average = [input1, input2, input3, input4, input5]
mean = numpy.mean(average)
print(addition, mean)

# Problem 4
item = 4
for item in range(3):
    item = item * (item + 1)
    print(item)
