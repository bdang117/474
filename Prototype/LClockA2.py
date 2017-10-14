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


class Package:
    # Setup constructors
    def __init__(self, message= "0", time_Stamp = 9999):
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


    # need a function to process the values
    def mainParse(self, m, n):
        #check the board for events






# ------------------------Start of main--------------------------------------
def main():

    n = 3
    m = 4

    # create the board size
    P_board1 = [[Package() for col in range(m)] for row in range(n)]

    '''
    # get range input from user
    n = int(input("Enter a number of rows: "))
    m = int(input("Enter a number of columns: "))

    if ((n > 1 and n <= 5) and (m <= 24 and m > 1)):
        # create the board size
        P_board1 = [[Package() for col in range(m)] for row in range(n)]
    else:
        print('Your dimensions do not meet our requirements!')

    # get individual message input from user
    for x in range(n):
        for y in range(m):
                P_board1[x][y].time_Stamp = int(input("Enter an event integer value: "))
    '''

    P_board1[0][0].time_Stamp = 1
    P_board1[0][1].time_Stamp = 2
    P_board1[0][2].time_Stamp = 8
    P_board1[0][3].time_Stamp = 9
    P_board1[1][0].time_Stamp = 1
    P_board1[1][1].time_Stamp = 6
    P_board1[1][2].time_Stamp = 7
    P_board1[1][3].time_Stamp = 0
    P_board1[2][0].time_Stamp = 3
    P_board1[2][1].time_Stamp = 4
    P_board1[2][2].time_Stamp = 5
    P_board1[2][3].time_Stamp = 6


    # printing the Process Board
    print('\n')
    for x in range(n):
        print('\n')
        for y in range(m):
            print(P_board1[x][y].time_Stamp, end=" ")

    for i in range(n):
        print('\n')
        for j in range(m):
            if P_board1[i][j].time_Stamp == 0:
               P_board1[i][j].set_Message("NULL")

            elif P_board1[i][j].time_Stamp == 1:
               P_board1[i][j].set_Message('a')
            else:
               #call the function
               P_board1[i][j].mainParse(m,n)



        print('\n')

    # outputting time values of messages
    for x in range(n):
        print('\n')
        for y in range(m):
            print(P_board1[x][y].get_Message(), end=" ")


if __name__ == '__main__':
    main()
