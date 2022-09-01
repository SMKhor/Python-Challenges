import datetime


def timed_proc():
    print("the lazy fox jumped over the brown dog")
    user = input("Please type: ")

start_time = datetime.datetime.now()  # Starts the timer, by putting the time into start_time variable
timed_proc()  # Whatever you want to time
time_taken = datetime.datetime.now()-start_time  # Current time - start time
print("The time taken: ",time_taken)  # Printing the time it took


#Make a procedure that times how long it takes the user to type in: e"​the lazy fox jumped over the brown dog"
