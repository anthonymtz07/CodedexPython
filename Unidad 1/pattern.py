"""

Pattern

Line by Line

Python is run one a time, from top to bottom. 
We can output multiple messages by using multiple print(fuctions). For exameple, if we want to print out two simple greetings:
* print('Morning Dharma!')
* print('Evening Sonny!')

This will output:
*   Morning Dharma!
*   Evening Sonny!

Instructions
Supponse we want the output to look exactly like this pattern below: 
1
2 3
4 5 6
7 8 9 10

How can you do that? 
Create a pattern.py program that prints this pattern exactly as shown. 
This is will likely take some trial and error, but give it a shot!

"""
def List(number):
    i,listNum = 0, []
    while i <= number:
        if i == 0:
            i =i+1 
        listNum.append(i) 
        i = i+1
    PrintList(number,listNum)

def PrintList(i,listNum):
    #Variables
    j, k = 0, 3
    n,m = 3,4

    #Cycle
    while j < i:
        if j == 0 : 
            print(listNum[j])
            j = j+1
        elif j == 1:
            print(listNum[j:k]) 
            j,k = j+2, k+3 
        else: 
            print(listNum[j:k])
            j,k = j+n, k + m
            n,m = n + 1,m + 1




    



List(int(input("How many numbers do you need?: ")))

