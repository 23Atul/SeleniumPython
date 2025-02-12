
# ----------------------- M U L T I P L E     I N H E R I T A N C E ---------------------

# 1. MULTIPLE INHERITANCE --> A class can inherit attributes and methods from more than one class.
# 2. Method Resolution Order (MRO) ---> Search is done first in current class, then search continues into parent classes in depth-first, left-right fashion without searching the same class twice.


# working in game dev company

class MoveCharacter:

    def move_fwd(self):
        print("Move forward 1 step")

    def move_bwd(self):
        print("Move backward 1 step")

    
class JumpCharacter:

    def jump_1level(self):
        print("Jump character 1 level")

    def jump_2level(self):
        print("Jump character 2 level")


class Pokemon(MoveCharacter, JumpCharacter):
    pass


p = Pokemon()
p.move_bwd()  # Move backward 1 step
p.jump_1level()  # Jump character 1 level

print(Pokemon.mro()) 
#[<class '__main__.Pokemon'>, <class '__main__.MoveCharacter'>, <class '__main__.JumpCharacter'>, <class 'object'>]


class Micky(JumpCharacter,MoveCharacter):
    pass

m = Micky()
m.move_fwd()  # Move forward 1 step
m.jump_2level()  # Jump character 2 level

print(Micky.mro())
# [<class '__main__.Micky'>, <class '__main__.JumpCharacter'>, <class '__main__.MoveCharacter'>, <class 'object'>]



# JumpCharacter        MoveCharacter
#         \             /
#          \           /
#           \         /
#            \       /
#             \     /
#              \   /
#             Pokemon