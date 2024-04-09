# Introduction to Lists(mutable)

shopping_list = ['apples', 'bananas', 'oranges', 'cheese']

print(shopping_list)
print(shopping_list[2])
print(shopping_list[0:2])

# add items to our list

shopping_list.append('blueberries')

print(shopping_list)

# Update items in our list

shopping_list[0] = 'cherries'

print(shopping_list)

# delete items in our list

del shopping_list[1]

print(shopping_list)

# length of list

print(len(shopping_list))

# Merging two list through addition 

shopping_list_2 = ['bread', 'jam', 'pb']
print(shopping_list+shopping_list_2)

# Mutiplying list

print(shopping_list * 2)

# max and min of list

list_num = [ 1, 2, 3, 4, 5 ]
print(max(list_num))
print(min(list_num))