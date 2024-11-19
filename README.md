Prime Number Checker and Goldbach Conjecture
This project is a Python script that checks the primality of numbers and verifies Goldbach's Conjecture for a given number. Goldbach's Conjecture states that every even integer greater than 2 is the sum of two prime numbers. The program also allows users to repeatedly test numbers based on their input.


Features
Check if a number is divisible by another:

The function is_divisible_by(number, divisor) checks whether a number is divisible by a given divisor.
Check if a number is prime:

The function is_prime(number) determines whether a given number is a prime number.
Find pairs of prime numbers that sum up to a given number:

The function is_sum_of_two_primes(number) returns pairs of prime numbers whose sum equals the input number.
Interactive functionality:

The script allows users to input multiple numbers to test, with the option to exit after each check.


How to Use
Prerequisites:

Ensure you have Python 3 installed on your system.
Running the Program:

Save the script in a file (e.g., prime_number_checker.py).
Run the script in your terminal:
bash
Code kopieren
python prime_number_checker.py
User Interaction:

Enter a number when prompted. The number must be greater than or equal to 2.
The program will:
Check if the number can be expressed as the sum of two prime numbers.
Display all valid pairs of prime numbers if applicable.
After processing, you'll be asked if you want to check another number:
Enter Y to check another number.
Enter N to exit the program.


Examples
Input:

Please enter the number you would like to check: 10
Output:
The number 10 equals to the sum of 3 and 7
The number 10 equals to the sum of 5 and 5

Input:
Please enter the number you would like to check: 9
The number 9 is not equal to the sum of two primes.


Code Structure
Functions
is_divisible_by(number, divisor)

Returns True if number is divisible by divisor, otherwise False.
is_prime(number)

Determines if a number is prime by checking divisors up to its square root.
is_sum_of_two_primes(number)

Finds all pairs of prime numbers whose sum equals the input number.
check_new_number()

Prompts the user to check another number or exit the program.
main()

Coordinates the program's logic and user interaction.


Limitations
This script assumes that the user inputs valid integers. Non-integer inputs will result in a prompt for correct input.
The script checks numbers starting from 2 and only works for numbers greater than or equal to 2.
Performance may decrease for large numbers due to prime-checking computations.


Future Improvements
Add a feature to handle very large numbers efficiently using advanced algorithms (e.g., Sieve of Eratosthenes).
Provide additional insights, such as listing all prime numbers below the given number.
Implement a graphical user interface (GUI) for user interaction.


License
This project is open-source and available for personal or educational use. You are free to modify and distribute the code with appropriate credit.
