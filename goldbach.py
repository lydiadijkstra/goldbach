
def is_divisible_by(number, divisor): #checks if number equals int when devided
    """
    Check for the given number if the number is divisible
    :return: True or False
    """
    return number % divisor == 0


def is_prime(number):
    """
    Check if a number is prime.
    :param number: the number to check
    :return: True if the number is prime, otherwise False
    """
    for i in range(2, int(number ** 0.5) + 1):
        if is_divisible_by(number, i):
            return False
    return True


def is_sum_of_two_primes(number):
    """
    check if there are 2 prime numbers of which its sum is an even number
    :param number: primenumbers
    :return: goldbach theory
    """
    list_of_primes = []
    for i in range(2, number):
        if is_prime(i):
            j = number - i
            if is_prime(j):
                if j < i:
                    continue
                list_of_primes.append((i, j))
    return number, list_of_primes


def check_new_number():
    """
    Asks the user if he/she would like to check another number
    :return: boolean for check another number, or not
    """
    while True:
        check_another_number = input("Do you want to check another number? (Y/N) ")
        if check_another_number.lower() == "n":
            print("Ok, bye.")
            return False
        elif check_another_number.lower() == "y":
            return True
        print("Invalid input! Please enter Y for yes or N for no")


def main():
    """
    calling the operator functions and asing for user input
    :return: print answer
    """
    while True:
        try:
            number = int(input("Please enter the number you would like to check: "))
            if number <= 1:
                print("Invalid number, the number should be at least 2.")
                continue
            number, list_of_primes = is_sum_of_two_primes(number)
            if list_of_primes:
                for prime_pairs in list_of_primes:
                    print(f"The number {number} equals to the sum of {prime_pairs[0]} and {prime_pairs[1]}")
            print(f"The number {number} is not equal to the sum of two primes.")
        except ValueError:
            print("Invalid input, please enter a positive integer")
            continue
        if not check_new_number():
            break


if __name__ == "__main__":
    main()

