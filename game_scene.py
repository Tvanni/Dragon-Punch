from input_manager import *

nivel = [1]

def scene_menu():
    if esc:
        janela.close()
    if input_light or input_medium or input_heavy:
        scene[0] = fundo_lvl1

def scene_level_1():
    if esc:
        scene[0] = fundo_menu
        nivel[0] = 1
    if input_light or input_medium or input_heavy:
        scene[0] = fundo_jogo