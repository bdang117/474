'''
CS-474 Project 1: Lamports Logical Clock
Names: Billy Dang, Sean Mckean, Hassan Hamod

For this algorithm, we must obtain the corresponding events given an
INPUT: A list (array) of integers
OUTPUT: A list of strings length 1 or 2 based off those corresponding values
'''

# modules
import sys
import os
import string
import random
import operator


class Package:
    # Setup constructors
    def __init__(self, message='xx', time_Stamp=9999):
        self.message = message
        self.time_Stamp = time_Stamp

    # Set functions
    def set_Message(self, message):
        self.message = message

    def set_Time(self, time_Stamp):
        self.time_Stamp = time_Stamp

    # Get functions
    def get_Message(self):
        return str(self.message)

    def get_Time(self):
        return int(self.time_Stamp)


# ------------------------Start of main--------------------------------------
def main():
    # get range input from user
    n = int(input("Enter a number of rows: "))
    m = int(input("Enter a number of columns: "))

    tempArr = []

    if ((n > 1 and n <= 5) and (m <= 24 and m > 1)):
        # create the board size
        P_board1 = [[Package() for col in range(m)] for row in range(n)]
    else:
        print('Your dimensions do not meet our requirements!')

    # get individual message input from user
    for x in range(n):
        for y in range(m):
            tempe = int(input("Enter an event integer value: "))
            tempArr.append(tempe)
            P_board1[x][y].time_stamp = tempe


    sortedList = sorted(tempArr)
    for x in range(len(sortedList)):
        if (sortedList[x] - sortedList[x - 1] > 1):
            print('INCORRECT')
            sys.exit

    # printing the Process Board
    print('------------------Initial Board--------------------')
    for x in range(n):
        print('\n')
        for y in range(m):
            print(P_board1[x][y].time_Stamp, end=" ")

    for i in range(n):
        for j in range(m):
            if P_board1[i][j].time_Stamp == 0:
                P_board1[i][j].set_Message("NULL")

            elif P_board1[i][j].time_Stamp == 1:
                P_board1[i][j].set_Message(random.choice(string.ascii_lowercase[:16]))

            elif P_board1[i][j].time_Stamp - P_board1[i][j - 1].time_Stamp > 1 and j != 0 or j == 0 and P_board1[i][
                j].time_Stamp > 1:
                P_board1[i][j].set_Message('r')
                for k in range(n):
                    for l in range(m):
                        if (P_board1[i][j].time_Stamp - 1 == P_board1[k][l].time_Stamp):
                            P_board1[k][l].set_Message('s')

    # for the last remaining local calculations
    for i in range(n):
        for j in range(m):
            if P_board1[i][j].message == 'xx':
                P_board1[i][j].set_Message(random.choice(string.ascii_lowercase[:16]))

    # now lets assign event values based on what was entered
    list_Values = {}
    counter = 1

    # get the send values
    for i in range(n):
        for j in range(m):
            if P_board1[i][j].message == 's':
                # grab time from object
                temp = P_board1[i][j].get_Time()
                # store the values into an array
                list_Values.setdefault(str(temp), counter)
                counter += 1

    # sort the send values
    list_Values = sorted(list_Values.items(), key=operator.itemgetter(0))

    '''for i in range(len(list_Values)):
        list_Values[i] = counter
        counter += 1'''

    # get length of list
    x = len(list_Values)

    # now lets label the send events with numbers
    for i in range(n):
        for j in range(m):
            for k in range(x):
                if P_board1[i][j].time_Stamp == list_Values[k]:
                    temp2 = P_board1[i][j].get_Message()
                    temp2 += str(list_Values[k])
                    P_board1[i][j].set_Message(temp2)

    # now lets get the r's
    for i in range(n):
        for j in range(m):
            if P_board1[i][j].message == "r":
                for k in range(n):
                    for l in range(m):
                        if (P_board1[i][j].time_Stamp - 1 == P_board1[k][l].time_Stamp):
                            P_board1[i][j].set_Message('r' + P_board1[k][l].get_Message()[1:])

    print('\n------------------After Run--------------------')
    # outputting messages
    for x in range(n):
        print('\n')
        for y in range(m):
            print(P_board1[x][y].get_Message(), end=" ")

    if __name__ == '__main__':
        main()
