a = input("1st number : ")
b = input("2nd number : ")
if (int(a) > float(b)):
    print('{0} is greater than {1}.\n'.format(a, b))

elif (int(a) == float(b)):
    print('{0} and {1} are equal.\n'.format(a, b))

else:
    print('{0} is lower than {1}.\n'.format(a, b))
