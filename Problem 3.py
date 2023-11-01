import numpy
input1 = float(input('Enter Input1'))
input2 = float(input('Enter Input2'))
input3 = float(input('Enter Input3'))
input4 = float(input('Enter Input4'))
input5 = float(input('Enter Input5'))
addition = (input1 + input2 + input3 + input4 + input5)
average = [input1, input2, input3, input4, input5]
mean = numpy.mean(average)
print(addition, mean)
