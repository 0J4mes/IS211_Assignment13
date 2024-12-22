# Part I: Implement the Fibonacci Sequence
def fibonacci(n):
    """Calculate the nth Fibonacci number using recursion."""
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    elif n == 1:
        return 0  # Base case: F1 = 0
    elif n == 2:
        return 1  # Base case: F2 = 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Part II: Implement Euclid's GCD Algorithm
def gcd(a, b):
    """Find the greatest common divisor of two integers using recursion."""
    if b == 0:
        return a  # Base case: GCD(a, 0) = a
    else:
        return gcd(b, a % b)

# Part III: String Comparison
def compareTo(s1, s2):
    """Compare two strings lexicographically using recursion."""
    # Base cases
    if not s1 and not s2:  # Both strings are empty
        return 0
    if not s1:  # s1 is empty but s2 is not
        return -1
    if not s2:  # s2 is empty but s1 is not
        return 1

    # Compare the first characters of both strings
    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])  # Difference in ASCII values
    else:
        return compareTo(s1[1:], s2[1:])  # Compare the remaining substrings
