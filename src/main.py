from dashboard import Dashboard
from battlemap import BattleMap

input("Press ENTER to start he game...")

username = input("Enter User1's name: ")
user1 = Dashboard(username)
username = input("Enter User2's name: ")
user2 = Dashboard(username)

print("{name}'s turn." .format(name=user1.username))
print("Start ship positioning.")

user1.myMap.disposition_of_all_ships()

print("{name}, you ships are disposed." .format(name=user1.username))

print("{name}'s turn." .format(name=user2.username))
print("Start ship positioning.")

user2.myMap.disposition_of_all_ships()

print("{name}, you ships are disposed." .format(name=user2.username))

print("End of input")


print("{name} shoots." .format(name=user1.username))

user1.shoot(user2, C)
