from math import*
#Write your code below this line 👇
not_prime = "It's not a prime numer"
prime = "It's a prime numer"
def prime_checker(number):
    if number == 1:
        return not_prime
    if number == 2 or number == 3:
        return prime
    if number % 2 == 0 or number % 3 == 0:
        return not_prime

    for i in range (5, floor(sqrt(number)),6):
        if(number % i == 0 or number % (i + 2) == 0):
            return not_prime

    return prime



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
result = prime_checker(number=n)
print(result)