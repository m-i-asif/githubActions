# # Write a function that prints the numbers from 1 to n, but for multiples of 3, print "Fizz" instead of the number,
# # and for multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".


def fizzbuzz(i):
    if i % 15 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return i


def main():
    for i in range(1, 101):
        print(fizzbuzz(i))


if __name__ == '__main__':
    main()


# def fizzbuzz(n):
#     for x in range(1, n+1):
#         print("Number = ", x)
#         if x % 3 == 0 and x % 5 != 0:
#             print("Fizz")
#         elif x % 5 == 0 and x % 3 != 0:
#             print("buzz")
#         elif (x % 3 == 0 and x % 5 == 0):
#             print("FizzBuzz")
#         else:
#             print(x)


# if __name__ == '__main__':
#     n = int(input("Enter Number : ").strip())

#     fizzbuzz(n)