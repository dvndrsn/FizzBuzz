# FizzBuzz
# Coded by Dave A. for Hacker School NYC
# # # # # # # # # # # # # # # # # # # # # # # #
# For each of the numbers from 1 to 100
# print Fizz if the number is divisible by 3,
# Buzz if the number is divisible by 5,
# FizzBuzz if it is divisible by both, or otherwise,
# just print the number.
# # # # # # # # # # # # # # # # # # # # # # # #

# Its fizzbuzz!
def main():
    # test cases (in case you don't care to loop through all the examples.
    # printFizzBuzz(3)
    # printFizzBuzz(5)
    # printFizzBuzz(15)
    # printFizzBuzz(1)

    for i in range(1,100+1):
        printFizzBuzz(i)


# prints the appropriate Fizz/Buzz message for the given number.
def printFizzBuzz(n):
    fizz = (n % 3) == 0
    buzz = (n % 5) == 0

    if (fizz and buzz):
        print 'FizzBuzz'
    elif (fizz):
        print 'Fizz'
    elif (buzz):
        print 'Buzz'
    else:
        print n

if __name__ == '__main__':
    main()
