# Write a function that prints the numbers from 1 to n, but for multiples of 3, print "Fizz" instead of the number,
# and for multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".

def fizzbuzz(n):
    for x in range(1, n+1):
        print("Number = ", x)
        if x % 3 == 0 and x % 5 != 0:
            print("Fizz")
        elif x % 5 == 0 and x % 3 != 0:
            print("buzz")
        elif (x % 3 == 0 and x % 5 == 0):
            print("FizzBuzz")
        else:
            print(x)


if __name__ == '__main__':
    n = int(input("Enter Number : ").strip())

    fizzbuzz(n)