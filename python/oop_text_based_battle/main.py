import os
from character import Hero, Enemy
from weapon import short_bow,iron_sword

hero = Hero(name = "Hero", health = 100)
hero.equip(iron_sword)
enemy = Enemy(name = "Enemy", health = 100, weapon = short_bow)

hero.health_bar.draw()
enemy.health_bar.draw()
input()
while hero.health != 0 and enemy.health != 0:
    os.system("clear")
    if enemy.health <= 50 and hero.health > 40 and hero.weapon == iron_sword:
        hero.drop()
    elif hero.health <= 40 and hero.weapon != iron_sword:
        hero.equip(iron_sword)
    hero.attack(enemy)
    enemy.attack(hero)

    ## CHANGE THIS MANUAL PRINTING TO DRAW
    # print(f"Health of {hero.name}: {hero.health}")
    # print(f"Health of {enemy.name}: {enemy.health}")
    hero.health_bar.draw()
    enemy.health_bar.draw()    
    input()
    
if hero.health == 0 and enemy.health == 0:
    print ("It is a draw!")
elif hero.health == 0:
    print(f"{enemy.name} win!")
elif enemy.health == 0:        
    print(f"{hero.name} win!")
