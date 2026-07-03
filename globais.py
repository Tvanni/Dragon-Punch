from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.animation import *

LARGURA_JANELA, ALTURA_JANELA = 720, 480

janela = Window(LARGURA_JANELA,ALTURA_JANELA,"DRAGON PUNCH!")

fundo_menu = GameImage("Start1.png")
fundo_lvl1 = GameImage("TelaVermelho.png")
fundo_lvl2 = GameImage("TelaAzul.png")
fundo_jogo = GameImage("AkumaUpscale.png")
fundo_jogo.set_position(-416, -420)

scene: list[GameImage] = [None]
global nivel
nivel = 0


player_state: list[Animation] = [None]
player_posição = [(LARGURA_JANELA/2) - 100, ALTURA_JANELA - 200]

player_actionable = [True]
flag = [False]
buffer = [False]

def set_position_center(eu, x_recebido=(LARGURA_JANELA/2), y_recebido=0):
    ##Posição Relativa, aceita input traduzido para Y sendo a parte inferior da tela,
    # e X movendo o centro do player.
    eu.x = x_recebido - (eu.width/2)
    eu.y = ALTURA_JANELA - (y_recebido + eu.height)
    return
    
def get_position_relativa(eu):
    x_relativo = eu.x + (eu.width/2)
    y_relativo = 1280 - (eu.y + eu.height)
    return x_relativo, y_relativo