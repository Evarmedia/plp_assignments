''' Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list. '''
# userInput = input('Please enter integers, seperated by comma: ' )

# inputList = userInput.split(',');

# userList = [];

# normal loop
# for num in inputList: 
#     userList.append(int(num))

# userList = [ int(num) for num in inputList ]; looping with list compression

# totalSum = sum(userList)

# print(f' the Sum of the numbers you entered is: {totalSum}')

''' Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.'''

# myBooks = ('Lord of the Rings', 'the Hobbits', "Guiliver's Travel", "The time traveler's Wife"); 

# printedBooks = [print(f'{book}') for book in myBooks]

''' Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console. '''

# user_data = {};

# user_name = input('Please enter your name: ');
# user_age = input('Please enter your age: ');
# user_fav_color = input('Please enter your favorite color: ');

# user_data["name"] = user_name;
# user_data["age"] = user_age;
# user_data["fav_color"] = user_fav_color;

# print(f'User info in a dict is {user_data}');


'''Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
'''

# set1 = set();
# set2 = set();

# user_input1 = input("Enter first set of integers, seperated by commas: ");
# user_input2 = input("Enter second set of integers, seperated by commas: ");

# user_list1 = user_input1.split(",");
# user_list2 = user_input2.split(",");

# set1.update(user_list1);
# set2.update(user_list2);

# intersection = set1 & set2;
# print(f'Intersection of both set is: {intersection}');

'''Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.
'''

# words = [];

# user_input = input('Enter list of words seperated by commas: ');

# word_list = user_input.split(',');

# print(word_list);

# for word in word_list:
#     stripped_word = word.strip();
#     if len(stripped_word) % 2 == 1:
#         print(stripped_word);

user_input = input('Enter list of words separated by commas: ')
word_list = user_input.split(',')

# List comprehension to get odd-length words after stripping spaces
odd_length_words = [word.strip() for word in word_list if len(word) % 2 == 1]

# Print each word that meets the condition
for word in odd_length_words:
    print(word)
