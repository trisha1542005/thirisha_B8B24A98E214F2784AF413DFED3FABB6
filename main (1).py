def factorial(n):
  if (n == 1 or n == 0):
    return 1
  else:
    return (n * factorial(n - 1))


# Derive code
num = 5
print("number :", num)
print(" factorial :", factorial(num))