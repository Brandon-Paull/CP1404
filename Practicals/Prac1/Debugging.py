"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
if score in range(0, 50):# TODO Only counts integers not floats
    print("Bad")
elif score in range(50, 90):
    print("Pass")
elif score in range(90, 101):
    print("Excellent")
else:
    print("Invalid score")
