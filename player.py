from animações import *
from input_manager import *

class PlayerPedro():
    def __init__(self):
        self.animation_enum = AnimationEnum()
        self.actionable = True
        self.buffer = False
        self.flag = False
        self.player_state: list[Animation] = [None]
        self.posição = [(LARGURA_JANELA/2) - 100, ALTURA_JANELA - 200]

    def player_animate(self) -> None:

        if hasattr(self.player_state[0], "rodando"):
            if not self.player_state[0].rodando:
                if not input_left and not input_right:
                    self.player_state[0] = player_animation[self.animation_enum.IDLE]
                    self.actionable = True
                if input_right and not input_left:
                    self.player_state[0] = player_animation[self.animation_enum.FORWARD]
                    self.actionable = True
                if input_left and not input_right:
                    self.player_state[0] = player_animation[self.animation_enum.BACKWARD]
                    self.actionable = True
                if input_left and input_right:
                    self.player_state[0] = player_animation[self.animation_enum.IDLE]
                    self.actionable = True
                    self.buffer = True
                

        if hasattr(self.player_state[0], "set_position"):
            self.player_state[0].set_position(self.player_posição[0], self.player_posição[1])

        if hasattr(self.player_state[0], "update"):
            self.player_state[0].update()



    def player_input_handler(self) -> None:

        if scene[0] == fundo_jogo:
            if input_down and input_light and self.actionable:
                self.player_state[0] = player_animation[self.animation_enum.SWEEP]
                self.actionable = False
                self.flag = False

            if input_just_right or input_just_left:
                self.buffer = True

            if input_right and not input_left and self.actionable:
                if input_just_right or self.buffer:
                    self.player_state[0] = player_animation[self.animation_enum.FORWARD]
                    self.buffer = False
                self.player_posição[0] += 300 * Window.get_instance().delta_time()
                self.flag = False
            
            if input_left and not input_right and self.actionable:
                if input_just_left or self.buffer:
                    self.player_state[0] = player_animation[self.animation_enum.BACKWARD]
                    self.buffer = False
                self.player_posição[0] -= 300 * Window.get_instance().delta_time()
                self.flag = False

            if not input_left and not input_right:
                if self.actionable and not self.flag:
                    self.player_state[0] = player_animation[self.animation_enum.IDLE]
                    self.flag = True
                if not self.actionable:
                    self.buffer = False

            if input_left and input_right and self.actionable and not self.flag:
                self.player_state[0] = player_animation[self.animation_enum.IDLE]
                self.flag = True
                self.buffer = True

