import re

while True:
    coordinate = input()
    if re.match("^[a-j]([1-9]|10)$", coordinate):
        print("match!!!!")
    else:
        print("don't match (((")