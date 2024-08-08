def prime_factors(n):
    """Return the prime factors of the given number."""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def format_factors(numbers):
    """Format the factors for each number in the set in the specified output format."""
    for n in numbers:
        factors = prime_factors(n)
        if factors:
            formatted_output = f"{n}=" + '*'.join(map(str, factors))
            print(formatted_output)
        else:
            print(f"{n} is a prime number and has no factors other than 1 and itself.")


numbers = {784, 658, 63, 350, 784, 364, 147, 532, 49, 63, 56, 126}
format_factors(numbers)
