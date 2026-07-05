from globais import *

player_animation = [
    ("Assets_DP/Idle.png", 6, 5, True), #0
    ("Assets_DP/Frente.png", 6, 6, False), #1
    ("Assets_DP/Backward.png", 6, 6, False), #2
    ("Assets_DP/Knee.png", 6, 5, False), #3
    ("Assets_DP/Sweep.png", 6, 5, False), #4
    ("Assets_DP/Shoryuken.png", 6, 7, False), #5
    ("Assets_DP/Donkey.png", 6, 8, False), #6
    ("Assets_DP/Fireball.png", 6, 8, False), #7
    ("Assets_DP/Knockdown.png", 6, 8, False), #8
    ("Assets_DP/Down.png", 1, 1, True), #9
    ("Assets_DP/Damage.png", 6, 4, False), #10
    ("Assets_DP/Block.png", 6, 2, False), #11
    ("Assets_DP/Block_Stun.png", 1, 1, True), #12
    ("Assets_DP/Dash.png", 6, 5, False) #13
]

def novo_animação(tupla) -> Animation:
    animation_nova = Animation(tupla[0],tupla[1],tupla[2], tupla[3])
    return animation_nova

    

class AnimationEnum():


    IDLE = 0
    FORWARD = 1
    BACKWARD = 2

    KNEE = 3
    SWEEP = 4
    SHORYUKEN = 5
    DONKEY = 6
    FIREBALL = 7
    
    KNOCKDOWN = 8
    DOWN = 9
    DAMAGE = 10
    BLOCK = 11
    BLOCK_STUN = 12
    DASH = 13

    def __init__(self):
        self.state = 0