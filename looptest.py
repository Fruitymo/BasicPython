## Edited file from a friend, test from 2019

#ask the user to type start or stop to eather start or stop the program
runProgram = str(input("Enter START or STOP:"))

n = 0

#run program if user types "start"
if runProgram == "START":
    #count up to 2000
    while n < 2000:
        #print the number we have at the moment
        print(n)
        
        #add one to the number
        n += 1

#reset the number to start over
    print("N reached 2000")
    n = 0
else:
    print("Stopped, did not run program!")