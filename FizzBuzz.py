# This is a FizzBuzz Program
# If the number is divisible by both 3 and 5, the output will be "FizzBuzz"
# If the number is divisible by 3, the output will be "Fizz"
# If the number is divisible by 5, the output will be "Buzz"

# Get user input for 'n' so the program can print 1 to 'n'
n = int(input("Please enter a number for range n: "))

# using a for loop to check range 'n'
# where 'i' is incremented by 1 to start the print with 1 instead of zero
for i in range(n):
    i += 1
    if (i % 3) == 0 and (i % 5) == 0:   # Check to see if 'i' is divisible by 3 and 5
        print("FizzBuzz")
    elif (i % 3) == 0:                  # Check to see if 'i' is divisible by 3
        print("Fizz")        
    elif (i % 5) == 0:                  # Check to see if 'i' is divisible by 5
        print("Buzz")  
    else:
        print(i)                        # Print the number if it is not divisible by 3 or 5
        