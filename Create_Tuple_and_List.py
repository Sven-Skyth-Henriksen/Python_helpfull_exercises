n1 = str(input("Enter a number: "))
n2 = str(input("Enter a number: "))
n3 = str(input("Enter a number: "))
n4 = str(input("Enter a number: "))
n5 = str(input("Enter a number: "))

total = n1 + ' ' + n2 + ' ' + n3 + ' ' + n4 + ' ' + n5

# create a list
l = total.split()
print(l)

#create a tuple

t = tuple(map(str, total.split()))
print(t)