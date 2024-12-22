from recursion import fibonacci, gcd, compareTo

# Test Fibonacci
print("Fibonacci Tests:")
print(f"Fibonacci(1): {fibonacci(1)}")  # Should return 0
print(f"Fibonacci(5): {fibonacci(5)}")  # Should return 3
print(f"Fibonacci(10): {fibonacci(10)}")  # Should return 34

# Test GCD
print("\nGCD Tests:")
print(f"GCD(48, 18): {gcd(48, 18)}")  # Should return 6
print(f"GCD(100, 25): {gcd(100, 25)}")  # Should return 25
print(f"GCD(7, 13): {gcd(7, 13)}")  # Should return 1

# Test String Comparison
print("\nString Comparison Tests:")
print(f"compareTo('apple', 'banana'): {compareTo('apple', 'banana')}")  # Should return negative
print(f"compareTo('banana', 'apple'): {compareTo('banana', 'apple')}")  # Should return positive
print(f"compareTo('apple', 'apple'): {compareTo('apple', 'apple')}")  # Should return 0
