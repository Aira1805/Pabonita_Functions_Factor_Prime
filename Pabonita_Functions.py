
def find_smallest_factor(n):
    if n < 2:
        print("Invalid input. Enter a number greater than 2.")
        return

    for i in range(2, n):
        if n % i == 0:
            print(f"The smallest factor other than 1 for {n} is {i}.")
            return

    print(f"{n} is a prime number.")


def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)

    print(f"Prime numbers in the range {start} to {end}: {primes}")

try:
    choice = int(input("Select an option (1 for smallest factor, 2 for prime numbers in range): "))

    if choice == 1:
        num = int(input("Enter an integer >= 2: "))
        find_smallest_factor(num)
    elif choice == 2:
        start = int(input("Enter the starting range: "))
        end = int(input("Enter the ending range: "))
        find_primes_in_range(start, end)
    else:
        print("Invalid choice. Select 1 or 2.")

except ValueError:
    print("Invalid input. Enter a valid integer.")
