import pygame
from pygame.locals import *
import random
import sys

pygame.init()

# cores
branco = (255,255,255)
preto = (0,0,0)

# resolução
screen = pygame.display.set_mode((800,600)) 

# fonte
pygame.font.init()
font = pygame.font.SysFont('Arial', 50)
font_rb = pygame.font.SysFont('Arial', 50)

palavras = [
'Caneta', 'Mesa', 'Cadeira', 'Telefone', 'Relogio', 'Livro', 'Computador', 'Chave', 'Óculos', 'Copo',
'Carro', 'Bicicleta', 'Escova', 'Garfo', 'Tesoura', 'Faca', 'Colher', 'Escova de dentes', 'TV', 
'Martelo', 'Banana', 'Abacaxi', 'Morango', 'Pessego', 'Uva','Limao', 'Melancia', 'Laranja', 'Kiwi',
'Manga', 'Cereja', 'Melao', 'Pera', 'Abacate', 'Framboesa', 'Amora', 'Mirtilo', 'Coco', 'Goiaba'
'Cachorro', 'Gato', 'Elefante', 'Leao', 'Tigre', 'Girafa', 'Urso', 'Rato', 'Pássaro', 'Cavalo',
'Macaco', 'Cobra', 'Panda', 'Coelho', 'Galinha', 'Pato', 'Peixe', 'Tubarão', 'Baleia', 'Jacare'
]

palavra_gerada = ''
palavra_escondidinha = ''
final = True
chance = 10
letra = ''
click_last_status = False

'''
def forca(screen, chance):
    if chance == 9:
        pygame.draw.rect(screen, (preto), (100, 500, 200, 10))
        pygame.draw.rect(screen, (preto), (100, 100, 10, 400))
        pygame.draw.rect(screen, (preto), )
    if chance == 8:
        pygame.draw
    if chance == 7:
        pygame.draw
    if chance == 6:
        pygame.draw
    if chance == 5:
        pygame.draw
    if chance == 4:
        pygame.draw
    if chance == 3:
        pygame.draw
    if chance == 2:
        pygame.draw
    if chance == 1:
        pygame.draw
    if chance == 0:
        pygame.draw
'''
while True:
    for event in pygame.event.get():
        # evento de fechar o jogo
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        # evento de pressionar uma tecla
        if event.type == pygame.KEYDOWN:
            letra = str(pygame.key.name(event.key)).upper()
            print(letra) #teste
    
    #forca(screen, chance)
    pygame.draw.rect(screen, (branco), (100, 500, 200, 10))
    pygame.draw.rect(screen, (branco), (150, 100, 10, 400))
    
    
    pygame.display.update()