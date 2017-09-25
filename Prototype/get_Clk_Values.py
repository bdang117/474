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
    __message = None
    __time_Stamp = None

    # Setup constructors
    def __init__(self, message = " ", time_Stamp = "0"):
        self.__message = message
        self.__time_Stamp = time_Stamp


    # Set functions
    def set_Message(self, message):
        self.__message = message

    def set_Time(self,time_Stamp):
        self.__time_Stamp = time_Stamp

    # Get functions
    def get_Message(self):
        return str(self.__message)

    def get_Time(self):
        return str(self.__time_Stamp)

    def __str__(self):
        return "From str method: Message: is %s, Time: is %s" % (self.message, self.time_Stamp)



#create the board size
P_board = [[0 for col in range(m)] for row in range(n)]
#P_board = [default for col in range(m)]



def main():
    for x in range(len(P_board)):
        print (P_board[x])

    #initialize process board
    #populate()

    test = P_board[0][0];
    print(test)

    #print(P_board[0][0].__message)
    #print(P_board[0][0].__time_Stamp)


    #Create events here
    

if __name__ == '__main__':
    main()
