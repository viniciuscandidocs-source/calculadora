'''Um JoKenPo que nao tem regras, onde a criatividade pode extravasar entre você e o jogador 2. Qualquer coisa pode ser digitada,
enquanto o programa seleciona aleatoriamente quem será o vencedor, o que pode acontecer coisas engraçadas como um graveto vencer uma
bomba atômica.'''
import random

player1 = input('P1, Selecione a sua lendária jogada: ')
player2 = input('P2, Selecione a sua lendária jogada: ')

if player1 == player2:
    resultado = "empate"
resultado = random.choice([player1, player2])
print(f'⚔️  {player1} contra {player2} ⚔️')
print(f'🏆 O vencedor foi: {resultado}🏆')