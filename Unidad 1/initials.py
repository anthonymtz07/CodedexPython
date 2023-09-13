"""
#Commets
Commets are very important in programming because they are used to document what outr code does. They are also used to disable parts of the program.

When the program is run, the commets are ignored.

In python, we can create a comment using the # hastag symbol: 

#printing out message
print('hi')

On the first line, we created a comment. As a result, everything to the right of the hashtag # is ignored. The program continues to the next line, and the
output is simply: 

hi

Python only ignores anything after the # on a line. So when a comment is placed towards the end of a line: 

print('Hi') #I'm a comment, too!

Here,the output would still be "Hi" because everything before the comment on the same line will still run. 


Instructions

Create an initials.py program that displays your initials in block letters 

First, start your program with a comment that says a fun fact about yourself. 

Then, create your block letters with your initials.

For example, if your name is Dua Lipa, your initials would be D and L, and your bloc letters would look like this: 

DDDD    L
D   D   L
D   D   L 
D   D   L   
D   D   L
D   D   L
DDDD    LLLLL

"""

def PrintJ():
    print('JJJJJJJ')
    print('   J')
    print('   J')
    print('   J')
    print('   J')
    print('J  J')
    print('JJJJ')

def PrintA():
    print('      A')
    print('     A A')
    print('    A   A')
    print('   AAAAAAA')
    print('  A       A')
    print(' A         A')
    print('A           A')

PrintJ() 
PrintA()