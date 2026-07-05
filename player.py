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
        esc = Keyboard().key_down(pygame.K_ESCAPE)

        input_just_right = Keyboard().key_down(pygame.K_d)
        input_just_left = Keyboard().key_down(pygame.K_a)
        input_just_down = Keyboard().key_down(pygame.K_s)
        input_just_up = Keyboard().key_down(pygame.K_w)

        input_right = Keyboard().key_pressed(pygame.K_d)
        input_left = Keyboard().key_pressed(pygame.K_a)
        input_down = Keyboard().key_pressed(pygame.K_s)
        input_up = Keyboard().key_pressed(pygame.K_w)

        input_light = Keyboard().key_down(pygame.K_j)
        input_medium = Keyboard().key_down(pygame.K_k)
        input_heavy = Keyboard().key_down(pygame.K_l)
        input_dash = Keyboard().key_pressed(pygame.K_SPACE)

        if hasattr(self.player_state[0], "rodando"):
            if not self.player_state[0].rodando:
                if not input_left and not input_right:
                    idle = novo_animação(player_animation[self.animation_enum.IDLE])
                    self.player_state[0] = idle
                    self.actionable = True
                if input_right and not input_left:
                    forward = novo_animação(player_animation[self.animation_enum.FORWARD])
                    self.player_state[0] = forward
                    self.actionable = True
                if input_left and not input_right:
                    backward = novo_animação(player_animation[self.animation_enum.BACKWARD])
                    self.player_state[0] = backward
                    self.actionable = True
                if input_left and input_right:
                    idle = novo_animação(player_animation[self.animation_enum.IDLE])
                    self.player_state[0] = idle
                    self.actionable = True
                    self.buffer = True
                

        if hasattr(self.player_state[0], "set_position"):
            self.player_state[0].set_position(self.posição[0], self.posição[1])

        if hasattr(self.player_state[0], "update"):
            self.player_state[0].update()



    def player_input_handler(self) -> None:
        esc = Keyboard().key_down(pygame.K_ESCAPE)

        input_just_right = Keyboard().key_down(pygame.K_d)
        input_just_left = Keyboard().key_down(pygame.K_a)
        input_just_down = Keyboard().key_down(pygame.K_s)
        input_just_up = Keyboard().key_down(pygame.K_w)

        input_right = Keyboard().key_pressed(pygame.K_d)
        input_left = Keyboard().key_pressed(pygame.K_a)
        input_down = Keyboard().key_pressed(pygame.K_s)
        input_up = Keyboard().key_pressed(pygame.K_w)

        input_light = Keyboard().key_down(pygame.K_j)
        input_medium = Keyboard().key_down(pygame.K_k)
        input_heavy = Keyboard().key_down(pygame.K_l)
        input_dash = Keyboard().key_pressed(pygame.K_SPACE)

        if scene[0] == fundo_jogo:
            if input_down and input_light and self.actionable:
                sweep = novo_animação(player_animation[self.animation_enum.SWEEP])
                self.player_state[0] = sweep
                self.actionable = False
                self.flag = False

            if input_just_right or input_just_left:
                self.buffer = True

            if input_right and not input_left and self.actionable:
                if input_just_right or self.buffer:
                    forward = novo_animação(player_animation[self.animation_enum.FORWARD])
                    self.player_state[0] = forward
                    self.buffer = False
                self.posição[0] += 300 * Window.get_instance().delta_time()
                self.flag = False
            
            if input_left and not input_right and self.actionable:
                if input_just_left or self.buffer:
                    backward = novo_animação(player_animation[self.animation_enum.BACKWARD])
                    self.player_state[0] = backward
                    self.buffer = False
                self.posição[0] -= 300 * Window.get_instance().delta_time()
                self.flag = False

            if not input_left and not input_right:
                if self.actionable and not self.flag:
                    idle = novo_animação(player_animation[self.animation_enum.IDLE])
                    self.player_state[0] = idle
                    self.flag = True
                if not self.actionable:
                    self.buffer = False

            if input_left and input_right and self.actionable and not self.flag:
                idle = novo_animação(player_animation[self.animation_enum.IDLE])
                self.player_state[0] = idle
                self.flag = True
                self.buffer = True

