import time

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)  # initially sets every value to true up to max number
    primes[0], primes[1] = False, False  #sets 1 and 0 to false as they are not primes
    p = 2
    while p * p <= n: # go up to the square root of max number
        if primes[p]:
            for i in range(p * p, n + 1, 2 * p):  # mark all multiples of p and starts from p * p as all previous ones will be marked off
                primes[i] = False # the multiples of p are set to false and marked to not prime
        p += 1
    return [2] + [i for i in range(3, n + 1, 2) if primes[i]] #

def is_palindrome(num):
    return str(num) == str(num)[::-1] # checks if the number is equal to the reverse of the number

def find_palindromic_primes(min_num, max_num):
    start_time = time.time() # start the timer

    primes = sieve_of_eratosthenes(max_num) # calls prime function
    special_num = [] # list for storing special numbers found

    for prime in primes:
        if prime < min_num: # validation check to make sure it is less than the minimum
            continue

        if is_palindrome(prime): # checks if the prime numbers are also palindromes
            special_num.append(prime) # add to list of special numbers

    return special_num, start_time

min_num = int(input("Enter a minimum number: ")) # minimum number input
max_num = int(input("Enter a maximum number: ")) # maximum number input


if max_num - min_num > 10 ** 12:
    print("The range is too large.") # make sure number entered is not over a trillion

special_num , start_time = find_palindromic_primes(min_num, max_num) # access variables
first_three_primes = special_num[:3]
last_three_primes = special_num[-3:]

# Display Results
if max_num > min_num:
    if len(special_num) < 6:
        print(f"The special numbers are {special_num}") # prints all numbers if less then 6
    else:
        print(f"Special numbers - {special_num}") # prints all special numbers found
        print(f"First three palindromic primes: {first_three_primes}") # first 3 special numbers
        print(f"Last three palindromic primes: {last_three_primes}") # last 3 special numbers
else:
    print("Invalid input") # if the minimum is less than the maximum it displays 'invalid input'


print(f"Number of special numbers - {len(special_num)}") # counts the total number of special numbers found between the min and max range

end_time = time.time()
time_taken = end_time - start_time # calculates final time
print(f"It took {time_taken} second(s) to complete") # shows final time in seconds
