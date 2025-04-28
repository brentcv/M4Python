'''
Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python.
Start each line with the phrase In Python you can... .
Save the file as learning_python.txt.
Write a program that reads the file and prints what you wrote three times.
Print the contents once by reading in the entire file, 
once by looping over the file object, and 
once by storing the lines in a list and then working with them outside the with block.

You can use the replace() method to replace any word in a string with a different word . 
Here’s a quick example showing how to replace 'dog' with 'cat' in a sentence:
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
    'I really like cats.'
Read in each line from the file you just created, learning_python.txt, and replace the word Python with the name of another language, such as PHP.
Print each modified line to the screen.
Take a screenshot of your successfully executed code and upload it in the space provided.
'''

# Write a program that reads the file and prints what you wrote three times
with open("learning_python.txt", 'r') as f:
    lp = (f.read())
    for i in range(0,3):
        print(lp,'\n 1---')

# Print the contents once by reading in the entire file
with open("learning_python.txt", 'r') as f:
    print(f.read())
    print('2---')

# once by looping over the file object
with open("learning_python.txt", 'r') as f:
    for i in range(4):
        print(f.readline())
        print('3---')

# once by storing the lines in a list and then working with them outside the with block
learning_list = []
with open("learning_python.txt", 'r') as f:
    learning_list = f.readlines()

print(learning_list)
print('4---')

# Read in each line from the file you just created, learning_python.txt, and 
# replace the word Python with the name of another language, such as PHP.
with open("learning_python.txt", 'r') as f:
    lpy = (f.read())
    lphp = lpy.replace("Python","PHP")
    print(lphp)
    print('5---')


