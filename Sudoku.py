# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 21:04:26 2023

@author: Rami
"""

import random
import time
import file_operations
 
def create_empty_board():
    """
    Returns
    -------
    board : 2D list
        9x9 grid of zeros.

    """
    #DON'T USE [[0]*9]*9
    board = []
    for i in range(9):
        x = []
        for j in range(9):
            x.append(0)
        board.append(x)
    return board

# def valid_subsquares(grid):
#   for row in range(0, 9, 3):
#       for col in range(0,9,3):
#          temp = []
#          for r in range(row,row+3):
#             for c in range(col, col+3):
#               if grid[r][c] != 0:
#                 temp.append(grid[r][c])
          
         
#          # Checking for repeated values.
#          if len(temp) != len(set(temp)):
#              return 0
 
def is_valid(board, row, col, value):
    """
    Parameters
    ----------
    board : 2D List
        grid of numbers to check if it's a valid sudoku after the insertion.
    row : int
        row number.
    col : int
        collum number.
    value : int from 1 to 9
        number to be inserted and checked for.

    Returns
    -------
    bool
        indication of the validation of the grid.

    """
    # Check if value is already in row
    if value in board[row]:
        return False
 
    # Check if value is already in column
    for i in range(9):
        if value  == board[i][col]:
            return False
 
    # Check if value is already in 3x3 box
    box_row = row // 3
    box_col = col // 3
    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if board[i][j] == value:
                return False
 
    # Value is valid
    return True
 
def create_board(board):
    """
    function to create the board with one solution Using BackTracking

    Parameters
    ----------
    board : 2D List
        grid of zeros.

    Returns
    -------
    bool
        indication for the backtracking recursion.

    """
    # Find the next empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try each possible value in the cell
                temp = []
                for i in range(9):
                    value = random.randint(1,9)
                    while value  in temp:
                        value = random.randint(1, 9)
                    temp.append(value)
                    
                    if is_valid(board, row, col, value): #if inserted value is valid
                        board[row][col] = value
                        if create_board(board): #assume the move and buil upon It
                            return True
                        else: #--if the assumed solution is not correct empty the cell and try another one --
                            board[row][col] = 0
                        
                # If no valid value is found, backtrack
                return False
    # If all cells are filled, the board is created with one solution 
    return True
 
def generate_puzzle(difficulty):
    """
    Parameters
    ----------
    difficulty : int
        number indication the difficutly inputed from the user.

    Returns
    -------
    list
        list containing 2 elements.
        1st element is the board before removing elements 
        2nd element is the puzzle created after removing elements from the board

    """
    #create empty board(zeros means empty cells)
    board = create_empty_board()
    #create the board with one solution
    create_board(board)
    # Copy the solved board to make a puzzle
    puzzle = []
    for i in range(9):
        puzzle.append(board[i].copy()) 
    # Remove some digits to make the puzzle
    nums_to_remove = difficulty*7
    rowsDic = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    colsDic = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    while nums_to_remove > 0:
        # Find a random cell to remove
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if puzzle[row][col] == 0 or (row != min(rowsDic, key=rowsDic.get) and col != min(colsDic, key=colsDic.get)):
            continue
        #for testing:
        print("----For Testing----")
        print(row,col,puzzle[row][col])
        nums_to_remove = 1
        print("-------------------")
        #______________________
        rowsDic[row] += 1
        colsDic[col] += 1
        nums_to_remove -=1
        puzzle[row][col] = 0
    
    return [board,puzzle]

def checkSolution(board):
    """
    Parameters
    ----------
    board : 2D List
        Board we want to check if it's correct or not.

    Returns
    -------
    Boolean
        indication of correctness.

    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            #---------------checking rows -----------------#
            temp = board[i]
            
            # Checking for Zeros.
            if (0 in temp):
               
                return False
            # Checking for repeated values.
            elif len(temp) != len(set(temp)):
                
                return False
            
            
            
            #----------------------Checking Collums-------------#
            # Extracting the column.
            temp = [row[j] for row in board]
            
            # Checking for Zeros .
            if (0 in temp):
                
                return False
              # Checking for repeated values.
            elif len(temp) != len(set(temp)):
                return 0
            
            
            
            #-------------------checking 3X3 Box -----------------#
            for Brow in range(0, 9, 3):
                for Bcol in range(0,9,3):
                    temp = []
                    for row in range(Brow,Brow+3):
                        for col in range(Bcol, Bcol+3):
                            if board[row][col] != 0:
                                temp.append(board[row][col])
                                # Checking for repeated values.
                            if len(temp) != len(set(temp)):
                                return False
            
    return True


#----------------testing------------------------------
# board = [[1, 8, 9, 3, 4, 7, 2, 5, 6],
#          [6, 4, 7, 2, 1, 5, 8, 3, 9], 
#          [3, 5, 2, 8, 9, 6, 7, 4, 1],
#          [2, 3, 6, 1, 5, 4, 9, 8, 7], 
#          [9, 7, 8, 6, 2, 3, 5, 1, 4],
#          [5, 1, 4, 7, 8, 9, 3, 6, 2], 
#          [4, 6, 5, 9, 3, 2, 1, 7, 8],
#          [7, 2, 1, 5, 6, 8, 4, 9, 3],
#          [8, 9, 3, 4, 7, 1, 6, 2, 5]]
# print(checkSolution(board))



def timeResult(time_taken):
    seconds = time_taken

    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    
    result = f"{hour:.2f} Hours, {minutes:.2f} Minutes, {seconds:.2f} Seconds"
    return result




if __name__ == "__main__":

    #username of the player
    try:
        username = input("Enter your Username:\n")
    except KeyboardInterrupt:
        print("Ended")
        raise SystemExit(0)
    #difficulty of the game inputed by the user
    difficultyDict = {"easy":1,"medium":2,"hard":3,"extreme":4}
    while True:
        try:
            difficulty = input("Hi ({}) Enter difficulty level (easy, medium, hard, extreme): \n".format(username))
            print()
            difficulty = difficulty.lower()
        except KeyboardInterrupt:
            print("Ended")
            raise SystemExit(0)
        if difficulty in (difficultyDict.keys()):
            break
        else:
            print("Invalid difficulty level. Please enter one of: easy, medium, hard, extreme")
    
    #listy conatins the board and the puzzle
    listy = generate_puzzle(difficultyDict[difficulty])
    
    #file operations
    file_operations.write(listy[1], "sudoku_game.txt")
    
    
    
    
    
    
    #Time calculation
    start_time = time.time()
    try:
        input("After Your Trial,{}\npress Enter\n".format(username))
        print()
    except KeyboardInterrupt:
        print("Ended")
        raise SystemExit(0)
    end_time = time.time()
    time_taken = end_time - start_time
    #to return time in hours , minutes and seconds
    time_result = timeResult(time_taken)
    #file operations
    
    
    #Checking user solution
    #file operations
    userSolution = file_operations.readUserSolution("sudoku_game.txt")
    if(checkSolution(userSolution)):
        print("Horray,{}\nYou Solved It !!!!\n".format(username))
        print("Time Taken: " + time_result + "\n")
    else:
        print("Sorry, your solution is not correct.\n")
        print("Time Taken: " + time_result + "\n")
        
    
    #Showing the solution for the user
    try:
        show_solution = input("Do you want to see the solution? (y/n) ")
        print()
        if show_solution.lower() == "y":
            #file operations
            file_operations.write(listy[0], "solution.txt")
            
        else:
            print("Thanks for playing!")
    except KeyboardInterrupt:
        print("Ended")
        raise SystemExit(0)

