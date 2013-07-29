def main():
    for i in range(1,100+1):
        printFizzBuzz(i)
    # test cases
    # printFizzBuzz(3)
    # printFizzBuzz(15)
    # printFizzBuzz(1)

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
