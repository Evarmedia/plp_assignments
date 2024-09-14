'''
Demonstrate your understanding of Python file handling by completing the following tasks.

Tasks:
File Creation:
Create a Python script (file_handling_assignment.py) that does the following:
Creates a new text file named "my_file.txt" in write mode ('w').
Write at least three lines of text to the file, including a mix of strings and numbers.

File Reading and Display:
Enhance your script to read the contents of "my_file.txt" and display them on the console.

File Appending:
Modify the script to open "my_file.txt" in append mode ('a').
Append three additional lines of text to the existing content.

Error Handling:
Implement error handling using try, except, and finally blocks to manage potential file-related exceptions (e.g., FileNotFoundError, PermissionError).'''

# Final version with error handling
try:
    # Writing to the file
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is the first line.\n")
        file.write("This file contains some sample numbers like 12345.\n")
        file.write("Here's another line with more text and numbers: 98765.\n")
    print("File 'my_file.txt' created and written successfully.")

    # Reading the file
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("File contents:")
        print(content)

    # Appending to the file
    with open("my_file.txt", "a") as file:
        file.write("This is an appended line.\n")
        file.write("Appended another line with more text.\n")
        file.write("Appending numbers too: 54321.\n")
    print("New lines appended successfully.")

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to access this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File handling operations completed.")
