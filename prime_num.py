# Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number == 1:
            is_prime
        elif number % i == 0:
            is_prime = False
        else:
            is_prime
    if is_prime:
        print(f"{number} is't a prime number")
    else:
        print(f"{number} is't not a prime number")


# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
