from globais import *

player_animation = [
    Animation("Assets_DP/Idle.png", 30, True), #0
    Animation("Assets_DP/Frente.png", 36, False), #1
    Animation("Assets_DP/Backward.png", 36, False), #2
    Animation("Assets_DP/Knee.png", 30, False), #3
    Animation("Assets_DP/Sweep.png", 30, False), #4
    Animation("Assets_DP/Shoryuken.png", 42, False), #5
    Animation("Assets_DP/Donkey.png", 48, False), #6
    Animation("Assets_DP/Fireball.png", 48, False), #7
    Animation("Assets_DP/Knockdown.png", 48, False), #8
    Animation("Assets_DP/Down.png", 1, True), #9
    Animation("Assets_DP/Damage.png", 24, False), #10
    Animation("Assets_DP/Block.png", 12, False), #11
    Animation("Assets_DP/Block_Stun.png", 1, True), #12
    Animation("Assets_DP/Dash.png", 30, False) #13
]

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