"""
Script for calculating the first ten digits of the sum of each number in digits.txt
"""

digits = open("digits.txt", "r")
elements = [int(x) for x in digits.readlines() if x != "\n"]
value = sum(elements)
print(str(value)[:10])
