''' 
Kindly go through the assignment, and submit the GitHub repo
Create a Python class named Person.
The Person class should have the following attributes:
name: representing the person's name.
age: representing the person's age.
gender: representing the person's gender.
Implement a method called introduce that prints a message introducing the person with their name, age, and gender.
Create an instance of the Person class and call the introduce method to display the person's information.
Create a GitHub repository for your assignment and submit the link. 
'''
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f'Your Name is: {self.name}, Your age is: {self.age}, Your gender is: {self.gender}')
    
person_one = Person('Mishak', 27, 'Male')

person_one.introduce()