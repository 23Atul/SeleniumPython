
#------------------- M U L T I L E V E L       I N H E R I T A N C E ----------------------

# 1. MULTILEVEL INHERITANCE --->  A class 


class MoveCharacter:   # base class

    def move_fwd(self):
        print("Move forward 1 step")

    def move_bwd(self):
        print("Move backward 1 step")


class JumpCharacter(MoveCharacter):  # 1st level inheritance
 
    def jump_1level(self):
        print("Jump character 1 level")

    def jump_2level(self):
        print("Jump character 2 level")


class Pokemon(JumpCharacter):   # 2nd level inheritance
    pass


p = Pokemon()
p.move_bwd()  # Move backward 1 step
p.jump_1level()  # Jump character 1 level

print(Pokemon.mro())
# [<class '__main__.Pokemon'>, <class '__main__.JumpCharacter'>, <class '__main__.MoveCharacter'>, <class 'object'>]


# MoveCharacter
#     |
#     |
#    \|/
# JumpCharacter
#     |
#     |
#    \|/
#  Pokemon