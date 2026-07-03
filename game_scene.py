from input_manager import *

def scene_menu():
    if esc:
        janela.close()
    if input_light or input_medium or input_heavy:
        scene[0] = fundo_jogo

def scene_level_1():
    if esc:
        scene[0] = fundo_menu
    if input_light or input_medium or input_heavy:
        scene[0] = fundo_jogo