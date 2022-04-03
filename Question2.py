def average (x,y): #function to get average
    avg = ((x+y)/2)
    return avg

x = input("Enter first number x: ")     #ask for first input x
y = input("Enter second number y: ")    #ask for second input y
x = float(x)      #convert x from a float to integer
y = float(y)      #convert y from a float to integer
avg = average(x,y)  #compute the average by using the function
print("The average of " + str(x) + " & " + str(y) +" is: " + str(avg))      #prints out the average in a string message