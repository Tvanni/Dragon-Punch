from input_manager import *

nivel = [1]

def scene_menu():
    esc = Keyboard().key_down(pygame.K_ESCAPE)
    input_light = Keyboard().key_down(pygame.K_j)
    input_medium = Keyboard().key_down(pygame.K_k)
    input_heavy = Keyboard().key_down(pygame.K_l)
    if esc:
        janela.close()
    if input_light or input_medium or input_heavy:
        scene[0] = fundo_lvl1

def scene_level_1():
    esc = Keyboard().key_down(pygame.K_ESCAPE)
    input_light = Keyboard().key_down(pygame.K_j)
    input_medium = Keyboard().key_down(pygame.K_k)
    input_heavy = Keyboard().key_down(pygame.K_l)
    if esc:
        scene[0] = fundo_menu
        nivel[0] = 1
    if input_light or input_medium or input_heavy:
        scene[0] = fundo_jogo

def scene_level_2():
    esc = Keyboard().key_down(pygame.K_ESCAPE)
    input_light = Keyboard().key_down(pygame.K_j)
    input_medium = Keyboard().key_down(pygame.K_k)
    input_heavy = Keyboard().key_down(pygame.K_l)
    if esc:
        scene[0] = fundo_menu
        nivel[0] = 1
    if input_light or input_medium or input_heavy:
        nivel[0] = 2
        scene[0] = fundo_jogo