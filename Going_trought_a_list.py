color_list = ["Red","Green","White" ,"Black"]

#print 1 and last item
print(color_list[0], color_list[-1])

#print 1-3
print(color_list[0:3])  # color_list[start : end]
print(color_list[:3]) #both options are possible

#print length of the list:
print(len(color_list))

#sorting a list:
print(sorted(color_list))

#append an item to a list:
color_list.append('Blue')
print(color_list)

#showing an item from the list with index:
print(color_list.pop(0))

#removing an item:
color_list.remove('White')
print(color_list)

#count how often an item is in a list:

print(color_list.count('Red'))

#looping over the items in a list:

for item in color_list:
    print(item)

# test if an item is in a list:

if 'Blue' in color_list:
    print('List contains: ', 'Blue')

