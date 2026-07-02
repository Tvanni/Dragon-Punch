from globais import *

player_animation = [
    Animation("Assets_DP/Idle.png", 5, True), #0
    Animation("Assets_DP/Frente.png", 6, False), #1
    Animation("Assets_DP/Backward.png", 6, False), #2
    Animation("Assets_DP/Dash.png", 5, False), #3
    Animation("Assets_DP/Back_Dash.png", 4, False), #4
    Animation("Assets_DP/Knee.png", 5, False), #5
    Animation("Assets_DP/Sweep.png", 5, False), #6
    Animation("Assets_DP/Shoryuken.png", 7, False), #7
    Animation("Assets_DP/Donkey.png", 8, False), #8
    Animation("Assets_DP/Fireball.png", 8, False), #9
    Animation("Assets_DP/Knockdown.png", 8, False), #10
    Animation("Assets_DP/Down.png", 1, True), #11
    Animation("Assets_DP/Wake_Up.png", 8, False), #12
    Animation("Assets_DP/Damage.png", 4, False), #13
    Animation("Assets_DP/Block.png", 2, False), #14
    Animation("Assets_DP/Block_Stun.png", 1, True) #15
]

class AnimationEnum():


    IDLE = 0
    FORWARD = 1
    BACKWARD = 2
    DASH = 3
    BACKDASH = 4

    KNEE = 5
    SWEEP = 6
    SHORYUKEN = 7
    DONKEY = 8
    FIREBALL = 9
    
    KNOCKDOWN = 10
    DOWN = 11
    WAKEUP = 12
    DAMAGE = 13
    BLOCK = 14
    BLOCK_STUN = 15

    def __init__(self):
        self.state = 0