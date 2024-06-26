# age = int(input("enter your age "))
# if age>=18 and age<65:
#     print("your an adult")
# elif age<18:
#     print('your a minor')
# elif age>65:
#     print("your a senior citizen")
# else:
#     print("invalid age")


# for x in range (10):
#     print(x)

# prime numbers between 1 and 20
def prime(n):
    if n<=1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def print_prime_no(start, end):
    for num in range (start, end + 1):
        if prime(num):
           print(num, end=" ")

print_prime_no(1, 20)

# using while loop
start = 1
end = 20
print(f'prime numbers between {start} and {end} are: ')
# start<+end means range between 1 upto 20
while start<+end:
    divisor = 2
    while divisor <=(start // 2):
        if start % divisor == 0:
            break
        divisor += 1

    else:
        print(start)
    start += 1