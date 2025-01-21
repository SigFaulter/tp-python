import unittest
from src.math_operations import add, subtract, multiply, divide
from src.string_operations import concatenate, to_uppercase
from tests.test_math_operations import TestMathOps

print("Execution des tests")
unittest.main(module="tests.test_math_operations", exit=False)

print("\nTest des operations test_math_operationsmatiques :")
print("Addition : ", add(5, 3))
print("Soustraction : ", subtract(10, 7))
print("Multiplication : ", multiply(4, 6))

try:
    print("Division : ", divide(8, 2))
except ValueError as e:
    print("Erreur : ", e)

print("\nTest des operations sur les chaines : ")
print("Concatenation :", concatenate("Bonjour", " test"))
print("Majuscules :", to_uppercase("hey"))

