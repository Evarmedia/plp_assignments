# Create an empty list called my_list.
my_list = []

firstList_to_be_added = [10, 20, 30, 40]

# Append the following elements to my_list: 10, 20, 30, 40.
my_list.extend(firstList_to_be_added);

# Insert the value 15 at the second position in the list.
my_list[1] = 15;

# Extend my_list with another list: [50, 60, 70].
another_list_to_be_added = [50, 60, 70];

my_list.extend(another_list_to_be_added);

# Remove the last element from my_list.
my_list.pop();

# Sort my_list in ascending order.
my_list.sort();

# Find and print the index of the value 30 in my_list.
print(my_list.index(30));