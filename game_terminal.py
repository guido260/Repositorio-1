import random
import os

animal = {'Cachorro', 'Gato', 'Elefante', 'Leao', 'Tigre', 'Girafa', 'Urso', 'Rato', 'Pássaro', 'Cavalo',
          'Macaco', 'Cobra', 'Panda', 'Coelho', 'Galinha', 'Pato', 'Peixe', 'Tubarão', 'Baleia', 'Jacare'}

fruta = {'Banana', 'Abacaxi', 'Morango', 'Pessego', 'Uva', 'Limao', 'Melancia', 'Laranja', 'Kiwi',
         'Manga', 'Cereja', 'Melao', 'Pera', 'Abacate', 'Framboesa', 'Amora', 'Mirtilo', 'Coco', 'Goiaba'}

objeto = {'Caneta', 'Mesa', 'Cadeira', 'Telefone', 'Relogio', 'Livro', 'Computador', 'Chave', 'Óculos', 'Copo',
          'Carro', 'Bicicleta', 'Escova', 'Garfo', 'Tesoura', 'Faca', 'Colher', 'Escova de dentes', 'TV', 'Martelo'}

forca = ['''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
      |
      |
      |
      |
      |
=========''','''
 
  
      
      
      
      
      
=========''', ' ']

class LetraRepetidaException(Exception):
    pass

def jogar():
    palavra = random.choice(list(animal | fruta | objeto)).upper()
    letras_usuario = []
    chances = 10
    ganhou = False
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'.upper()
    t = 1

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        for letra in palavra:
            if letra in letras_usuario:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        print(f'\nVocê tem {chances} chances')
        print(forca[len(forca) - t])
        print(f'\n letras usadas: {letras_usuario}')
        
        try:
            tentativa = input('Escolha uma letra para adivinhar: ').upper()
            
            if tentativa in letras_usuario or tentativa not in alfabeto:
                raise LetraRepetidaException('Erro')
            
            letras_usuario.append(tentativa)
            
            if tentativa not in palavra:
                chances -= 1
                t += 1

            ganhou = True
            for letra in palavra:
                if letra not in letras_usuario:
                    ganhou = False
        
        except LetraRepetidaException as e:
            print(e)
            input('Pressione Enter para continuar...')

        if chances == 0 or ganhou:
            break

    if ganhou:
        print(f'Parabéns! A palavra era: {palavra}')
    else:
        print(f'Você perdeu! A palavra era: {palavra}')

while True:
    jogar()
    novamente = input('Deseja jogar novamente? ("s" para sair, qualquer outra tecla para continuar): ').upper()
    if novamente == 'S':
        break