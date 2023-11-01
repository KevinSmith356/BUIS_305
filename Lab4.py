# Step 2
for numbers in range(0, 10):
    print(numbers)
# Step 3
for number in range(1, 10):
    print(number)
# Step 4
for order in range(-1, 10, 2):
    print(order)
# Steps 5-7
radius = float(input('Enter Radius'))
if radius > 0:
    print('Valid Input')
    area = 3.14 * radius * radius
    print(area)
else:
    print('Invalid Input')
# Steps 9-10
length = float(input('Enter Length'))
breadth = float(input('Enter Breadth'))
if length and breadth > 0:
    print('Valid Input')
    area1 = length * breadth
    print(area1)
else:
    print('Invalid Input')
# Step 11
length = float(input('Enter Length'))
breadth = float(input('Enter Breadth'))
if length and breadth >= 0:
    print('Valid Input')
    area2 = length * breadth
    print(area2)