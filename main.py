from World import World
from Player import Player
from Items import Items

items = [Items("club", "melee", 1, 0, 1), Items("dagger", "melee", 3, 0, 4),
         Items("greatclub", "melee", 5, 0, 12), Items("handaxe", "melee", 8, 0, 18),
         Items("greatsword", "melee", 12, 0, 25), Items("Maul", "melee", 9, 0, 20),
         Items("woodshield", "melee", 0, 2, 5), Items("metalshield", "melee", 0, 5, 13),
         Items("ironshield", "melee", 0, 9, 25), Items("steelshield", "melee", 0, 15, 40)
         ]

t = Player("name", 1, 0, [5, 5])

world = World(t)

world.menu()
