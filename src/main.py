from dashboard import Dashboard
from battlemap import BattleMap
from cell import Cell

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

shooting_user = user1
target_user = user2

while True:
    print("{name} shoots." .format(name=shooting_user.username))
    print("Choose target.")
    target_cell = Cell.cell_input()
    change_turn = shooting_user.shoot(target_user, target_cell)
    if shooting_user.rivalMap.ship_counter == target_user.myMap.ship_counter:
        print("{name} wins. Perfect victory!!!" .format(name=shooting_user.username))
        break
    else:
        if change_turn:
            shooting_user, target_user = target_user, shooting_user