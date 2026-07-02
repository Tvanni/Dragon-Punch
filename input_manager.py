from globais import *

def player_input() -> None:
    global esc
    esc = Keyboard().key_down(pygame.K_ESCAPE)


    global input_just_right
    input_just_right = Keyboard().key_down(pygame.K_d)
    global input_just_left
    input_just_left = Keyboard().key_down(pygame.K_a)
    global input_just_down
    input_just_down = Keyboard().key_down(pygame.K_s)
    global input_just_up
    input_just_up = Keyboard().key_down(pygame.K_w)


    global input_right
    input_right = Keyboard().key_pressed(pygame.K_d)

    global input_left
    input_left = Keyboard().key_pressed(pygame.K_a)

    global input_down
    input_down = Keyboard().key_pressed(pygame.K_s)

    global input_up
    input_up = Keyboard().key_pressed(pygame.K_w)

    global input_light
    input_light = Keyboard().key_down(pygame.K_j)

    global input_medium
    input_medium = Keyboard().key_down(pygame.K_k)

    global input_heavy
    input_heavy = Keyboard().key_down(pygame.K_l)
    
    global input_x
    input_x = Keyboard().key_pressed(pygame.K_x)