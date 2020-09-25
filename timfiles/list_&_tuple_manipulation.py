# https://www.youtube.com/watch?v=1uCH3zqbv2s&list=PLzMcBGfZo4-mFu00qxl0a67RhjjZj3jXm&index=8
# Python Programming Tutorial #8 - List's and Tuples

# Elements in lists are called "items"
my_list = ["a", "b", 3, "d", "e", "f", "g", "h"] # list

# Used for coordinates, colors, rectangles, & other mathy stuff
my_tuple = ("a", "b", "c", 4, "e", "f", "g", "h") # tuple

print(my_tuple[slice(3, 5)])
print(my_list[slice(3, 5)])

my_list.append("i") # cannot append a tuple

# set item
my_list[-1] = "z"

print(my_list)

# Checkout this for .pop() & .shift() type stuff:
# https://docs.python.org/3.3/tutorial/datastructures.html