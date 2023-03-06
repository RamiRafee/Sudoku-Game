def write(board,name):
    base  = 3
    side  = base*base
    
    def expandLine(line):
        return line[0]+line[11:22].join([line[1:11]*(base-1)]*base)+line[1:11]
    line0  = expandLine(" --------- ---------  ")
    line1  = expandLine("|         |         ||")
    line2  = expandLine("|    .    |    .    ||")
    line3  = line0 +"\n"+ line0

    #symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbol = " 123456789"
    nums   = [ [""]+[symbol[n] for n in row] for row in board ]

    """
    (" --------- ---------  --------- ")
    ("|         |         ||         |")
    ("|         |         ||         |")
    ("|    .    |    .    ||    .    |")
    ("|         |         ||         |")
    ("|         |         ||         |")
    (" --------- ---------  --------- ")

    """
    
    with open(__file__.replace("file_operations.py", name), "w", encoding='utf-8') as f:
        #print(line0)
        f.write(line0)
        f.write("\n")
        for r in range(1,side+1):
            f.write(line1)
            f.write("\n")
            f.write(line1)
            f.write("\n")
            f.write( "".join(n+s for n,s in zip(nums[r-1],line2.split("."))))
            f.write("\n")
            f.write(line1)
            f.write("\n")
            f.write(line1)
            f.write("\n")
            #f.write([line2,line3,line4][(r%side==0)+(r%base==0)])
            if (r%base==0 and r!=side):
                f.write(line3)
                f.write("\n")
            else:
                f.write(line0)
                f.write("\n")
        print(f"The {name} Path Is : \n")
        print(__file__.replace("file_operations.py", name))
        print()




def readUserSolution(name):
    solution=[]
    try:
        with open(name,'r') as f:
             for line in f:
                 l = []
                 for char in line:
                      if char.isdigit()==True:
                           l.append(int(char))
                 solution.append(l)
                 for j in solution:
                      if j==[]:
                          solution.remove(j)
                 for j in solution:
                      while len(j)!=9:
                          j.append(0)
        
    except FileNotFoundError:
        print("File not Found")
        raise SystemExit(0)
        
    return solution