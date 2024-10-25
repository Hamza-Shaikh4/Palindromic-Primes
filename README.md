# Palindromic-Primes

Palindromic Primes Finder
This Python program identifies "palindromic primes"—prime numbers that read the same forwards and backwards—within a user-defined range. It uses the Sieve of Eratosthenes for efficient prime number generation, filtering for palindromic properties within the specified range.

Features

- Efficient Prime Generation: Uses the Sieve of Eratosthenes to identify primes up to a maximum value (max_num). This algorithm has a time complexity of O(nloglogn) and a space complexity of O(n), making it suitable for large inputs.
- Palindrome Check: Filters generated primes by converting each prime to a string and checking if it reads the same forwards and backwards.
- User-Defined Range: Allows users to specify min_num and max_num to control the search range for palindromic primes.

How It Works

1) Prime Generation: Initializes an array to mark each number's primality status, marking non-prime multiples of each prime starting from 2. This generates all primes up to max_num.
2) Palindrome Filtering: Converts each prime in the range to a string and checks if it’s a palindrome.
3) Result Output: Returns the list of palindromic primes, displaying the first and last three for easy viewing.

Example

- Enter a minimum number: 1
- Enter a maximum number: 10000000
-  Special numbers - [2, 3, 5, 7, 11, ... , 9981899, 9989899]
- First three palindromic primes: [2, 3, 5]
- Last three palindromic primes: [9980899, 9981899, 9989899]
- Number of special numbers - 781
- It took 0.9771080017089844 second(s) to complete


