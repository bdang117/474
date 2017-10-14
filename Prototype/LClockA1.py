
'''
CS-474 Project 1: Lamports Logical Clock
Names: Billy Dang, Sean Mckean, Hassan Hamod

For this algorithm, we must calculate the corresponding values given an
INPUT: A list (array) of string chars of either length 2 or 1 that indicate some event
(Send, receive, or local calculation)
OUTPUT: A list of calculated values based off those corresponding events
'''

# modules
import sys
import os


# global dictionary keeping track of send commands
sARR = {}

# global time variable
time = 0

# send Flag
sFlag = 1


class Package:

    # Setup constructors
    def __init__(self, message="0", time_Stamp=0):
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


    # function helps process the message
    def mainParse(self, time):

        # check if the message is a default value
        if self.message == "0":
            return

        # check if messages first character string is "s"
        elif (self.message[0] == "s"):

            # record the local time
            self.time_Stamp = time

            # initiate send
            self.sendV()

        # # check if messages first character string is "r"
        elif (self.message[0] == "r"):

            # initiate receive
            self.recV()

        # Check if the message is NULL
        elif (self.message == "NULL" or self.message == "\n" or self.message == " "):

            # set the time_Stamp to 0
            self.time_Stamp = 0

        # Otherwise perform local calculation
        else:

            # record time stamp
            self.time_Stamp = time

            # return the time_Stamp value
            return self.time_Stamp



    # check if corresponding send function is in sARR
    # if so, compare previous object time_Stamp to sARR timestamp and select max
    def recV(self):
        global time
        if (self.message == "r1"):
            if ('s1' in sARR):
                self.time_Stamp = max(time, sARR['s1'])
                time = self.time_Stamp
        elif (self.message == "r2"):
            if ('s2' in sARR):
                self.time_Stamp = max(time, sARR['s2'])
                time = self.time_Stamp
        elif (self.message == "r3"):
            if ('s3' in sARR):
                self.time_Stamp = max(time, sARR['s3'])
                time = self.time_Stamp
        elif (self.message == "r4"):
            if ('s4' in sARR):
                self.time_Stamp = max(time, sARR['s4'])
                time = self.time_Stamp
        elif (self.message == "r5"):
            if ('s5' in sARR):
                self.time_Stamp = max(time, sARR['s5'])
                time = self.time_Stamp
        elif (self.message == "r6"):
            if ('s6' in sARR):
                self.time_Stamp = max(time, sARR['s6'])
                time = self.time_Stamp
        elif (self.message == "r7"):
            if ('s7' in sARR):
                self.time_Stamp = max(time, sARR['s7'])
                time = self.time_Stamp
        elif (self.message == "r8"):
            if ('s8' in sARR):
                self.time_Stamp = max(time, sARR['s8'])
                time = self.time_Stamp
        elif (self.message == "r9"):
            if ('s9' in sARR):
                self.time_Stamp = max(time, sARR['r9'])
                time = self.time_Stamp

        else:
            print("recieve function does not exist")

    # sender function
    def sendV(self):
        global sARR
        global sFlag

        if (self.message in sARR and self.time_Stamp < sARR[self.message]):
            return
        else:
            sFlag += 1
            sARR[self.message] = self.time_Stamp + 1



def main():
    global sARR
    global time
    global sFlag

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
                P_board1[x][y].message = input("Enter an event Value: ")

    print("\n================Initial Process Board===============")
    # printing the Process Board
    for x in range(n):
        print('\n')
        for y in range(m):
            print(P_board1[x][y].message, end=" ")



    print("\n===============The Work Begins====================")
    # goes through the array of packages and updates by calling local time
    # continues to do so if any send functions are read (sFlag)
    while (sFlag > 0):
        sFlag = 0

        for i in range(n):
            time = 1
            print('\n')
            for j in range(m):
                    temp = P_board1[i][j]
                    if (P_board1[i][j].message == "0"):
                        break
                    else:
                        temp.mainParse(time)
                        time += 1
                        P_board1[i][j].set_Time(temp.get_Time())
                        print(P_board1[i][j].time_Stamp, end= ' ')

        print('\n')

    # outputting time values of messages
    for x in range(n):
        print('\n')
        for y in range(m):
            print(P_board1[x][y].get_Time(), end=" ")



if __name__ == '__main__':
    main()
