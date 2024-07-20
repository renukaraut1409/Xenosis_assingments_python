# loop through each row
for row in range(11):

    #loop through each coloumn
    for col in range(11):
        mid = 11 //2

     # Conditions for printing the hollow diamond
        if row+col==mid or  col-row==mid or row-col==mid or row+col==11 - 1 + mid: 
            print("*",end="")
        else:
            print(end=" ")

    print() #start the new line after each row
