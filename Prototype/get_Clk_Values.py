#modules
import sys
import os

#board dimensions

#number of rows max
n = 5

#number of columns max (max of number of events)
m = 24

sARR = []

class Package:
    #Private variables

    # Setup constructors
    def __init__(self, message = "0", time_Stamp = 0):
        self.message = message
        self.time_Stamp = time_Stamp

    # Set functions
    def set_Message(self, message):
        self.message = message

    def set_Time(self,time_Stamp):
        self.time_Stamp = time_Stamp

    # Get functions
    def get_Message(self):
        return str(self.message)

    def get_Time(self):
        return int(self.time_Stamp)

    # functions that perform local calculations


    def local_Count(self,time):
        if self.message == "0":
            return
        elif (self.message[0] == "s"):
            temp = int(self.message[1])
            print(temp)
            #self.sendV(temp, self.time_Stamp)
        else:
            self.time_Stamp = time
            # P.time_Stamp = time
            return self.time_Stamp
        # sender(P)

    def sendV(self, number, time):
        global sARR
        sARR[number] = time

#create the board size
P_board1 = [[Package() for col in range(m)] for row in range(n)]

#fixed values for P_board1
P_board1[0][0].set_Message("a")
P_board1[0][1].set_Message("s1")
P_board1[0][2].set_Message("r3")
P_board1[0][3].set_Message("b")
P_board1[1][0].set_Message("c")
P_board1[1][1].set_Message("r2")
P_board1[1][2].set_Message("s3")
P_board1[2][0].set_Message("r1")
P_board1[2][1].set_Message("d")
P_board1[2][2].set_Message("s2")
P_board1[2][3].set_Message("e")



def main():

    #see if we have default Package objects
    for x in range(n):
        print('\n')
        for y in range(m):
            print(P_board1[x][y].message, end = " ")

    #test to see if time is changed
    for i in range(n):
        time = 1
        for j in range(m):
            #P_board1[i][j].time_Stamp = local_Count(time)
            e = P_board1[i][j]
            if(P_board1[i][j].message == "0"):
                break
            else:
                e.local_Count(time);
                time += 1
                temp_val = e.get_Time()
                P_board1[i][j].set_Time(e.get_Time())

    print('\n', P_board1[2][3].get_Time())

if __name__ == '__main__':
    main()
