import pygame
import sys
import time
from pygame.locals import *
import random
# Inicializa o Pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Forca")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)

# Fonte
FONTE = pygame.font.SysFont('comicsans', 40)
FONTE_PEQUENA = pygame.font.SysFont('comicsans', 30)

# Palavra para adivinhar
aleatório = {'Caneta', 'Mesa', 'Cadeira', 'Telefone', 'Relogio', 'Livro', 'Computador', 'Chave', 'Óculos', 'Copo',
          'Carro', 'Bicicleta', 'Escova', 'Garfo', 'Tesoura', 'Faca', 'Colher', 'Escova de dentes', 'TV', 'Martelo', 'Banana', 'Abacaxi', 'Morango', 'Pessego', 'Uva', 'Limao', 'Melancia', 'Laranja', 'Kiwi',
         'Manga', 'Cereja', 'Melao', 'Pera', 'Abacate', 'Framboesa', 'Amora', 'Mirtilo', 'Coco', 'Goiaba', 'Cachorro', 'Gato', 'Elefante', 'Leao', 'Tigre', 'Girafa', 'Urso', 'Rato', 'Pássaro', 'Cavalo',
          'Macaco', 'Cobra', 'Panda', 'Coelho', 'Galinha', 'Pato', 'Peixe', 'Tubarão', 'Baleia', 'Jacare'}

palavra = random.choice(list(aleatório)).upper()
letras_palavra = set(palavra)
letras_usadas = set()
tentativas = 10
jogo_terminado = False

# Função para desenhar a forca e o boneco
def desenha_forca(tentativas_restantes):

    if tentativas_restantes <= 9:
        pygame.draw.rect(TELA, PRETO, (150, 500, 200, 20))  # base

    if tentativas_restantes <= 8:
        pygame.draw.line(TELA, PRETO, (250, 500), (250, 100), 7)  # poste vertical
        pygame.draw.line(TELA, PRETO, (400, 100), (400, 150), 7)  # corda
        pygame.draw.line(TELA, PRETO, (250, 100), (400, 100), 7)  # poste horizontal

    if tentativas_restantes <= 7:
        pygame.draw.circle(TELA, PRETO, (400, 180), 30, 5)  # cabeça
    if tentativas_restantes <= 6:
        pygame.draw.line(TELA, PRETO, (385, 170), (395, 180), 3)  # olho direito
        pygame.draw.line(TELA, PRETO, (395, 170), (385, 180), 3)  # olho direito

    if tentativas_restantes <= 5:
        pygame.draw.line(TELA, PRETO, (405, 170), (415, 180), 3)  # olho esquerdo
        pygame.draw.line(TELA, PRETO, (415, 170), (405, 180), 3)  # olho esquerdo

    if tentativas_restantes <= 4:
        pygame.draw.line(TELA, PRETO, (400, 210), (400, 320), 5)  # tronco

    if tentativas_restantes <= 3:
        pygame.draw.line(TELA, PRETO, (400, 240), (350, 300), 5)  # braço direito

    if tentativas_restantes <= 2:
        pygame.draw.line(TELA, PRETO, (400, 240), (450, 300), 5)  # braço esquerdo

    if tentativas_restantes <= 1:
        pygame.draw.line(TELA, PRETO, (400, 320), (350, 380), 5) # perna direita
    
    if tentativas_restantes <= 0:
        pygame.draw.line(TELA, PRETO, (400, 320), (450, 380), 5) # perna esquerda


    

# Função para desenhar a tela principal do jogo
def desenha_tela():
    TELA.fill(BRANCO)
    
    # Desenha as letras já usadas
    texto_letras_usadas = " ".join(letras_usadas)
    rotulo_letras_usadas = FONTE_PEQUENA.render(f"Letras usadas: {texto_letras_usadas}", 1, PRETO)
    TELA.blit(rotulo_letras_usadas, (20, 20))

    # Desenha a palavra com as letras descobertas
    palavra_exibida = [letra if letra in letras_usadas else "_" for letra in palavra]
    rotulo_palavra = FONTE.render(" ".join(palavra_exibida), 1, PRETO)
    TELA.blit(rotulo_palavra, (LARGURA // 2 - rotulo_palavra.get_width() // 2, ALTURA - 100))

    # Desenha as tentativas restantes
    rotulo_tentativas = FONTE_PEQUENA.render(f"Tentativas restantes: {tentativas}", 1, PRETO)
    TELA.blit(rotulo_tentativas, (20, 60))

    # Desenha a forca e o boneco
    desenha_forca(tentativas)

    pygame.display.update()

# Função para desenhar a tela final
def desenha_tela_final(mensagem, cor):
    TELA.fill(BRANCO)
    rotulo_final = FONTE.render(mensagem, 1, cor)
    TELA.blit(rotulo_final, (LARGURA // 2 - rotulo_final.get_width() // 2, 200))

    rotulo_reiniciar = FONTE_PEQUENA.render("Pressione 'R' para reiniciar", 1, PRETO)
    TELA.blit(rotulo_reiniciar, (LARGURA // 2 - rotulo_reiniciar.get_width() // 2, 300))

    pygame.display.update()

# Função para reiniciar o jogo
def reiniciar_jogo():
    global letras_palavra, letras_usadas, tentativas, jogo_terminado
    letras_palavra = set(palavra)
    letras_usadas = set()
    tentativas = 10
    jogo_terminado = False

# Configurações do relógio
relogio = pygame.time.Clock()
executando = True
mensagem_erro = ""
tempo_erro = 0

while executando:
    relogio.tick(60)
    if jogo_terminado:
        if tentativas == 0:
            desenha_tela_final("Você perdeu! Tente novamente.", VERMELHO)
        else:
            desenha_tela_final("Parabéns! Você ganhou!", VERDE)

        for evento in pygame.event.get():
            if evento.type == QUIT:
                executando = False
            if evento.type == KEYDOWN:
                if evento.key == K_r:
                    reiniciar_jogo()

    else:
        desenha_tela()
        if mensagem_erro and time.time() - tempo_erro > 3:
            mensagem_erro = ""

        for evento in pygame.event.get():
            if evento.type == QUIT:
                executando = False
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:
                    executando = False
                if evento.unicode.isalpha():
                    letra = evento.unicode.upper()
                    if letra in letras_usadas:
                        mensagem_erro = f"A letra {letra} já foi usada."
                        tempo_erro = time.time()
                    elif letra in letras_palavra:
                        letras_usadas.add(letra)
                        letras_palavra.remove(letra)
                        if len(letras_palavra) == 0:
                            jogo_terminado = True
                    else:
                        letras_usadas.add(letra)
                        tentativas -= 1
                        if tentativas == 0:
                            jogo_terminado = True
                else:
                    mensagem_erro = "Digite apenas letras."
                    tempo_erro = time.time()

        if mensagem_erro:
            rotulo_erro = FONTE_PEQUENA.render(mensagem_erro, 1, VERMELHO)
            TELA.blit(rotulo_erro, (20, 100))
            pygame.display.update()

pygame.quit()
sys.exit()
