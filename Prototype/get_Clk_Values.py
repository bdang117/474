#modules
import sys
import os

#board dimensions

#number of rows max
n = 5

#number of columns max (max of number of events)
m = 24

class Package:
    #Private variables

    # Setup constructors
    def __init__(self, message = " ", time_Stamp = "0"):
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
P_board1[4][23].time_Stamp = "4"
P_board1[4][23].message = "a"





def main():
    for x in range(n):
        print('\n')
        for y in range(m):
            print (P_board1[x][y].time_Stamp)

    #initialize process board
    #populate()


    #test = P_board[0][0].get_Message();

    #test = Package("a", 0)
    #print(test)

    #print(P_board[0][0].__message)
    #print(P_board[0][0].__time_Stamp)


    #Create events here
    

if __name__ == '__main__':
    main()
