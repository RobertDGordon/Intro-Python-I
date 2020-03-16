"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

import os.path

with open(os.path.dirname(__file__) + '/foo.txt') as foo:
    read_data = foo.read()
    print(read_data)

print(foo.closed)


# f = open(os.path.dirname(__file__) + '/foo.txt')
# print(f)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

bar = open(os.path.dirname(__file__) + '/bar.txt', 'w')
bar.write('Umm... is this going to work?\n')
bar.write('Only one way to find out...\n')
bar.write('Yippe kai yay!\n')
bar.close()
print(bar.closed)