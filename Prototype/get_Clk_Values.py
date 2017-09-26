#modules
import sys
import os

#board dimensions

#number of rows max
n = 5

#number of columns max (max of number of events)
m = 24

#time 
#time = 0

class Package:
    #Private variables

    # Setup constructors
    def __init__(self, message = "0", time_Stamp = "0"):
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
        return str(self.time_Stamp)



#create the board size
P_board1 = [[Package() for col in range(m)] for row in range(n)]

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


P = Package()

#functions that perform local calculations
def local_Count(P, time):
    if P.message == "0":    
        exit()
    else:
        time += 1
        P.time_Stamp = str(time)
        #sender(P)



def main():
    time = 0;


    for x in range(n):
        print('\n')
        for y in range(m):
            print(P_board1[x][y].message, end = " ") 

    #Create events here
    for i in range(m): 
        for j in range(n):
            local_Count(P_board1[i][j],time)    

print(P_board1[1][2].time_Stamp)    
if __name__ == '__main__':
    main()
