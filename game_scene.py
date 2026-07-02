from input_manager import *

def scene_menu():
    if esc:
        janela.close()
    if input_light or input_medium or input_heavy:
        scene[0] = fundo_jogo

