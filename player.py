from animações import *
from input_manager import *

class PlayerPedro():
    def __init__(self):
        self.animation_enum = AnimationEnum()
        self.actionable = True
        self.buffer = True
        self.player_state: list[Animation] = [None]
        self.posição = [(LARGURA_JANELA/2) - 100, ALTURA_JANELA - 200]

    def player_animate(self) -> None:

        if hasattr(self.player_state[0], "rodando"):
            if not self.player_state[0].rodando:
                if not input_left and not input_right:
                    self.animation_enum.state = 0
                    self.player_state[0] = player_animation[self.animation_enum.state]
                    self.actionable = True
                if input_right and not input_left:
                    player_drlevis = Animation("Assets_Footsies/FrenteGIGA.png", 6, False)
                    self.player_state[0] = player_drlevis
                    self.actionable = True
                if input_left and not input_right:
                    player_klevis = Animation("Assets_Footsies/BackwardGIGA.png", 6, False)
                    self.player_state[0] = player_klevis
                    self.actionable = True
                if input_left and input_right:
                    player_alevis = Animation("Assets_Footsies/IdleGIGA.png", 5, False)
                    self.player_state[0] = player_alevis
                    self.actionable = True
                    self.buffer = True
                

        if hasattr(player_state[0], "set_position"):
            player_state[0].set_position(player_posição[0], player_posição[1])

        if hasattr(player_state[0], "update"):
            player_state[0].update()



    def player_input_handler() -> None:

        if scene[0] == fundo_jogo:
            if input_down and input_heavy and player_actionable[0]:
                player_sweep = Animation("Assets_Footsies/SweepGIGA.png", 5, False)
                player_state[0] = player_sweep
                player_actionable[0] = False
                flag[0] = False

            if input_just_right or input_just_left:
                buffer[0] = True

            if input_right and not input_left and player_actionable[0]:
                if input_just_right or buffer[0]:
                    player_forward = Animation("Assets_Footsies/FrenteGIGA.png", 6, True)
                    player_state[0] = player_forward
                    buffer[0] = False
                player_posição[0] += 300 * Window.get_instance().delta_time()
                flag[0] = False
            
            if input_left and not input_right and player_actionable[0]:
                if input_just_left or buffer[0]:
                    player_backward = Animation("Assets_Footsies/BackwardGIGA.png", 6, True)
                    player_state[0] = player_backward
                    buffer[0] = False
                player_posição[0] -= 300 * Window.get_instance().delta_time()
                flag[0] = False

            if not input_left and not input_right:
                if player_actionable[0] and not flag[0]:
                    player_blevis = Animation("Assets_Footsies/IdleGIGA.png", 5, True)
                    player_state[0] = player_blevis
                    flag[0] = True
                if not player_actionable[0]:
                    buffer[0] = False

            if input_left and input_right and player_actionable[0] and not flag[0]:
                player_blevis = Animation("Assets_Footsies/IdleGIGA.png", 5, True)
                player_state[0] = player_blevis
                flag[0] = True
                buffer[0] = True

