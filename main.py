from globais import *
from player import *
from hud import *
from game_scene import *

##Configs Iniciais
scene[0] = fundo_menu
pedro = PlayerPedro()
pedro.player_state[0] = player_animation[pedro.animation_enum.state]

while True:

    if scene[0] == fundo_menu:
        scene_menu()
    
    if scene[0] == fundo_lvl1:
        scene_level_1()

    if scene[0] == fundo_lvl2:
        scene_level_2()

    if scene[0] == fundo_jogo:
        pedro.player_input_handler()
        pedro.player_animate()


    ##DESENHA
    scene[0].draw()

    if scene[0] == fundo_jogo:
        pedro.player_state[0].draw()


    janela.update()
