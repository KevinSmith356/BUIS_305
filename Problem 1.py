length = float(input('Enter Length'))
breadth = float(input('Enter Breadth'))
if length and breadth > 0:
    print('Valid Input')
    area1 = length * breadth
    print(area1)
else:
    print('Invalid Input')
